#!/usr/bin/env python

import requests

# put your keys in the header
headers = {
    "app_id": "15d495c3",
    "app_key": "dbf71210732663c17ef0b6b365c41be5"
}

payload = '{"image":"http://media.kairos.com/kairos-elizabeth.jpg"}'

url = "http://api.kairos.com/detect"

# make request
r = requests.post(url, data=payload, headers=headers)
print r.content