# Circuitpython sample

from board import GP1, GP2, GP3, GP4
from busio import SPI
from digitalio import DigitalInOut
from storage import VfsFat, mount

from adafruit_sdcard import SDCard

# Hardware:
#  Raspberry Pico H: https://www.amazon.com/gp/product/B09HC9X24J
#  1.8" ST7735R SPI 128x160 TFT LCD with PCB: https://www.amazon.com/dp/B00LSG51MM
# Using CircuitPython:
#  UF2 available at: https://circuitpython.org/board/raspberry_pi_pico/
#  Extra libraries from here: https://circuitpython.org/libraries
#  Copy these into CIRCUITPYTHON/lib: adafruit_sdcard.mpy
# Screen Wiring:
# +-------------------+----------------+-------------------+----------------------------------------+
# | Breakout Terminal | Pico Pin ID    | Pico Pin # (1-40) | Notes                                  |
# +-------------------+----------------+-------------------+----------------------------------------+
# | SD_CS             | GP1 (SPIO CSn) | 2                 |                                        |
# +-------------------+----------------+-------------------+----------------------------------------+
# | SCK               | GP2 (SPIO SCK) | 4                 |                                        |
# +-------------------+----------------+-------------------+----------------------------------------+
# | MOSI              | GP3 (SPIO TX)  | 5                 |                                        |
# +-------------------+----------------+-------------------+----------------------------------------+
# | MISO              | GP4 (SPIO RX)  | 6                 |                                        |
# +-------------------+----------------+-------------------+----------------------------------------+

sck_pin = GP2
mosi_pin = GP3
miso_pin = GP4
spi_sd = SPI(sck_pin, mosi_pin, miso_pin)
cs = DigitalInOut(GP1)
sd = SDCard(spi_sd, cs)
vfs = VfsFat(sd)
mount(vfs, '/sd')
with open('/sd/grassy.bmp') as f:
    pass

# From this point on, you can access files on the drive in the same manner as usual, /sd/*
