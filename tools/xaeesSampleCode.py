import requests
from requests.structures import CaseInsensitiveDict
import json
from collections import namedtuple

def UserData(userData):
    return namedtuple('X', userData.keys())(*userData.values())

url = 'https://boilerlive.xaees.com/api/v1/inOutEntry'
json_data_list = []

#f = open("data.txt","r",encoding='UTF-8')
lines = ['{"DateTime":"2022-08-02 15:39:49","UID":"04F1B1F098CC","DoorNo":"5","Status":"2"}','{"DateTime":"2022-08-02 15:39:51","UID":"04F1B1F098CC","DoorNo":"5","Status":"2"}']

for line in lines:
    x = json.loads(line.strip(), object_hook=UserData)
    #print(x.UID)
    json_data_list.append({"DateTime":x.DateTime,"UID":x.UID,"DoorNo":x.DoorNo,"Status":x.Status})


#print(json_data_list)

jsonArrObj = json.loads(json.dumps({"entry":json_data_list}))
#print(json.dumps(jsonArrObj, indent = 3))

headers = CaseInsensitiveDict()
headers["Content-Type"] = "application/x-www-form-urlencoded"
data = "data="+str(json.dumps(jsonArrObj, indent = 3))
x=requests.post(url,headers=headers,data=data)

print(x.status_code)
print(x.text)
