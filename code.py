"""
Author: Corey Walcott
Date: 4/17/2024

Title: Final Project
Description:
Project door checker logic, included temperature and light sensor for checking proper UART message format
added adafruit_hcsr04 import includes use of ultrasonic sensor.

"""
import time
import gc
import microcontroller
import adafruit_lis3dh
import adafruit_hashlib as hashlib
import adafruit_ble_broadcastnet
import adafruit_thermistor
import board
import analogio
import adafruit_hcsr04


from adafruit_ble import BLERadio
from adafruit_ble.advertising.standard import ProvideServicesAdvertisement
from adafruit_ble.services.nordic import UARTService
from adafruit_circuitplayground import cp


#ultrasonic sensor initialization
ultrasonic_sensor = adafruit_hcsr04.HCSR04(trigger_pin=board.A4, echo_pin=board.A5)

# Create Bluetooth objects
ble = BLERadio()
uart = UARTService()
advertisement = ProvideServicesAdvertisement(uart)
ble.name = "Walcott-BlueFruit"

print("This is BroadcastNet sensor:", adafruit_ble_broadcastnet.device_address)

# Advertise and wait for connection
ble.start_advertising(advertisement)
print("Waiting to connect")
while not ble.connected:
    pass
print("Connected")

# Create an MD5 message
print("--MD5--")
byte_string = b"password"
m = hashlib.md5()
# Update the hash object with byte_string
m.update(byte_string)
# Obtain the digest, digest size, and block size
print(
    "Msg Digest: {}\nMsg Digest Size: {}\nMsg Block Size: {}".format(
        m.hexdigest(), m.digest_size, m.block_size
    )
)
#temperature initialization.
temperatureMeasure = cp.temperature * 9 / 5 + 32

# Forever loop
while True:

    try:
        distance = ultrasonic_sensor.distance
    except RuntimeError:
        print("hol up, trying big dog")

    if not cp.switch:
        # If the switch is to the right, it returns False!
        print("Slide switch off!")
        continue

    # only do things with bluetooth if connected
    if ble.connected:
        line = uart.readline()  # receive data from UART
        line = line.strip()

        if line:
            print(line)

            m2 = hashlib.md5() #apply m2 object as a new hash object
            m2.update(line)     #apply passed line from UART to hash object
            if(m.hexdigest() ==  m2.hexdigest()): #hexdigest checker
                print("connection successful")
                uart.write("DISTANCE = {0}\n:".format(distance))
                uart.write("Light = \{0}\n".format(cp.light))
                uart.write("TEMP = {0}:".format(temperatureMeasure))

                """could use logic to check
                    if(distance > 30)
                        uart.write("door open")
                        break
                    else
                        uart.write("door closed")

                """

            else:
                print("invalid")   #otherwise, print invalid.


    m.hexdigest()



    gc.collect()
    time.sleep(0.1)
