#!/usr/bin/python3

import RPi.GPIO as GPIO
from time import sleep  
GPIO.setmode(GPIO.BCM) 

GPIO.setup(17, GPIO.OUT)# set GPIO 17 as output for blue led  
GPIO.setup(27, GPIO.OUT)# set GPIO 27 as output for red led  
GPIO.setup(22, GPIO.OUT)# set GPIO 22 as output for green led
blue = GPIO.PWM(17, 70)
red = GPIO.PWM(27, 70)
green = GPIO.PWM(22, 70)
i = 0
try:
    while(True): 
        if(i<70):
            i += 1 
        else:
            i = 0 
        green.start(i)
        sleep(0.8)
        green.stop()
        
        red.start(i)
        sleep(0.8)
        red.stop()
        
        blue.start(i)    
        sleep(0.8)
        blue.stop()

        green.start(i)
        red.start(i)
        sleep(0.8)
        green.stop()
        red.stop()

        red.start(i)
        green.start(i)
        sleep(0.8)
        red.stop()
        green.stop()

        blue.start(i)
        red.start(i)
        sleep(0.8)
        blue.stop()
        red.stop()

        blue.start(i)
        green.start(i)
        sleep(0.8)
        blue.stop()
        green.stop()

        blue.start(i)
        red.start(i)
        green.start(i)
        sleep(0.8)
        blue.stop()
        red.stop()
        green.start(i)

        red.start(i)
        blue.start(i)
        green.start(i)
        sleep(0.8)
        red.stop()
        blue.stop()
        green.start(i)

        green.start(i)
        red.start(i)
        blue.start(i)
        sleep(0.8)
        green.stop()
        red.stop()
        blue.start(i)
except KeyboardInterrupt:
    green.stop()
    red.stop()
    blue.stop() 
    GPIO.cleanup() 