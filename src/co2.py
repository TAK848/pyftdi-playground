import time
from datetime import datetime

from pyftdi.serialext import serial_for_url

# D0: TX
# D1: RX

READ_COMMAND = bytearray([
    0xff, # start byte
    0x01, # reserved
    0x86, # command
    0x00,
    0x00,
    0x00,
    0x00,
    0x00,
    0x79, # checksum
])

def co2():
    ser = serial_for_url('ftdi://ftdi:232h/1')
    try:
        while True:
            # ser.write(b'Hello, World!\n')
            ser.write(READ_COMMAND)
            # time.sleep(0.1)
            response = ser.read(9)
            # print(response.hex())
            if len(response) == 9:
                if response[8] == get_check_sum(response):
                    # print(f"checksum: {response[8]}, {get_check_sum(response)}")
                    co2 = response[2] * 256 + response[3]
                    now = datetime.now()
                    print(f"{now.strftime('%Y-%m-%d %H:%M:%S.%f')}: CO2: {co2}ppm")
                else:
                    print("Checksum error")
            else:
                print("Invalid response length")
            # time.sleep(0.1)
    except KeyboardInterrupt:
        pass
    finally:
        ser.close()

def serial_test():
    ser = serial_for_url('ftdi://ftdi:232h/1')
    try:
        while True:
            ser.write(b'Hello, World!\n')
            # time.sleep(0.1)
    except KeyboardInterrupt:
        pass
    finally:
        ser.close()

def get_check_sum(data):
    checksum = 0xff - sum(data[1:8]) + 1
    return checksum & 0xff
