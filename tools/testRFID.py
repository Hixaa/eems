import serial

rfid1 = serial.Serial('/dev/ttyUSB0', 115200, parity = serial.PARITY_NONE, timeout = 0.01)
rfid1.write(serial.to_bytes([0xAA, 0x02, 0x10, 0x00, 0x02, 0x01, 0x01, 0x71, 0xAD])) # type: ignore
rfid1.flush()
rfid2 = serial.Serial('/dev/ttyUSB1', 115200, parity = serial.PARITY_NONE, timeout = 0.01)
rfid2.write(serial.to_bytes([0xAA, 0x02, 0x10, 0x00, 0x02, 0x01, 0x01, 0x71, 0xAD])) # type: ignore
rfid2.flush()
print("[*] RFID Test Started...")

while True:
    data = rfid1.readline()
    if(data.decode(errors='ignore').strip() != ''):
        print("[+] ", "RFID_1: ", data.decode(errors='ignore').strip()[0:]," : ")
    # rfid_1 = rfid1.readline()
    # print("[+] ", rfid_1.strip())
    data = rfid2.readline()
    if(data.decode(errors = 'ignore').strip() != ''):
        print("[+] ", "RFID_2: ", data.decode(errors='ignore').strip()[0:]," : ")
