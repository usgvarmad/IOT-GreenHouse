#Code based on on http://rowboboat.com/bay2/2015/01/02/python-stepper-motor-driver-example/
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
 
#Setup the raspberry pi's GPIOs

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

 
#Set direction of rotation

#set the output to true for left and false for right
if direction == 'left':

    gpio.output(12, False)
elif direction == 'right':

    gpio.output(12, True)

# Enable all
gpio.output(14, True)
gpio.output(23, True)
gpio.output(8, False)
 
#Setup step counter and speed control variables
#track the number of steps taken
StepCounter = 0
 
#waittime controls speed
WaitTime = 0.008

gpio.output(24,False)
gpio.output(15,False)
 
# Start the program main loop
while StepCounter < steps:
 

    gpio.output(7, True)

    gpio.output(7, False)
    StepCounter += 1
 
    time.sleep(WaitTime)

#relase the GPIO
gpio.cleanup()