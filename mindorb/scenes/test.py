"""Various testing scenes"""

from __future__ import division, absolute_import, print_function

import random

from mindorb.scenetypes import EMOTION_COLORS, SceneBase


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


class TestMemoryRackRandom(SceneBase):
    CHANGE_PERIOD = 1

    def __init__(self, ledbuffer, fadetime):
        super(TestMemoryRackRandom, self).__init__(ledbuffer, fadetime)
        self._orbs = self._ledbuffer.mapping.shelf_section_orb_map
        self._last_change = 0
        # from IPython import embed; embed()

    def loop(self, frame_timestamp):
        if frame_timestamp - self._last_change > self.CHANGE_PERIOD:
            for shelf in self._orbs:
                for section in shelf:
                    for orb in section:
                        orb.set_color(random.choice(tuple(EMOTION_COLORS)))

            self._last_change = frame_timestamp
