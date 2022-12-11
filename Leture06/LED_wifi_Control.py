# LED CONTROL FROM ANDROID
# Program: LED_Wifi.py
# Date: 2022-12-10
# Author: X.Tang
# Version: 1.0

from flask import Flask, render_template
import RPi.GPIO as GPIO

app = Flask(__name__)

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

# LED is on gpio 2, config gpio 2 as output

LED = 2
GPIO.setup(LED, GPIO.OUT)

#Turn OFF the LED to start with

GPIO.output(LED, 0)

@app.route("/<device>/<action>")
def action(device, action):
    actuator = LED
    if action == "on":
        GPIO.output(actuator, GPIO.HIGH)
    if action == "off":
        GPIO.output(actuator, GPIO.LOW)
    return ""

if __name__ == '__main__':
    app.run(debug=True, port=80, host='0.0.0.0',use_reloader=False)
