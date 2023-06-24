import requests
import json

url = 'http://boilerlive.xaees.com/api/v1/inOutEntry'
data = [{"DateTime":"2023-06-22 15:28:00","UID":"1234ABCDEF","DoorNo":"1","Status":"1"},{"DateTime": "2022-09-07 20:05:02","DoorNo":"1","Status":"2"}]

jsonObj = json.loads(data) # type: ignore

x = requests.post(url,json=data)

print(x.text)
