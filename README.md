<div align="center">

# 🌦️ Weather App

**A Flask web app that turns a raw weather API into a real, browsable tool.**

Built to sharpen two specific skills: working with a live third-party REST API, and structuring a multi-route Flask app the right way — not just scripting a single API call.

[![Python](https://img.shields.io/badge/Python-3.x-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-Micro--framework-000000?logo=flask&logoColor=white)](https://flask.palletsprojects.com/)
[![Visual Crossing](https://img.shields.io/badge/API-Visual%20Crossing-00A3E0)](https://www.visualcrossing.com/weather-api)
[![Status](https://img.shields.io/badge/Status-Learning%20Project-yellow)]()

</div>

---

## Why this exists

This was a deliberate, scoped exercise — not an attempt to ship a product. The goal was to get comfortable with two things I wanted to strengthen before going further:

- **Consuming a real external API** — handling query params, API keys, and a live JSON response shape that I don't control (instead of practicing on data I made up myself).
- **Flask fundamentals, done properly** — routing, GET/POST form handling, and passing backend data cleanly into Jinja templates across multiple pages, rather than one script that prints to a console.

It's intentionally lean: no database, no auth, no styling framework. Depth over surface area — get the fundamentals solid first, then layer on complexity.

## What it does

| Route | Method | What it does |
|---|---|---|
| `/`, `/home` | GET | Landing page |
| `/city` | GET/POST | Form to submit a city name |
| `/weather` | GET | Current temp, high/low, and feels-like for `?name=<city>`, converted from °F to °C |
| `/wind` | GET | Wind speed, gusts, and direction for `?name=<city>` (defaults to Delhi) |
| `/rain` | GET | Condition, Rain, Rain Probablity, Snow, Snow Depth, Humidity, Dew | 

## Tech stack

- **Backend:** Python 3, Flask
- **API:** [Visual Crossing Weather API](https://www.visualcrossing.com/weather-api) (`timeline` endpoint, JSON)
- **HTTP:** `requests`
- **Templates:** Jinja2 (`home.html`, `city.html`, `weather.html`, `wind.html`)

## Project structure

```
Weather-App/
├── app.py           # Flask routes: /, /city, /weather, /wind
├── methods.py        # Unit conversion helpers (°F→°C)
├── Response.py        # Standalone script for testing the raw API call (not part of the app)
├── static/
└── templates/
```

## Getting started

```bash
git clone https://github.com/atinterstellar/Weather-App.git
cd Weather-App
pip install -r requirements.txt
```

Grab a free API key from [Visual Crossing](https://www.visualcrossing.com/weather-api), then set it as an environment variable rather than a tracked file:

```bash
export WEATHER_API_KEY=your_key_here
```

Run it:

```bash
python app.py
```

Visit `http://localhost:5103`.

## Roadmap

This is a living project. Next up:

- 🗄️ **SQLite caching layer with TTL invalidation** — the original point of this exercise; avoid re-hitting the live API for repeat city lookups
- 🛡️ **Error handling** — graceful responses for invalid cities or API failures instead of raw stack traces
- ✅ **Input validation** on the city form
- 📦 **`requirements.txt`** and a proper local dev setup

## Limitations

No database, no auth, minimal error handling, no automated tests — this is a fundamentals project, not a production app. Treat it accordingly.

---

<div align="center">
<sub>Built by <a href="https://github.com/atinterstellar">@atinterstellar</a> — first-year Chemical Engineering @ IIT Delhi, learning to build.</sub>
</div>