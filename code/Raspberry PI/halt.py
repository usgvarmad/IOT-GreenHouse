# This script is used to stop the motors from moving

import sys
import RPi.GPIO as gpio #https://pypi.python.org/pypi/RPi.GPIO more info
import time

gpio.setmode(gpio.BCM)

gpio.setup(14, gpio.OUT) #E1
gpio.setup(15, gpio.OUT) #S1
gpio.setup(18, gpio.OUT) #D1
gpio.setup(23, gpio.OUT) #E2
gpio.setup(24, gpio.OUT) #S2
gpio.setup(25, gpio.OUT) #D2
gpio.setup(8, gpio.OUT)  #E3
gpio.setup(7, gpio.OUT)  #S3
gpio.setup(12, gpio.OUT) #D3

gpio.output(25, True)
gpio.output(18, True)
gpio.output(12, True)

# disable all
gpio.output(14, True)
gpio.output(23, True)
gpio.output(8, True)

gpio.output(24,False)
gpio.output(15,False)
gpio.output(7, False) 

while True: #Loop forever
    time.sleep(1)


gpio.cleanup()
