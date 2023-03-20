# Circuitpython sample

from board import GP10, GP11, GP16, GP17, GP18
from busio import SPI
from displayio import release_displays, Group, FourWire, Bitmap, Palette, TileGrid
from terminalio import FONT

from adafruit_display_text import label
from adafruit_st7735r import ST7735R

# Hardware:
#  Raspberry Pico H: https://www.amazon.com/gp/product/B09HC9X24J
#  1.8" ST7735R SPI 128x160 TFT LCD with PCB: https://www.amazon.com/dp/B00LSG51MM
# Using CircuitPython:
#  UF2 available at: https://circuitpython.org/board/raspberry_pi_pico/
#  Extra libraries from here: https://circuitpython.org/libraries
#  Copy these into CIRCUITPYTHON/lib: adafruit_st7735r.mpy, adafruit_display_text
# Screen Wiring:
# +-----------------+-------------+-------------------+----------------------------------------+
# | Screen Terminal | Pico Pin ID | Pico Pin # (1-40) | Notes                                  |
# +-----------------+-------------+-------------------+----------------------------------------+
# | LED-            | -           | -                 |                                        |
# +-----------------+-------------+-------------------+----------------------------------------+
# | LED+            | 3V3 (OUT)   | 36                |                                        |
# +-----------------+-------------+-------------------+----------------------------------------+
# | SD_CS           |  -          | -                 |                                        |
# +-----------------+-------------+-------------------+----------------------------------------+
# | MOSI            | -           | -                 |                                        |
# +-----------------+-------------+-------------------+----------------------------------------+
# | MISO            | -           | -                 |                                        |
# +-----------------+-------------+-------------------+----------------------------------------+
# | SCK             | -           | -                 | This is the clock for the SD card slot |
# +-----------------+-------------+-------------------+----------------------------------------+
# | CS              | GP18        | 24                |                                        |
# +-----------------+-------------+-------------------+----------------------------------------+
# | SCL             | GP10        | 14                |                                        |
# +-----------------+-------------+-------------------+----------------------------------------+
# | SDA             | GP11        | 15                |                                        |
# +-----------------+-------------+-------------------+----------------------------------------+
# | A0              | GP16        | 21                |                                        |
# +-----------------+-------------+-------------------+----------------------------------------+
# | RESET           | GP17        | 22                |                                        |
# +-----------------+-------------+-------------------+----------------------------------------+
# | NC              | -           | -                 |                                        |
# +-----------------+-------------+-------------------+----------------------------------------+
# | NC              | -           | -                 |                                        |
# +-----------------+-------------+-------------------+----------------------------------------+
# | NC              | -           | -                 |                                        |
# +-----------------+-------------+-------------------+----------------------------------------+
# | VCC             | VBUS        | 40                |                                        |
# +-----------------+-------------+-------------------+----------------------------------------+
# | GND             | GND         | 38                |                                        |
# +-----------------+-------------+-------------------+----------------------------------------+


mosi_pin = GP11
clk_pin = GP10
reset_pin = GP17
cs_pin = GP18
dc_pin = GP16

release_displays()

spi = SPI(clock=clk_pin, MOSI=mosi_pin)
display_bus = FourWire(spi, command=dc_pin, chip_select=cs_pin, reset=reset_pin)
display = ST7735R(display_bus, width=128, height=160, bgr = True)

splash = Group()
display.show(splash)

color_bitmap = Bitmap(128, 160, 1)

color_palette = Palette(1)
color_palette[0] = 0x00FF00  # Bright Green

bg_sprite = TileGrid(color_bitmap, pixel_shader=color_palette, x=0, y=0)
splash.append(bg_sprite)

# Draw a smaller inner rectangle
inner_bitmap = Bitmap(118, 150, 1)
inner_palette = Palette(1)
inner_palette[0] = 0x000000  # Black
inner_sprite = TileGrid(inner_bitmap, pixel_shader=inner_palette, x=5, y=5)
splash.append(inner_sprite)

# Draw a label
text_group = Group(scale=1, x=11, y=24)
text = "Hello World!\n\nThis is a sample\ntext!\n\nEverything is \nworking fine."
text_area = label.Label(FONT, text=text, color=0xFFFFFF)
text_group.append(text_area)  # Subgroup for text scaling
splash.append(text_group)

while True:
    pass
