#!/usr/bin/python

import requests

url = 'https://api.kairos.com/recognize'

values =  {
    
    "gallery_name": "Asimov"
  }


headers = {
    'app_id': '15d495c3',
    'app_key': 'dbf71210732663c17ef0b6b365c41be5'
}

files = {'image': open('kolamaavu_coco_nayanthara.jpg', 'rb')}

r = requests.post(url, data=values, headers=headers, files=files)


print r.text
