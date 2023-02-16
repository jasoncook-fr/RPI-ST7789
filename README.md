# RGB TFT Screen ST7789 & Rapsberry Pi

**Running Headless Raspberry Pi OS (Lite) on a Raspberry Pi 3 Model B+**
<br />
**Primary screen used is 1.3" SPI Colour Square LCD (240x240) Breakout bought on Aliexpress**
<br />
<br />
For RPi image preparations, see the following link [RPi OS bullsye setup](https://www.raspberrypi.com/news/raspberry-pi-bullseye-update-april-2022/)
<br />
<br />
In raspi-config -> 3) Interface Options -> SPI -> choose **YES** <br />

## Install Dependencies:

```shell
sudo apt-get update
sudo apt-get install python3-rpi.gpio python3-spidev python3-pip python3-pil python3-numpy
```
3 test codes are included. **test240x240.py** and **test240x280.py** illustrate showing a jpeg image on different sized screens. **testGif.py** illustrates using an animated gif on a 240x240 screen. <br /> 
<br />
***FIRST TEST
Use the code **test240x240.py** . <br />
Be sure that your test images (ex. 'cat.jpg') are in the **images** folder, located in the same folder as the code. <br />
Launch the code as such:

```shell
python testImage.py
```

| Screen Pins   | RPI GPIO | RPI Pin Function |
| ------------- | -------- | ---------------- |
| GND           | GND      |                  |
| VCC (or VDD)  | 3.3V     |                  |
| SCK           | 11       | SPI0 SCLK        |
| SDA (or MOSI) | 10       | SPI0 MOSI        |
| RESET         | 25       |                  |
| DC            | 9        | SPI0 MISO        |
| CS            | 7        | SPI0 CE1         |

### References: 
- [Techtronic : Getting Started with RPI and ST7789](https://techatronic.com/st7789-raspberry-pi/) : Pulled test code here and modified it
- [Pimoroni st7789-python on github](https://github.com/pimoroni/st7789-python) : Took notes from their examples, notably the GIF.py example. The examples assume you are using their Garden Board Breakout thing. I don't have this. 
