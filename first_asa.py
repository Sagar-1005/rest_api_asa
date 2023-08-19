import requests
from requests.auth import HTTPBasicAuth
from getpass import getpass
import json

asa_url='https://192.168.188.136/api/monitoring/device'

username= input('Please input username: ')
password= getpass('Please enter password: ')
auth= HTTPBasicAuth(username=username,password=password)
heders={
    'Accept':'application/json'
}

response= requests.get(url=asa_url,
                        auth=auth,
                        headers=heders,
                        verify=False)

print(response)
print(type(response.text))
# output=json.loads(response.text)
# print(type(output))
print(json.dumps(json.loads(response.text),indent=4))