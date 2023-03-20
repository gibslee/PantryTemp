# Micropython sample

from json import dumps
from time import sleep

from machine import Pin
from usocket import socket, getaddrinfo
from network import WLAN, STA_IF

try:
    from wifi_secrets import wifi_name, wifi_pw  # need to keep wifi_secrets.py next to the file
except ImportError:
    wifi_name = "Wifi-Network-Name"
    wifi_pw = "Wifi-Password"

# Hardware:
#  Raspberry Pico W: https://www.amazon.com/Pico-Raspberry-Pre-Soldered-Dual-core-Processor/dp/B0BK9W4H2Q
# Using Wifi-enabled Micropython:
#  UF2 available at: https://micropython.org/download/rp2-pico/
# Wiring:
#  Power-on LED from positive on pin 16 to a ground pin
#  Wifi-connected LED from positive on pin 15 to a ground pin

boot_led = Pin(16, Pin.OUT)
boot_led.value(0)
boot_led.value(1)

connect_led = Pin(15, Pin.OUT)
connect_led.value(0)
ap = WLAN(STA_IF)
ap.active(False)
ap.active(True)
ap.connect(wifi_name, wifi_pw)
sleep(1)  # wait for it to connect
while not ap.isconnected():
    pass  # could do better here
connect_led.value(1)


def api():
    return dumps({'kay': 'value', 'foo': 'bar'})


addr = getaddrinfo('0.0.0.0', 80)[0][-1]
s = socket()
s.bind(addr)
s.listen(1)
print('listening on', addr)

# Listen for connections
while True:
    try:
        cl, addr = s.accept()
        print('client connected from', addr)
        request = cl.recv(1024)
        print(request)
        response = api()
        cl.send('HTTP/1.0 200 OK\r\nContent-Type: application/json; charset=UTF-8\r\n\r\n' + response + '\r\n')
        cl.close()
    except OSError as e:
        cl.close()
        print('connection closed')
