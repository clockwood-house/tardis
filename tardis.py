import sys
from requests import get

sys.path.append('..')  # persistent import directory for K9 secrets

from k9secrets import token


url = "http://octopi.local:8123/api/services"
headers = {
    "Authorization": token,
    "content-type": "application/json",
}

response = get(url, headers=headers)
print(response.text)

