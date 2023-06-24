import requests
import json
from requests.structures import CaseInsensitiveDict
from collections import namedtuple
from components.appConfig import Config
from components.storejson import StoreJson
import subprocess
from time import sleep
from components.statusLeds import statusLED

class CloudService:
    def __init__(self):
        self.__config = Config()
        self.__url = self.__config.url()
        self.__storeData = StoreJson()
        self.__ledtstat = statusLED()
    
    def __UserData(self,userData):
        return namedtuple('X', userData.keys())(*userData.values())

    def __dataFormat(self, data):
        return {"DateTime":data.DateTime,"UID":data.UID,"DoorNo":data.DoorNo,"Status":data.Status}
    def push(self,data):
        try:
            json_data_list = []
            for line in data:
                d = json.loads(line.strip(), object_hook=self.__UserData)
                # TODO: Add company id in list
                json_data_list.append(self.__dataFormat(d))

            files=[]
            headers = {}

            jsonArrObj = json.loads(json.dumps({"entry":json_data_list}))
            payload = {'data':str(json.dumps(jsonArrObj))}
            resp = requests.request("POST", self.__url, headers=headers, data=payload, files=files)
            
            # print("Status_raw: ",resp.text)
            dict_data = json.loads(resp.text)
            print("[+] Status_dict: ", dict_data)
            if(dict_data['success'] == 1):
                print("[+] Successfully Added Data!")
                self.__ledtstat.dataUploadStat_Show()
            else:
                # self.__storeData.pushLocal(data)
                print("[+] Added Data Locally!")
                print("[!] Not Successfully Added Data! Server Issue !")
                raise Exception("Server Issue")

        except:
            self.__storeData.pushLocal(data)
            print("[+] Added Data Locally!!")
            print("[!] Error in Data Push. Network Issue!")

    def autoSync(self):
        while True:
            # FIXME: Change OR to AND
            if(self.__storeData.checkAvailable_Files(recent = False) and self.__ping_server()):
                try:
                    json_data_list=[]
                    data = self.__storeData.getJsonArray()
                    for line in data:
                        d = json.loads(line.strip(),object_hook=self.__UserData)
                        json_data_list.append(self.__dataFormat(d))
                    
                    files=[]
                    headers = {}
                    jsonArrObj = json.loads(json.dumps({"entry":json_data_list}))
                    payload = {'data':str(json.dumps(jsonArrObj))}
                    resp = requests.request("POST", self.__url, headers=headers, data=payload, files=files)

                    print("[+] Status_raw: ",resp.text)
                    dict_data = json.loads(resp.text)
                    print("[+] Status_dict: ", dict_data)
                    if(dict_data['success'] == 1):
                        print("[+] Successfully Added Data!")
                        self.__ledtstat.dataUploadStat_Show()
                        self.__storeData.truncateFile()
                    else:
                        print("[!] AutoSync: Not Successfully Added Data! Server Issue !")
                except:
                    print("[!] AutoSync: Network Issue!")
            else:
                print("[!] DataStorage Files are not available!")
            sleep(1)

    def __ping_server(self):
        cmd = ['ping','-c','1','boilerlive.xaees.com']
        return subprocess.call(cmd) == 0
