import RPi.GPIO as GPIO
from time import sleep
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

sysReady = 20
rfidStat = 26
dataUploadStat = 16

class statusLED:
    def __init__(self):
        GPIO.setup(sysReady,GPIO.OUT)
        GPIO.setup(rfidStat,GPIO.OUT)
        GPIO.setup(dataUploadStat,GPIO.OUT)
        GPIO.output(sysReady,False)
        GPIO.output(rfidStat,False)
        GPIO.output(dataUploadStat,False)

    def sysReady_Show(self,stat):
        GPIO.output(sysReady,stat)

    def rfidStat_Show(self):
        for i in [0,2]:
            GPIO.output(rfidStat,True)
            sleep(0.05)
            GPIO.output(rfidStat,False)
            sleep(0.05)
    
    def dataUploadStat_Show(self):
        for i in [0,3]:
            GPIO.output(dataUploadStat,True)
            sleep(0.05)
            GPIO.output(dataUploadStat,False)
            sleep(0.05)

    def Error_Show(self):
        for i in [0,3]:
            GPIO.output(sysReady,True)
            GPIO.output(rfidStat,True)
            GPIO.output(dataUploadStat,True)
            sleep(0.05)
            GPIO.output(sysReady,False)
            GPIO.output(rfidStat,False)
            GPIO.output(dataUploadStat,False)
            sleep(0.05)
    
    def close(self):
        GPIO.output(sysReady,False)
        GPIO.output(rfidStat,False)       
        GPIO.output(dataUploadStat,False)
        GPIO.cleanup()
        

