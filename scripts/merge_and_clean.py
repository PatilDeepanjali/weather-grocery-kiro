# merge_and_clean.py
import json
from datetime import datetime


with open('dashboard/weather.json') as f:
w = json.load(f)
with open('dashboard/trends.json') as f:
t = json.load(f)


# Simplify weather: extract date, temp, pop (probability of precipitation)
weather_points = []
for item in w.get('list',[]):
dt = item['dt_txt']
temp = item['main']['temp']
pop = item.get('pop',0)
weather_points.append({'dt':dt,'temp':temp,'pop':pop})


# trends already has timestamp keys; convert to daily averages for keywords
# Example transform depending on pytrends structure
from collections import defaultdict
agg = defaultdict(lambda: defaultdict(list))
for row in t:
    date = row.get('date') or row.get('index')
for k in ['noodles','soup','cold drink','ice cream','tea']:
if k in row:
agg[date][k].append(row[k])


trends_points = []
for date,vals in agg.items():
avg = {k: sum(v)/len(v) if v else 0 for k,v in vals.items()}
trends_points.append({'date':str(date),'metrics':avg})


# Output merged json for dashboard
out = {'weather':weather_points,'trends':trends_points,'generated_at':str(datetime.utcnow())}
with open('dashboard/data.json','w') as f:
json.dump(out,f)
print('merged data saved')
