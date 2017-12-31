"""Dealing with LED control directly"""

from __future__ import division, absolute_import, print_function

from enum import Enum
from itertools import repeat
import os
import time

if os.getenv('RESIN'):
    from dotstar import Adafruit_DotStar
else:
    from DotStar_Emulator import Adafruit_DotStar

from mindorb import scenes
from mindorb.scenetypes import LedColor


class SpiDevice(Enum):
    primary = "/dev/spidev0.0"
    secondary = "/dev/spidev0.1"


class LedBuffer(object):
    def __init__(self, num_pixels, brightness=0.25):
        # Initialize the buffer to all-black by default
        self.leds = list(repeat(LedColor.black.value, num_pixels))
        self.brightness = brightness

    def set_all(self, color):
        if isinstance(color, LedColor):
            color = color.value

        for idx, _ in enumerate(self.leds):
            self.leds[idx] = color


class LedManager(object):
    def __init__(
        self, num_pixels,
        default_scene=scenes.SolidBlack,
        spi_dev=SpiDevice.primary, spi_freq=12000000, led_order='bgr'
    ):
        self.num_pixels = num_pixels
        self.ledbuffer = LedBuffer(num_pixels)
        self.scene = None
        self.set_scene(default_scene, 0)

        if os.getenv('RESIN'):
            self._dotstar_strip = Adafruit_DotStar(
                num_pixels, spi_freq, order=led_order
            )
        else:
            # Unfortunately: the emulator doesn't support the `order` kwarg...
            self._dotstar_strip = Adafruit_DotStar(num_pixels)

        self._dotstar_strip.begin()

    def set_scene(self, new_scene, fadetime):
        if self.scene.__class__ is new_scene.__class__:
            # Make this a no-op if the scene has not changed
            print("Ignoring scene change: old={}, new={}".format(
                self.scene, new_scene
            ))
            return

        print("Changing scene: old={}, new={}, fadetime={}".format(
            self.scene, new_scene, fadetime))
        self.scene = new_scene(self.ledbuffer, fadetime)

    def run(self):
        while True:
            frame_timestamp = 0  # TODO: make this real
            self.scene.loop(frame_timestamp)

            self._dotstar_strip.setBrightness(
                int(255 * self.ledbuffer.brightness)
            )

            for idx in xrange(self.num_pixels):
                color = self.ledbuffer.leds[idx]
                self._dotstar_strip.setPixelColor(
                    idx,
                    color[0] << (2 * 8) |
                    color[1] << (1 * 8) |
                    color[2] << (0 * 8)
                )

            self._dotstar_strip.show()

            time.sleep(1.0 / 50)
