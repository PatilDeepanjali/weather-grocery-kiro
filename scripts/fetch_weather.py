# fetch_weather.py
import requests, json, os

# Read API key from environment variable
API_KEY = os.getenv('0e2ac22287e368c89076e512f541f17f')

CITY = "Mumbai"

# Build the API URL correctly
url = f'https://api.openweathermap.org/data/2.5/forecast?q={CITY}&units=metric&appid={"0e2ac22287e368c89076e512f541f17f"}'


# Fetch weather data
resp = requests.get(url)
resp.raise_for_status()

# Save response into dashboard/weather.json
with open('dashboard/weather.json', 'w') as f:
    json.dump(resp.json(), f)

print("weather saved")
