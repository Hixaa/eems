import serial

ser = serial.Serial("/dev/ttyUSB0", 115200,parity = serial.PARITY_NONE, timeout = 0.01)
# ser.write(bytearray(b'AA 02 10 00 02 01 01 71 AD'))
ser.write(serial.to_bytes([0xAA, 0x02, 0x10, 0x00, 0x02, 0x01, 0x01, 0x71, 0xAD])) # type: ignore


while True:
    data = ser.readline()
    # data = str(data)
    # print(type(data))
    # print(data[2:-5])
    print(data.decode(errors='ignore'))