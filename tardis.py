import sys
import time
from requests import post

sys.path.append('..')  # persistent import directory for K9 secrets

from k9secrets import token

token = "Bearer " +  token

on_url = "http://octopi.local:8123/api/services/light/turn_on"
off_url = "http://octopi.local:8123/api/services/light/turn_off"
payload = { "entity_id" : "light.33648804cc50e3ef7048"}
headers = {
    "Authorization": token,
    "content-type": "application/json",
}

while True:
    try:
        response = post(on_url, headers=headers, json=payload )
        time.sleep(1.0)
        print(response)
        response = post(off_url, headers=headers, json=payload )
        time.sleep(1.0)
        print(response)
    except KeyboardInterrupt:
        response = post(off_url, headers=headers, json=payload )
        print("Clean exit, light should go off")
        sys.exit(0)


