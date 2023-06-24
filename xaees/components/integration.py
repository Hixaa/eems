## DELETE THIS FILE

from cloudService import CloudService
# from rfid_simulator import rfid
from time import sleep

cloud = CloudService()

# data = rfid()
while True:
    sleep(0.25)
    cloud.autoSync()