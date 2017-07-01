import requests
from datetime import datetime
import json

now = datetime.now().isoformat()
print(now)
url = 'http://api.heclouds.com/devices/9087827/datapoints?type=3'
headers = {'api-key': 'EazpwgBmpqo=S4Uhl=BOgGyWQqY='}
payload = {"PM2_5": 105}
r = requests.post(url, headers=headers, data=json.dumps(payload))

print(r)
