#Step 0: Preamble
#------------------------------------------------------------------------
#------------------------------------------------------------------------
#Program Title  : easy_stepper.py 
#Code Written by: Salty Scott
#Current Project: www.rowboboat.com
#This code is a very basic example of using python to control a spark fun
# easy driver.  The spark fun easy driver that I am using in this example
# is connected to a 42HS4013A4 stepper motor and my raspberry pi.  Pin 23
# is the direction control and pin 24 is the step control.  I am using
# these components in the www.rowboboat.com project version 2.0 and I
# hope someone finds this a useful and simple example.
# This program expects two arguments: direction and steps
# Example usage: sudo python easy_stepper.py left 1600
# The above example would turn a 200 step motor one full revolution as by
# default the easy driver 4.4 is in 1/8 microstep mode. However the stepper driver 
# selected by gtaagii will default to one full step per step pulse, microstepping can
# be selected if desired.
#------------------------------------------------------------------------
#------------------------------------------------------------------------
 
#Step 1: Import necessary libraries 
#------------------------------------------------------------------------
#------------------------------------------------------------------------
import sys
import RPi.GPIO as gpio #https://pypi.python.org/pypi/RPi.GPIO more info
import time
from picamera import PiCamera
from time import sleep


lengthSteps = 1000
rotationSteps = 400
WaitTime1 = 0.005
WaitTime2 = 0.008

def m1m2p1():
    steps = lengthSteps
    #set direction for Right 
    gpio.output(25, True)
    gpio.output(18, False)
    while steps > 0:
 
        #turning the gpio on and off tells the easy driver to take one step
        gpio.output(24, True)
        gpio.output(15, True)
        #gpio.output(7, True)
        gpio.output(24, False)
        gpio.output(15, False)
        #gpio.output(7, False)
        steps -= 1
 
        #Wait before taking the next step...this controls rotation speed
        time.sleep(WaitTime1)
    
def m1m2p2():
    steps = lengthSteps
    #set direction for Right 
    gpio.output(25, False)
    gpio.output(18, True)
    while steps > 0:
 
        #turning the gpio on and off tells the easy driver to take one step
        gpio.output(24, True)
        gpio.output(15, True)
        #gpio.output(7, True)
        gpio.output(24, False)
        gpio.output(15, False)
        #gpio.output(7, False)
        steps -= 1
 
        #Wait before taking the next step...this controls rotation speed
        time.sleep(WaitTime1)
    
def m3pos1():
    steps = rotationSteps
    #turn clockwise
    gpio
    gpio.output(12, True)
    while steps > 0:
 
        #turning the gpio on and off tells the easy driver to take one step
        #gpio.output(24, True)
        #gpio.output(15, True)
        gpio.output(7, True)
        #gpio.output(24, False)
        #gpio.output(15, False)
        gpio.output(7, False)
        steps -= 1
 
        #Wait before taking the next step...this controls rotation speed
        time.sleep(WaitTime2)
    
def m3pos2():
    steps = rotationSteps
    #turn counter clockwise
    gpio.output(12, False)
    while steps > 0:
 
        #turning the gpio on and off tells the easy driver to take one step
        #gpio.output(24, True)
        #gpio.output(15, True)
        gpio.output(7, True)
        #gpio.output(24, False)
        #gpio.output(15, False)
        gpio.output(7, False)
        steps -= 1
 
        #Wait before taking the next step...this controls rotation speed
        time.sleep(WaitTime2)

def setupPins():
    
    #use the broadcom layout for the gpio
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

    gpio.output(14, False)
    gpio.output(23, False)
    gpio.output(8, False)

setupPins()
camera = PiCamera()
camera.resolution = (640, 480)
#capture image 1
sleep(1)
camera.capture('plot1.jpg')

m3pos2()
#capture image 2
sleep(1)
camera.capture('plot2.jpg')

m1m2p2()
gpio.cleanup()
setupPins()
#capture image 3
sleep(1)
camera.capture('plot3.jpg')

m3pos1()
#capture image 4
sleep(1)
camera.capture('plot4.jpg')

m1m2p1() # go home
 
#Step 7: Clear the GPIOs so that some other program might enjoy them
#------------------------------------------------------------------------
#------------------------------------------------------------------------
#relase the GPIO
gpio.cleanup()
#------------------------------------------------------------------------
#------------------------------------------------------------------------