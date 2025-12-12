# fetch_trends.py (uses pytrends)
from pytrends.request import TrendReq
import json, os
pytrends = TrendReq(hl='en-US', tz=330)
keywords = ['noodles', 'soup', 'cold drink', 'ice cream', 'tea']
pytrends.build_payload(keywords, cat=0, timeframe='now 7-d', geo='IN')
trends = pytrends.interest_over_time().reset_index().to_dict(orient='records')
with open('dashboard/trends.json','w') as f:
json.dump(trends, f)
print('trends saved')