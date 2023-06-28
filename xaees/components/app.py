import sys
import threading
from time import sleep
from datetime import datetime
from components.rfidReader import RFID
from components.gate import Gate
from components.cloudService import CloudService
from components.statusLeds import statusLED
from components.appConfig import Config

# rfid gate direction 
INSIDE_STATUS = 1
OUTSIDE_STATUS = 2

class App:
    def __init__(self):
        try:
            self.__myrfid = RFID()
            # print("[!] OSError Occured!! Retrying...")
            self.__config = Config()
            # TODO: add companyId 
            # self.__companyID = self.__config.companyId()
            self.__gateNo = Gate().read()
            self.__cloud = CloudService()
            self.__ledstat = statusLED()
            self.__uid1 = ''
            self.__uid2 = ''
            self.__data = []
            self.__ledstat.sysReady_Show(True)
            self.__DATA_FORMAT = '{"DateTime":"%s","UID":"%s","DoorNo":"%d","Status":"%d"}'
        except:
            self.__ledstat.sysReady_Show(False)

    def __rfidDirection(self, uid):
        if (uid[0] == 'O'):
            return int(OUTSIDE_STATUS)
        elif (uid[0] == 'I'):
            return int(INSIDE_STATUS)

    def __rfidCapture(self):
        while True:
            try:
                self.__uid1 = self.__myrfid.getUID(1) #Outside
                self.__uid2 = self.__myrfid.getUID(2) #Inside
                
                self.__DateTime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                # TODO: add company id in the json data
                if(self.__uid1 != None and self.__uid1 != 'None'): #Outside       Sends "O_"
                    print("[+] RFID1: ", self.__rfidDirection(self.__uid1), "\t", self.__uid1)
                    formattedData_1 = self.__DATA_FORMAT%(self.__DateTime, self.__uid1[14:], self.__gateNo, self.__rfidDirection(self.__uid1))
                    print("RFID1: ",formattedData_1)
                    self.__data.append(formattedData_1)
                    
                
                if(self.__uid2 != None and self.__uid2 != 'None'): #Inside        Sends "I_"
                    print("[+] RFID2: ", self.__rfidDirection(self.__uid2), "\t", self.__uid2)
                    formattedData_2 = self.__DATA_FORMAT%(self.__DateTime, self.__uid2[14:], self.__gateNo, self.__rfidDirection(self.__uid2))
                    print("RFID2: ",formattedData_2)
                    self.__data.append(formattedData_2)

            except Exception as e:
                print("[!] Exception Occured: ", e)
                print("[+] xaees App exited safely!")
                self.__myrfid.close()
                self.__ledstat.close()
                sys.exit()

    def __dataSync(self):
        while True:
            if(len(self.__data) > 0):
                d = [self.__data.pop(0)]
                print("[+] Syncing!!!--> Called")
                self.__cloud.push(d)
                #self.__data = []

    def run(self):
        try:
            rfidCapture_Thread = threading.Thread(target = self.__rfidCapture)
            dataSync_Thread = threading.Thread(target = self.__dataSync)
            autoSync_Thread = threading.Thread(target = self.__cloud.autoSync)
            rfidCapture_Thread.start()
            dataSync_Thread.start()
            autoSync_Thread.start()
            rfidCapture_Thread.join()
            dataSync_Thread.join()
            autoSync_Thread.join()        
        except:
            self.close()
            self.__ledstat.close()

        
    def close(self):
        self.__myrfid.close()
        sys.exit()
