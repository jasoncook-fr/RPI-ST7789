#!/usr/bin/env python3
from PIL import Image
import ST7789
import time
import sys

# Screen used is 240x240

# Choose gif file to play. make sure it is pre-formated to be square
image_file = 'images/microbe.gif'

# Create ST7789 LCD display class.
disp = ST7789.ST7789(
    port=0,
    cs=1,
    rst=25,
    dc=9,
    backlight=19,
    spi_speed_hz=80 * 1000 * 1000,
)

disp._spi.mode=3
disp.reset()
disp._init()

width = 240
height = 240

# Load an image.
print('Loading gif: {}...'.format(image_file))
image = Image.open(image_file)

print('Drawing gif, press Ctrl+C to exit!')

frame = 0

while True:
    try:
        image.seek(frame)
        disp.display(image.resize((width, height)))
        frame += 1
        time.sleep(0.05)

    except EOFError:
        frame = 0
