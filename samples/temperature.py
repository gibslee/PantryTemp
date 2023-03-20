# Micropython sample

from time import sleep

from onewire import OneWire
from dx18x20 import DS18X20
from machine import Pin

# Hardware:
#  Raspberry Pico H: https://www.amazon.com/gp/product/B09HC9X24J/ref=ppx_yo_dt_b_search_asin_title?ie=UTF8&psc=1
#  DS18B20 Temperature Sensor: https://www.amazon.com/dp/B09NVFJYPS?psc=1&ref=ppx_yo2ov_dt_b_product_details
# Using Micropython:
#  UF2 available at: https://micropython.org/download/rp2-pico/
# Wiring:
#  Power-on LED from positive on pin 16 to a ground pin
#  Freezer temperature sensor running between pin 26 and ground
#  Fridge temperature sensor running between pin 27 and ground

boot_led = Pin(16, Pin.OUT)
boot_led.value(0)
boot_led.value(1)

freezer_pin = Pin(26, Pin.IN)
freezer_sensor = DS18X20(OneWire(freezer_pin))

fridge_pin = Pin(27, Pin.IN)
fridge_sensor = DS18X20(OneWire(fridge_pin))

freezer_roms = freezer_sensor.scan()
freezer_sensor.convert_temp()
fridge_roms = fridge_sensor.scan()
fridge_sensor.convert_temp()
sleep(1)  # docs say you have to wait 750ms before calling read_temp()
freezer_temp = freezer_sensor.read_temp(freezer_roms[0])
fridge_temp = fridge_sensor.read_temp(fridge_roms[0])

print(f"{fridge_temp=}; {freezer_temp=}")
