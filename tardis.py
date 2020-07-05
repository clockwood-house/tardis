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

server = "octopi.local:8123"
tardis_roof  = "light.33648804cc50e3ef7048"
tardis_int = "light.33648804cc50e3ef73b5"

#on_url = "http://octopi.local:8123/api/services/light/turn_on"
#off_url = "http://octopi.local:8123/api/services/light/turn_off"

def device(domain,service,entity_id):
    global server
    myURL = "http://" + server + "/api/services/" + domain + "/" + service
    print(myURL)
    payload = { "entity_id" : entity_id }
    response = post(myURL, headers=headers, json=payload )
    return response

def light(light,status):
    if status :
        response = device("light","turn_on",light)
        return response
    else :
        response = device("light","turn_off",light)
        return response

for x in range(5):
    response = light(tardis_roof,1)
    time.sleep(1.0)
    print(response)
    response = light(tardis_roof,0)
    time.sleep(1.0)
    print(response)
response = light(tardis_int,1)
time.sleep(10.0)
for x in range(5):
    response = light(tardis_roof,1)
    time.sleep(1.0)
    print(response)
    response = light(tardis_roof,0)
    time.sleep(1.0)
    print(response)
response = light(tardis_int,0)



