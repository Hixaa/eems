import requests
import json

URL = "https://boilerlive.xaees.com/api/v1/inOutEntry"

d = [
'{"DateTime":"2023-06-23 11:10:00","UID":"1234ABCDEF","DoorNo":"5","Status":"1"}',
'{"DateTime":"2023-06-23 11:10:00","UID":"1234ABCDEF","DoorNo":"5","Status":"2"}',
'{"DateTime":"2023-06-23 11:10:00","UID":"1234ABCDEF","DoorNo":"5","Status":"1"}',
'{"DateTime":"2023-06-23 11:10:00","UID":"1234ABCDEF","DoorNo":"5","Status":"2"}']
json_data_list = []

for line in d:
    x = json.loads(line)
    x = {"DateTime": x['DateTime'],"UID": x['UID'],"DoorNo": x['DoorNo'],"Status": x['Status']}
    json_data_list.append(x)

# print("[+]", json_data_list)
jsonArrObj = json.loads(json.dumps({"entry":json_data_list}))
# print("[+]", str(json.dumps(jsonArrObj)))
      
payload = {'data':str(json.dumps(jsonArrObj))}
print("[+] Payload:", payload)

files=[]
headers = {}
response = requests.request("POST", URL, headers=headers, data=payload, files=files)
print("[+] RESPONSE: ", response.text)