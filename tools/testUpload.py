import requests

url = "https://rakshaiot.com/api/v1/ioEntry"

payload = {'data': '{"entry":[{"dt":"2021-04-14 15:45:00","cid":"2","uid":"1234ABCDEF","gn":"2","io":"2"},{"dt":"2021-04-14 15:50:00","cid":"2","uid":"1234ABCDEF","gn":"2","io":"1"}]}'}
files=[

]
headers = {}

response = requests.request("POST", url, headers=headers, data=payload, files=files)

print("response")
print(response.status_code)
