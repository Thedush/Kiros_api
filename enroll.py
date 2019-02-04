#!/usr/bin/python

import requests

url = 'https://api.kairos.com/enroll'

values =  {
    "subject_id": "Navaneeth",
    "gallery_name": "check1"
  }


headers = {

    'app_id': '027a95d0',
    'app_key': '3b5372ff123773c8abe788239ac462c8'
}
# image = ['test3.jpeg']
image = ['pp.jpeg','image1.jpg']
for i in image:
	files = {'image': open(i, 'rb')}
	r = requests.post(url, data=values, headers=headers, files=files)
	print r.content
