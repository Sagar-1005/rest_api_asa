import requests
from requests.auth import HTTPBasicAuth
from getpass import getpass
import json

asa_url='https://192.168.188.136/api/interfaces/physical'

username= input('Please input username: ')
password= getpass('Please enter password: ')
auth= HTTPBasicAuth(username=username,password=password)
heders={
    'Accept':'application/json'
}
payload= {
  "securityLevel": 0,
  "kind": "object#GigabitInterface",
  "channelGroupMode": "active",
  "flowcontrolLow": -1,
  "name": "gig3",
  "duplex": "auto",
  "forwardTrafficSFR": False,
  "hardwareID": f"GigabitEthernet0/{input('Enter config: ')}",
  "mtu": 1500,
  "lacpPriority": -1,
  "flowcontrolHigh": -1,
  "ipAddress": {
    "ip": {
      "kind": "IPv4Address",
      "value": "192.168.33.32"
    },
    "kind": "StaticIP",
    "netMask": {
      "kind": "IPv4NetMask",
      "value": "255.255.255.0"
    }
  },
  "flowcontrolOn": False,
  "shutdown": True,
  "interfaceDesc": "Add description test",
  "managementOnly": False,
  "channelGroupID": "",
  "speed": "auto",
  "forwardTrafficCX": False,
  "flowcontrolPeriod": -1
}

response= requests.put(url=asa_url,
                        auth=auth,
                        headers=heders,
                        data=payload,
                        verify=False)

print(response)
print(type(response.status_code))
# output=json.loads(response.text)
# print(type(output))
output=json.dumps(json.loads(response.text),indent=4)
print(output)
with open("backup.txt","a") as file:
    file.write(output)