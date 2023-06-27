#!/usr/bin/python3
import rgbLed
from time import sleep
import RPi.GPIO as GPIO

if __name__ == '__main__':
    rgb = rgbLed.RGBLed(17,27,22)
    rgb.blueLight()
    rgb.clean()
    
    