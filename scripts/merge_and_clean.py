import json
from datetime import datetime
import numpy as np

# Load weather
with open('dashboard/weather.json') as f:
    weather_raw = json.load(f)

weather_points = []
for item in weather_raw.get('list', []):
    weather_points.append({
        "dt": item["dt_txt"][:10],  # date only (YYYY-MM-DD)
        "temp": item["main"]["temp"],
        "pop": item.get("pop", 0)
    })

# Load trends (from CSV-made JSON)
with open('dashboard/trends.json') as f:
    trends_raw = json.load(f)

# Build daily aligned lists
dates = [t["date"] for t in trends_raw]

temps = []
pops = []
noodles = []
cold_drink = []
soup = []

# Map weather to same dates as trends
weather_by_date = {}
for w in weather_points:
    d = w["dt"]
    if d not in weather_by_date:
        weather_by_date[d] = {"temps": [], "pops": []}
    weather_by_date[d]["temps"].append(w["temp"])
    weather_by_date[d]["pops"].append(w["pop"])

def avg(values):
    values = [v for v in values if v is not None]
    return sum(values)/len(values) if values else None


for t in trends_raw:
    d = t["date"]
    metrics = t["metrics"]
    noodles.append(metrics["noodles"])
    cold_drink.append(metrics["cold_drink"])
    soup.append(metrics["soup"])

    # weather for this day
    wd = weather_by_date.get(d, {"temps": [None], "pops": [None]})
    temps.append(avg(wd["temps"]))
    pops.append(avg(wd["pops"]))

# Convert Nones → drop during correlation
def correlation(a, b):
    paired = [(x, y) for x, y in zip(a, b) if x is not None and y is not None]
    if len(paired) < 3:
        return None
    x, y = zip(*paired)
    return float(np.corrcoef(x, y)[0, 1])

correlations = {
    "temp_noodles": correlation(temps, noodles),
    "temp_cold_drink": correlation(temps, cold_drink),
    "rain_soup": correlation(pops, soup)
}

output = {
    "weather": weather_points,
    "trends": trends_raw,
    "correlations": correlations,
    "generated_at": str(datetime.utcnow())
}

with open("dashboard/data.json", "w") as f:
    json.dump(output, f, indent=2)

print("merged data saved with correlations")
