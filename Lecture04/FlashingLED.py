import RPi.GPIO as GPIO  #import GPIO library
import time

GPIO.setwarnings(False)
#GPIO.setmode(GPIO.BOARD)
GPIO.setmode(GPIO.BCM)
#GPIO.setup(3, GIPO.IN)
GPIO.setup(3, GPIO.OUT)

try:
    while True:
        GPIO.output(3, 1)    #turn on the LED
        time.sleep(1)
        GPIO.output(3, 0)    #turn off the LED
        time.sleep(1)
        
except KeyboardInterrupt:
    GPIO.cleanup()
