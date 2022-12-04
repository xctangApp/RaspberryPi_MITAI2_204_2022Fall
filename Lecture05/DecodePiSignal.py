#
#
#  decode Pi signal/data
#
#

try:
    while True:
        data = client.recv(1024)           # Receive data bytes
        if data.decode('utf-8') == '1':    # 1 received
            GPIO.output(LED, 1)            # LED ON
        elif data.decode('utf-8') == '0':  # 0 received
            GPIO.output(LED, 0)            # LED OFF
            
except KeyboardInterrupt:
    client.close()
    s.close()
