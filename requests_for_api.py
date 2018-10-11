GET:
import requests
response = requests.get('enter URL')
response.status_code
print (response.json())

import requests
import json
for id in [11]:
    response = requests.get('enter URL'+ str (id))
print (response.status_code)
print (response.json())

POST:
import requests
import json
header = {'Content-Type': "application/json"}
body = json.dumps({'name': 'enter Name',
'position': 'enter Position'})
response = requests.post('enter URL', headers=header, data=body)
print (response.status_code)
print (response.json())

DELETE:
import requests
import json
for id in [11, 12, 13]:
    response = requests.delete('enter URL' + str (id))
print (response.status_code)
print (response.json())