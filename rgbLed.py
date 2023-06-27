import RPi.GPIO as GPIO
from time import sleep
GPIO.setmode(GPIO.BCM)

class RGBLed():
    def __init__(self, blue_pin, red_pin, green_pin):
        GPIO.setup(blue_pin, GPIO.OUT)
        GPIO.setup(red_pin, GPIO.OUT)
        GPIO.setup(green_pin, GPIO.OUT)
        self.blue = GPIO.PWM(blue_pin, 75)
        self.red = GPIO.PWM(red_pin, 75)
        self.green = GPIO.PWM(green_pin, 75)

    def blueLight(self,second=3,forever=False):
        if forever:
            try:
                while(True):
                    self.blue.start(75)
                    self.red.start(75)
            except:
                self.blue.stop()
                self.red.stop()
                #GPIO.cleanup()
        else:                  
            self.blue.start(75)
            self.red.start(75)
            sleep(second)
            self.blue.stop()
            self.red.stop()     

      
    def clean(self):
        GPIO.cleanup()