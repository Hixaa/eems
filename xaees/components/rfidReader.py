import serial
from components.appConfig import Config
from components.statusLeds import statusLED

class RFID:
    def __init__(self):
        self.__config = Config()
        self.__ledtstat = statusLED()
        self.__RFID_CONFIG = [0xAA, 0x02, 0x10, 0x00, 0x02, 0x01, 0x01, 0x71, 0xAD]
        while True:
            try:
                self.__ser_rfid1 = serial.Serial(self.__config.rfid1Port(),self.__config.rfid1BaudRate(),parity=serial.PARITY_NONE,timeout=self.__config.rfid1TimeOut())
                self.__ser_rfid1.write(serial.to_bytes(self.__RFID_CONFIG)) # type: ignore
                self.__ser_rfid2 = serial.Serial(self.__config.rfid2Port(),self.__config.rfid2BaudRate(),parity=serial.PARITY_NONE,timeout=self.__config.rfid2TimeOut())
                self.__ser_rfid2.write(serial.to_bytes(self.__RFID_CONFIG)) # type: ignore
                if (self.__ser_rfid1.readline() != '' and self.__ser_rfid2.readline() != ''):
                    break
            except Exception as e:
                print("[!] Unable to configure RFID! - ", e)
                self.__ledtstat.Error_Show()
                continue
        # self.__ser_rfid1 = serial.Serial(self.__config.rfid1Port(),self.__config.rfid1BaudRate(),parity=serial.PARITY_NONE,timeout=self.__config.rfid1TimeOut())
        # self.__ser_rfid2 = serial.Serial(self.__config.rfid2Port(),self.__config.rfid2BaudRate(),parity=serial.PARITY_NONE,timeout=self.__config.rfid2TimeOut())
        self.__currRfid1 = ''
        self.__currRfid2 = ''
        self.__ser_rfid1.flush()
        self.__ser_rfid2.flush()
        # to ignore acknowledgement for configure
        self.__ser_rfid1.readline().decode(errors='ignore').strip()
        self.__ser_rfid2.readline().decode(errors='ignore').strip()



    def getUID(self,rfid=1):
        try:
            if(rfid == 1):
                self.__currRfid1 = self.__ser_rfid1.readline().decode(errors='ignore').strip()
                self.__ser_rfid1.flush()
                if(self.__currRfid1 != ''):
                    self.__ledtstat.rfidStat_Show()
                    # print("[+] Data REceive: ", self.__currRfid1)
                    return self.__currRfid1

            if(rfid == 2):
                self.__currRfid2 = self.__ser_rfid2.readline().decode(errors='ignore').strip()
                self.__ser_rfid2.flush()
                if(self.__currRfid2 != ''):
                    self.__ledtstat.rfidStat_Show()
                    return self.__currRfid2
        except Exception as e:
            print("[!] RFID Reader Error! - ", e)
            self.__ledtstat.Error_Show()
    
    def close(self):
        self.__ser_rfid1.close()
        self.__ser_rfid2.close()


