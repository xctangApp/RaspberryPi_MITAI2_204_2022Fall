#This code is running in Mu 1.0.2
#204 LED Control Program
#Date: 2022-11-09
#Owner: X.Tang
#Version: 1.0

from gpiozero import LED
from time import sleep

led = LED(2)

while True:
    led.on()
    sleep(1)
    led.off()
    sleep(1)
