"""Various testing scenes"""

from __future__ import division, absolute_import, print_function

from mindorb.scenetypes import SceneBase


class TestStripChase(SceneBase):
    def __init__(self, ledbuffer, fadetime):
        super(TestStripChase, self).__init__(ledbuffer, fadetime)
        self.numpixels = len(self._ledbuffer.leds)

        self.head = 0  # Index of first 'on' pixel
        self.tail = -10  # Index of last 'off' pixel
        self.color = 0xFF0000  # 'On' color (starts red)

    def loop(self, frame_timestamp):
        # This test pattern adapted from:
        # https://github.com/adafruit/Adafruit_DotStar_Pi/blob/master/strandtest.py
        self._ledbuffer.leds[self.head] = (
            self.color >> 16 & 0xFF,
            self.color >> 8 & 0xFF,
            self.color & 0xFF)
        self._ledbuffer.leds[self.tail] = (0, 0, 0)

        self.head += 1  # Advance head position
        if(self.head >= self.numpixels):  # Off end of strip?
            self.head = 0  # Reset to start
            self.color >>= 8  # Red->green->blue->black
            if(self.color == 0):
                self.color = 0xFF0000  # If black, reset to red

        self.tail += 1  # Advance tail position
        if(self.tail >= self.numpixels):
            self.tail = 0  # Off end? Reset
