# LED CONTROL FROM ANDROID
# Program: LEDBluetooth_Control.py
# Date: 2022-12-03
# Author: X.Tang
# Version: 1.0

import socket
import RPi.GPIO as GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

# LED is on gpio 2, config gpio 2 as output

LED = 2
GPIO.setup(LED, GPIO.OUT)

#Turn OFF the LED to start with

GPIO.output(LED, 0)

#Read the commands from Android device, decode, and control the LED

Port = 1
MAC = 'change to your own RaspberryPi address'    #check in terminal with code : hciconfig | grep "BD Address"
s=socket.socket(socket.AF_BLUETOOTH,socket.SOCK_STREAM,socket.BTPROTO_RFCOMM)
s.bind((MAC, Port))
s.listen(1)
client, addr = s.accept()

try:
    while True:
        data = client.recv(1024)        ## Receive data bytes
        if data.decode('utf-8') == "1":
            GPIO.output(LED,1)
        elif data.decode('utf-8') == "0":
            GPIO.output(LED,0)

except KeyboardInterrupt:
    Client.close()
    s.close()
