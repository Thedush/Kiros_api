#!/usr/bin/python

import requests
import json

url = 'https://api.kairos.com/recognize'

values =  {
    
    "gallery_name": "check1"
  }


headers = {
    'app_id': '027a95d0',
    'app_key': '3b5372ff123773c8abe788239ac462c8'
}

files = {'image': open('full.jpg', 'rb')}

r = requests.post(url, data=values, headers=headers, files=files)


# print r.text

image = json.loads(r.text)["images"]
for f in image:
	count = f["transaction"]
	if count["status"] == "failure" :
		print 'unknown'
	else:
		print count["subject_id"]
