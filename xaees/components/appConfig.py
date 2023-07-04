import configparser
import os
from pathlib import Path

class Config:

    def __init__(self):
        self.__rootFolder = os.getcwd()
        #print(self.__rootFolder)
        self.__configPath = self.__rootFolder+'/config_xaees.ini'
        self.__devices = os.listdir("/dev/")
        self.__USB = filter(lambda dev: dev[0:6] == 'ttyUSB', self.__devices)
        self.__USB = list(self.__USB)
        try:
            if (len(self.__USB) == 0):
                raise "DeviceIssue: Check /dev/ttyUSB*"
            else:
                parser = configparser.ConfigParser()
                parser.read(self.__configPath)
                parser.set('RFID_1', 'port', self.__USB[0])
                parser.set('RFID_2', 'port', self.__USB[1])        
        except Exception as e:
            print("[!] Unable to Detect RFID: ", e)
        # print("[*] Config Path: ", self.__configPath)
        
    def rfid1Port(self):
        parser = configparser.ConfigParser()
        parser.read(self.__configPath)
        return parser.get('RFID_1','port')

    def rfid1BaudRate(self):
        parser = configparser.ConfigParser()
        parser.read(self.__configPath)
        return int(parser.get('RFID_1','baudRate'))

    def rfid1TimeOut(self):
        parser = configparser.ConfigParser()
        parser.read(self.__configPath)
        return float(parser.get('RFID_1','timeout'))

    def rfid2Port(self):
        parser = configparser.ConfigParser()
        parser.read(self.__configPath)
        return parser.get('RFID_2','port')

    def rfid2BaudRate(self):
        parser = configparser.ConfigParser()
        parser.read(self.__configPath)
        return int(parser.get('RFID_2','baudRate'))

    def rfid2TimeOut(self):
        parser = configparser.ConfigParser()
        parser.read(self.__configPath)
        return float(parser.get('RFID_2','timeout'))

    def url(self):
        parser = configparser.ConfigParser()
        parser.read(self.__configPath)
        return parser.get('URL','url')

    def maxjsonLimit(self):
        parser = configparser.ConfigParser()
        parser.read(self.__configPath)
        return int(parser.get('JSONStorage','max_limit'))

    def gateNo(self):
        parser = configparser.ConfigParser()
        parser.read(self.__configPath)
        return int(parser.get('Gate','gate'))
    
    def companyId(self):
        parser = configparser.ConfigParser()
        parser.read(self.__configPath)
        return int(parser.get('Company_ID', 'id'))
