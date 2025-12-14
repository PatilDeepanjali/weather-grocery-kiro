# Weather vs Grocery Demand Predictor  
*Kiro Heroes Challenge – Week 3: The Data Weaver*

---

##  Overview
This project demonstrates how **two unrelated datasets — weather data and grocery demand trends — can be woven together** to uncover meaningful and actionable insights.

Using **Kiro automation**, the system fetches weather data, merges it with grocery demand trends, computes correlations, and visualizes the results in a live interactive dashboard.

---

##  Problem Statement
Weather conditions strongly influence consumer behavior, but these effects are often hidden when datasets are analyzed independently.

This project explores questions such as:
- Do hotter days increase cold drink demand?
- Does rainfall influence soup consumption?
- How does temperature affect snack demand?

By weaving weather and grocery data together, the dashboard reveals patterns that would otherwise remain unnoticed.

---

##  Datasets Used

### 1️⃣ Weather Data (Live API)
- **Source:** OpenWeatherMap API  
- **Metrics:**
  - Temperature
  - Precipitation probability  
- **Granularity:** Hourly forecast data  

### 2️⃣ Grocery Demand Trends (Custom Dataset)
- **Items Tracked:**
  - Noodles
  - Soup
  - Cold Drink
  - Ice Cream
  - Tea  
- **Granularity:** Daily values  

Although these datasets are unrelated, combining them reveals real-world demand behavior.

---

##  Automation with Kiro
Kiro is used to automate the entire data pipeline:

1. Fetch live weather data  
2. Load grocery demand trends  
3. Merge datasets and compute correlations  
4. Generate a unified dataset for visualization  

All automation is defined using a **Kiro workflow (`workflow.yaml`)**, enabling scheduled and repeatable execution.

---

##  Insights Generated
The dashboard automatically computes correlations and displays insights such as:

- 🔶 Hotter days strongly increase cold drink demand  
- 🔶 Rainy conditions correlate with higher soup interest  
- 🔷 Cooler days reduce certain snack demand  

These insights are calculated programmatically and updated automatically.

---

##  Dashboard Features
- Line chart for temperature and precipitation trends  
- Line chart for grocery demand trends  
- Insight cards with correlation values  
- Auto-generated recommendations based on data  

---

##  Tech Stack
- **Automation & Backend:** Python, Kiro workflows  
- **Data Processing:** NumPy  
- **Frontend:** HTML, CSS, JavaScript  
- **Visualization:** Chart.js  
- **Hosting:** GitHub Pages / Kiro storage  

---

## 📁 Project Structure

/.kiro
workflow.yaml
README.md (link)
/scripts
fetch_weather.py
fetch_trends.py
merge_and_clean.py
/dashboard
index.html
app.js
styles.css
/docs
blog_draft.md