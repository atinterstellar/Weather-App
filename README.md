# Weather App

A small Flask app that looks up current weather for any city, built as a quick one-day project to get comfortable consuming an external API and wiring it up to a real (if bare-bones) web app instead of just a script.

Nothing fancy here — no database, no auth, no styling to speak of. It hits the [Visual Crossing](https://www.visualcrossing.com/weather-api) API, converts the numbers from Fahrenheit to Celsius, and renders them into a couple of templates. Good for practicing Flask routing and working with a real third-party API response instead of toy data.

## Features

- Look up today's weather for any city by name
- Temperature (current, max, min, feels-like) converted from °F to °C
- Separate wind page showing wind speed, gusts, and direction (defaults to Delhi if no city is given)

## Tech Stack

- Python 3 / Flask
- [Visual Crossing Weather API](https://www.visualcrossing.com/weather-api) (JSON, `timeline` endpoint)
- `requests` for HTTP calls
- Jinja2 templates (`home.html`, `city.html`, `weather.html`, `wind.html`)

## Project Structure

```
Weather-App/
├── app.py           # Flask routes: /, /city, /weather, /wind
├── methods.py       # Unit conversion helpers (F→C, F→K)
├── Response.py       # Standalone script for testing the API call directly (not used by app.py)
├── api_key.txt      # Visual Crossing API key (plain text)
├── static/
└── templates/
```

## Setup

1. Install dependencies:
   ```
   pip install flask requests
   ```
2. Get a free API key from [Visual Crossing](https://www.visualcrossing.com/weather-api) and put it in `api_key.txt` in the project root (just the key, no quotes or extra whitespace).
3. Run the app:
   ```
   python app.py
   ```
4. Visit `http://localhost:5103`

That's it — no database setup, no migrations, no config beyond the API key.

## Routes

| Route | Method | Description |
|---|---|---|
| `/` , `/home` | GET | Landing page |
| `/city` | GET/POST | Form to submit a city name |
| `/weather` | GET | Shows today's temperature data for `?name=<city>` |
| `/wind` | GET | Shows wind data for `?name=<city>` (defaults to Delhi) |

## Known Issues / Things to Fix Before Sharing This Publicly

Since this is sitting in a public repo, worth being upfront about the current state rather than pretending it's production-ready — it's a one-day learning project, not a shipped product, and it shows:

- **The API key is committed to the repo** (`api_key.txt` is tracked in git). Anyone who clones this can read your key. It should be removed from version control, rotated, and loaded from an environment variable or a `.gitignore`'d file instead.
- **`__pycache__` and `.DS_Store` are also committed.** Add a `.gitignore` (Python + macOS templates) so these stop showing up in every diff.
- **No error handling.** If the city name is invalid or the API call fails, `response["days"][0]` will throw a raw `KeyError`/`IndexError` and the user gets a Flask stack trace instead of a friendly error.
- **`debug=True` in `app.run()`.** Fine for local dev, but this must never run in production — it exposes the Werkzeug debugger, which allows arbitrary code execution if reachable externally.
- **Global mutable state** (`place` and `response` as module-level globals in `app.py`) — this isn't thread-safe and will misbehave under concurrent requests. Pass data through Flask's `request`/`session` instead.
- **`Response.py` looks like a leftover scratch/test file** rather than part of the app (it duplicates the API-key-loading logic and just prints a raw response). Worth moving to a `scripts/` or `tests/` folder, or removing, so it's clear it's not part of the request path.
- **No caching**, despite this project having been scoped as an exercise in SQLite-based response caching with TTL invalidation — the current code hits the live API on every request. If that's still the plan, it's not in this version of the repo yet.
- **No `requirements.txt`** — setup currently relies on the reader guessing `flask` and `requests` are the only dependencies.

## What's Next

If this gets picked back up, the natural next steps are: fix the API key exposure, add a `.gitignore`, wrap the weather lookup in a try/except with a proper error page, and — per the original plan for this exercise — add a SQLite caching layer with TTL invalidation so repeat lookups for the same city don't hit the live API every time.

## License

Not specified.