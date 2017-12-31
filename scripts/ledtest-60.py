#!/usr/bin/env python

# Simple strand test for Adafruit Dot Star RGB LED strip.
# This is a basic diagnostic tool, NOT a graphics demo...helps confirm
# correct wiring and tests each pixel's ability to display red, green
# and blue and to forward data down the line.  By limiting the number
# and color of LEDs, it's reasonably safe to power a couple meters off
# USB.  DON'T try that with other code!

import itertools
import os
import time

if os.getenv('RESIN'):
    from dotstar import Adafruit_DotStar
else:
    from DotStar_Emulator import Adafruit_DotStar

numpixels = 60  # Number of LEDs in strip

# Here's how to control the strip from any two GPIO pins:
# datapin  = 23
# clockpin = 24
# strip    = Adafruit_DotStar(numpixels, datapin, clockpin)
if os.getenv('RESIN'):
    strip = Adafruit_DotStar(numpixels, 12000000, order='bgr')
else:
    # Unfortunately: the emulator doesn't support the `order` kwarg...
    strip = Adafruit_DotStar(numpixels)

# Alternate ways of declaring strip:
#  Adafruit_DotStar(npix, dat, clk, 1000000) # Bitbang @ ~1 MHz
#  Adafruit_DotStar(npix)                    # Use SPI (pins 10=MOSI, 11=SCLK)
#  Adafruit_DotStar(npix, 32000000)          # SPI @ ~32 MHz
#  Adafruit_DotStar()                        # SPI, No pixel buffer
#  Adafruit_DotStar(32000000)                # 32 MHz SPI, no pixel buf
# See image-pov.py for explanation of no-pixel-buffer use.
# Append "order='gbr'" to declaration for proper colors w/older DotStar strips)


def set_brightness(value):
    # Adafruit lib takes brightness [0, 255] where 0 -> full
    # Scale to [0, 255]
    lib_val = int(255 * value)
    # Scale to [1, 256]
    lib_val += 1
    # Convert 256 (full brightness) -> 0
    if lib_val == 256:
        lib_val = 0

    strip.setBrightness(lib_val)


brightness_iter = itertools.cycle((0.1, 0.25, 0.5, 0.75, 1.0))

strip.begin()           # Initialize pins for output
set_brightness(next(brightness_iter))

# Runs 10 LEDs at a time along strip, cycling through red, green and blue.
# This requires about 200 mA for all the 'on' pixels + 1 mA per 'off' pixel.

head = 0               # Index of first 'on' pixel
tail = -10             # Index of last 'off' pixel
color = 0xFF0000        # 'On' color (starts red)

while True:                              # Loop forever

    strip.setPixelColor(head, color)  # Turn on 'head' pixel
    strip.setPixelColor(tail, 0)     # Turn off 'tail'
    strip.show()                     # Refresh strip
    time.sleep(1.0 / 50)             # Pause 20 milliseconds (~50 fps)

    head += 1                        # Advance head position
    if(head >= numpixels):           # Off end of strip?
        head = 0              # Reset to start
        color >>= 8              # Red->green->blue->black
        if(color == 0):
            color = 0xFF0000  # If black, reset to red
            set_brightness(next(brightness_iter))

    tail += 1                        # Advance tail position
    if(tail >= numpixels):
        tail = 0  # Off end? Reset
