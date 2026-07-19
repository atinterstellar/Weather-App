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
    if request.method == 'POST' :
        place = request.form.get('city')
        return redirect(url_for('weather', name=place))
    return render_template('city.html')

@app.route('/weather')
def weather() :
    name = request.args.get("name")
    url = f"{base}/{name}/today"
    params = {"key": API_KEY, "contentType": "json"}
    response = requests.get(url, params=params, timeout=5).json()
    maxxc , minnc , feelc , tempc = mt.to_c(response["days"][0]["tempmax"]) , mt.to_c(response["days"][0]["tempmin"]) , mt.to_c(response["days"][0]["feelslike"]) , mt.to_c(response["days"][0]["temp"]) 
    return render_template('weather.html' , response = response , maxxc = maxxc , minnc = minnc , feelc = feelc , tempc= tempc)


if __name__ == '__main__' :
    app.run(host = '0.0.0.0' , port = 5103 , debug = True)
