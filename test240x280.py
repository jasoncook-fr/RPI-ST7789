import ST7789
from PIL import Image
from time import sleep
'''
GPIO is all in the ST7789 init object

port=0 : RPi has 2 SPI ports. We are using port 0. SDA on the screen is attached to MOSI (GPIO 10)

cs=1   : CS on screen attached to SPI0 CE1 (GPIO 7)

rst=25 : reset on screen attached to GPIO 25

backlight=19 : Backlight on screen attached to GPIO 19
'''
display = ST7789.ST7789(
    width = 280,
    rotation=180,
    port=0,
    cs=1,
    rst=25,
    dc=9,
    backlight=19,
    spi_speed_hz=80*1000*1000,
    offset_left=20
)

display._spi.mode=3
display.reset()
display._init()
# Display a Color for 2 seconds
image=Image.new('RGB',(240,280),(0,0,225))  #('RGB',(240,240),(r,g,b))
display.display(image)
sleep(3)
image=Image.open("images/vio.jpg")
#image=image.resize((240,240),resample=Image.LANCZOS)
display.display(image)
