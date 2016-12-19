# Based on http://rowboboat.com/bay2/2015/01/02/python-stepper-motor-driver-example/
import sys
import RPi.GPIO as gpio #https://pypi.python.org/pypi/RPi.GPIO more info
import time

try: 
    direction = sys.argv[1]
    steps = int(float(sys.argv[2]))
except:
    steps = 0
 
#print which direction and how many steps 
print("You told me to turn %s %s steps.") % (direction, steps)

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

if direction == 'left':
    gpio.output(25, True)
    gpio.output(18, False)
    gpio.output(12, False)
elif direction == 'right':
    gpio.output(25, False)
    gpio.output(18, True)
    gpio.output(12, True)

# Enable all
gpio.output(14, False)
gpio.output(23, False)
gpio.output(8, False)
 

StepCounter = 0
WaitTime = 0.005

# Start the main program loop
while StepCounter < steps:
 
    #turning the gpio on and off tells the easy driver to take one step
    gpio.output(24, True)
    gpio.output(15, True)
    #gpio.output(7, True)
    gpio.output(24, False)
    gpio.output(15, False)
    #gpio.output(7, False)
    StepCounter += 1
 
    #Wait before taking the next step...this controls rotation speed
    time.sleep(WaitTime)
 
gpio.output(14,True)
gpio.output(23,True)
gpio.output(8,True) 

gpio.cleanup()