#!/usr/bin/python

import requests

url = "https://api.kairos.com/detect"

headers = {
    'app_id': '15d495c3',
    'app_key': 'dbf71210732663c17ef0b6b365c41be5'
    }

files = {'image': open('img2.jpg', 'rb')}

r = requests.post( url, headers=headers, files=files )

print r.text

