# How Weather Shapes Grocery Demand: A Data-Weaving Dashboard Using Kiro

## Introduction
Consumer demand patterns are often influenced by external factors that are not immediately obvious when datasets are analyzed in isolation. Weather conditions such as temperature and rainfall play a significant role in shaping daily purchasing behavior, especially for grocery and food items.

In **Week 3 of the Kiro Heroes Challenge – “The Data Weaver”**, the goal was to combine two unrelated datasets and extract meaningful insights. In this project, I explored how **weather data** and **grocery demand trends** can be woven together to uncover actionable patterns using **Kiro automation**.

The result is an automated data pipeline and an interactive dashboard that highlights correlations between weather conditions and grocery demand.

---

## Data Sources

### Weather Data
Weather data is fetched using the **OpenWeatherMap API**, which provides a 5-day forecast with hourly granularity.

**Metrics used:**
- Temperature (°C)
- Precipitation probability
- Forecast timestamps

---

### Grocery Demand Trends
A curated grocery demand dataset is used to represent daily interest levels for common food items such as:
- Noodles
- Soup
- Cold drinks
- Ice cream
- Tea

Although this dataset is independent of weather data, weaving the two together reveals meaningful behavioral patterns.

---

## Automation with Kiro
Kiro is used to automate the entire data workflow, ensuring repeatability and consistency.

The automated pipeline performs the following steps:
1. Fetch live weather data  
2. Load grocery demand trends  
3. Merge datasets and compute correlations  
4. Publish processed data for dashboard visualization  

All steps are orchestrated using a **Kiro workflow (`workflow.yaml`)**, allowing the pipeline to run on a schedule without manual intervention.

---

## Dashboard Overview
The dashboard visualizes the woven datasets through:
- A line chart showing temperature and precipitation trends
- A line chart displaying grocery demand trends
- Insight cards highlighting computed correlations
- Automatically generated recommendations

---

## Key Insights
By weaving weather and grocery demand data together, the dashboard reveals several meaningful insights:
- Hotter days strongly correlate with increased cold drink demand
- Rainy conditions show a positive relationship with soup interest
- Temperature changes influence snack-based items such as noodles

These insights are calculated dynamically during the data merge process.

---

## How to Run the Project Locally

### Prerequisites
- Python 3.8+
- OpenWeatherMap API key

### Environment Setup
Set the API key as an environment variable:

### (For Linux/macOS)
export OPENWEATHER_API_KEY=your_api_key_here
### Run the Pipeline
python scripts/fetch_weather.py
python scripts/fetch_trends.py
python scripts/merge_and_clean.py
## Run the Dashboard
cd dashboard
python -m http.server 8000
### Open in browser:
http://localhost:8000

```bash
setx OPENWEATHER_API_KEY your_api_key_here


