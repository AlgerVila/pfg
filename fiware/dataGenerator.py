import requests
import time
import datetime
import random
import json

uri = "http://localhost:1026/v2/entities/Street1/attrs"
headers = {'Content-Type': 'application/json'}
temp = round(random.uniform(-5, 35),1)
presure = random.randrange(600,900)


while True:
    temp = round(random.uniform(temp - 1, temp + 1),1)
    presure = random.randrange(presure - 10, presure + 10)
    st = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    info = {  
        "temperature": {
            "value": str(temp),
            "type": "Float"
        },
        "pressure": {
            "value": str(presure),
            "type": "Float"
        },
            "time": {
            "value": st,
            "type": "String"
        }
    }
    requests.patch(url = uri, headers=headers, data = json.dumps(info))
    time.sleep(180)
    print("Hello")
   