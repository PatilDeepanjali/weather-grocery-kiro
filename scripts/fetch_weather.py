# fetch_weather.py
import requests
import json
import os

# Read API key from environment variable
API_KEY = os.getenv("OPENWEATHER_API_KEY")

if not API_KEY:
    raise ValueError("OPENWEATHER_API_KEY environment variable not set")

CITY = "Mumbai"

# Build the API URL using the API key safely
url = (
    f"https://api.openweathermap.org/data/2.5/forecast"
    f"?q={CITY}&units=metric&appid={API_KEY}"
)

# Fetch weather data
resp = requests.get(url)
resp.raise_for_status()

# Save response into dashboard/weather.json
with open("dashboard/weather.json", "w") as f:
    json.dump(resp.json(), f)

print("weather saved")
