import requests
from datetime import datetime
import json

now=datetime.now().isoformat()
print(now)
url='http://api.yeelink.net/v1.0/device/356096/sensor/403249/datapoints'
headers={'U-ApiKey':'bc85c66d54a3a1526bd992b1918e27ef'}
payload={"timestamp":now,"value":400}
r=requests.post(url,headers=headers,data=json.dumps(payload))
print(r)