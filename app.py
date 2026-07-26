from flask import Flask , render_template , request , redirect, url_for
import methods as mt
import requests
import os


script_dir = os.path.dirname(os.path.abspath(__file__))
key_path = os.path.join(script_dir, 'api_key.txt')

with open(key_path, 'r') as f:
    API_KEY = f.read().strip()

base = "https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline"

app = Flask(__name__)

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')

place = None

@app.route('/city' , methods = ['GET', 'POST'])
def city():
    global place
    if request.method == 'POST' :
        place = request.form.get('city')
        return redirect(url_for('weather', name=place))
    return render_template('city.html')

response = None 

@app.route('/weather')
def weather() :
    name = request.args.get("name")
    url = f"{base}/{name}/today"
    params = {"key": API_KEY, "contentType": "json"}
    response = requests.get(url, params=params, timeout=5).json()
    maxxc , minnc , feelc , tempc = round(mt.to_c(response["days"][0]["tempmax"]),2) , round(mt.to_c(response["days"][0]["tempmin"]),2) , round(mt.to_c(response["days"][0]["feelslike"]),2) , round(mt.to_c(response["days"][0]["temp"]),2) 
    return render_template('weather.html' , response = response , maxxc = maxxc , minnc = minnc , feelc = feelc , tempc= tempc)

@app.route('/wind')
def wind():
    name = request.args.get("name")
    if name :
        url = f"{base}/{name}/today"
    else:
        url = f"{base}/Delhi/today"
    params = {"key": API_KEY, "contentType": "json"}
    response = requests.get(url, params=params, timeout=5).json()

    day = response["days"][0]
    windspeed = day["windspeed"]
    windgust  = day["windgust"]
    winddir   = day["winddir"]

    return render_template('wind.html', response=response, windspeed=windspeed, windgust=windgust, winddir=winddir)
    



if __name__ == '__main__' :
    app.run(host = '0.0.0.0' , port = 5103 , debug = True)
