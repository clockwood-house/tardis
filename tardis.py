import sys
import time
import json
from requests import post

sys.path.append('..')  # persistent import directory for K9 secrets

from k9secrets import token

token = "Bearer " +  token
headers = {
    "Authorization": token,
    "content-type": "application/json",
}

URL = "octopi.local:8123"
tardis_roof  = "light.33648804cc50e3ef7048"

#on_url = "http://octopi.local:8123/api/services/light/turn_on"
#off_url = "http://octopi.local:8123/api/services/light/turn_off"

def device(domain,service,entity_id):
    global URL
    URL = "http://" + URL + "/api/services/" + domain + "/" + service
    payload = { "entity_id" : entity_id }
    json_obj = json.dumps(payload)
    response = post(URL, headers=headers, json=json_obj )
    return response

def light(light,status):
    if status :
        response = device("light","turn_on",light)
        return response
    else :
        response = device("light","turn_off",light)
        return response

while True:
    try:
        #response = post(on_url, headers=headers, json=payload )
        response = light(tardis_roof,1)
        time.sleep(1.0)
        print(response)
        #response = post(off_url, headers=headers, json=payload )
        #response = device(light,"turn_off",tardis_roof)
        response = light(tardis_roof,0)
        time.sleep(1.0)
        print(response)
    except KeyboardInterrupt:
        response = light(tardis_roof,0)
        print("Clean exit, light should go off")
        sys.exit(0)


