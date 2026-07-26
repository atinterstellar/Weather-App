# REFERENCE FILE

import os
import requests

script_dir = os.path.dirname(os.path.abspath(__file__))
key_path = os.path.join(script_dir, 'api_key.txt')

with open(key_path, 'r') as f:
    API_KEY = f.read().strip()

BASE_URL = "https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline"
name = 'Delhi'
url = f"{BASE_URL}/{name}"
params = {"key": API_KEY, "contentType": "json"}

response = requests.get(url, params=params, timeout=5)
print("Status code:", response.status_code)
print("Raw response:", response.text)