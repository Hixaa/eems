import requests
import json
from requests.structures import CaseInsensitiveDict
from collections import namedtuple

def UserData(userData):
    return namedtuple('x', userData.keys())(*userData.values())

url = "http://boilerlive.xaees.com/api/v1/inOutEntry"

d = ['{"DateTime":"2033-06-21 14:40:18","UID":"031BA9F55BE3","DoorNo":"5","Status":"2"}',
'{"DateTime":"2033-06-21 14:40:18","UID":"031BA4664989","DoorNo":"5","Status":"1"}',
'{"DateTime":"2033-06-21 14:40:18","UID":"061D8401EE64","DoorNo":"5","Status":"2"}',
'{"DateTime":"2033-06-21 14:40:18","UID":"06951939FE0F","DoorNo":"5","Status":"1"}',
'{"DateTime":"2033-06-21 14:40:18","UID":"031BA9F55BE3","DoorNo":"5","Status":"1"}',
'{"DateTime":"2033-06-21 14:40:18","UID":"061D8401EE64","DoorNo":"5","Status":"1"}',
'{"DateTime":"2033-06-21 14:40:19","UID":"031BA4664989","DoorNo":"5","Status":"2"}',
'{"DateTime":"2033-06-21 14:40:19","UID":"04F1B6F52337","DoorNo":"5","Status":"2"}',
'{"DateTime":"2033-06-21 14:40:48","UID":"04F1B6F52337","DoorNo":"5","Status":"2"}',
'{"DateTime":"2033-06-21 14:40:48","UID":"031BA4664989","DoorNo":"5","Status":"2"}',
'{"DateTime":"2033-06-21 14:40:49","UID":"061D8401EE64","DoorNo":"5","Status":"1"}',
'{"DateTime":"2033-06-21 14:40:50","UID":"061D8401EE64","DoorNo":"5","Status":"2"}',
'{"DateTime":"2033-06-21 14:40:50","UID":"031BA4664989","DoorNo":"5","Status":"2"}',
'{"DateTime":"2033-06-21 14:40:50","UID":"04F1B6F52337","DoorNo":"5","Status":"2"}',
'{"DateTime":"2033-06-21 14:40:50","UID":"061D8401EE64","DoorNo":"5","Status":"1"}',
'{"DateTime":"2033-06-21 14:40:50","UID":"031BA4664989","DoorNo":"5","Status":"1"}',
'{"DateTime":"2033-06-21 14:40:51","UID":"04F1B6F52337","DoorNo":"5","Status":"1"}',
'{"DateTime":"2033-06-21 14:40:51","UID":"031BA4664989","DoorNo":"5","Status":"2"}',
'{"DateTime":"2033-06-21 14:40:52","UID":"04F1B6F52337","DoorNo":"5","Status":"2"}',
'{"DateTime":"2033-06-21 14:40:52","UID":"061D8401EE64","DoorNo":"5","Status":"2"}',
'{"DateTime":"2033-06-21 14:40:52","UID":"061D8401EE64","DoorNo":"5","Status":"1"}',
'{"DateTime":"2033-06-21 14:40:52","UID":"04F1B6F52337","DoorNo":"5","Status":"1"}']

'''
d = [
'{"DateTime":"2023-06-19 16:42:52","UID":"04F1B6F52337","DoorNo":"5","Status":"2"}',
'{"DateTime":"2023-06-19 16:52:52",UID":"061D8401EE64","DoorNo":"5","Status":"2"}',
'{"DateTime":"2023-06-19 17:02:52","UID":"061D8401EE64","DoorNo":"5","Status":"1"}',
'{"DateTime":"2023-06-19 17:12:52","UID":"04F1B6F52337","DoorNo":"5","Status":"1"}']'''
json_data_list = []

for line in d:
    x = json.loads(line.strip(), object_hook=UserData)
    json_data_list.append({"DateTime":x.DateTime,"UID":x.UID,"DoorNo":x.DoorNo,"Status":x.Status})

jsonArrObj = json.loads(json.dumps({"entry":json_data_list}))
print(str(json.dumps(jsonArrObj)))
      
payload = {'data':str(json.dumps(jsonArrObj))}
print(payload)

files=[]
headers = {}
response = requests.request("POST", url, headers=headers, data=payload, files=files)

print(response.text)
