import sys
import time
from requests import post

sys.path.append('..')  # persistent import directory for K9 secrets

from k9secrets import token

token = "Bearer " +  token

on_url = "http://octopi.local:8123/light/turn_on"
off_url = "http://octopi.local:8123/light/turn_off"
payload = { "entity_id" : "light.33648804cc50e3ef7048"}
headers = {
    "Authorization": token,
    "content-type": "application/json",
}

while True:
    try:
        response = get(on_url, headers=headers, json=payload )
        time.sleep(1.0)
        response = get(off_url, headers=headers, json=payload )
        time.sleep(1.0)
    except KeyboardInterrupt:
        response = get(off_url, headers=headers, json=payload )
        print("Clean exit, light should go off")


