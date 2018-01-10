"""Various testing scenes"""

from __future__ import division, absolute_import, print_function

import colorsys
import random

from mindorb.scenetypes import DUAL_COLOR_WITH_SOLIDS, LedColor, SceneBase


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

        self._ledbuffer.set_all(LedColor.black)

    def loop(self, frame_timestamp):
        if frame_timestamp - self._last_change > self.CHANGE_PERIOD:
            for shelf in self._orbs:
                for section in shelf:
                    for orb in section:
                        orb.set_colors(*random.choice(tuple(
                            DUAL_COLOR_WITH_SOLIDS)))

            self._last_change = frame_timestamp


class TestHueFade(SceneBase):
    HUE_PERIOD_S = 10

    def __init__(self, ledbuffer, fadetime):
        super(TestHueFade, self).__init__(ledbuffer, fadetime)
        self._base_ts = 0

    def loop(self, frame_timestamp):
        ts_diff = frame_timestamp - self._base_ts
        if ts_diff > self.HUE_PERIOD_S:
            self._base_ts = frame_timestamp

        rgb = colorsys.hsv_to_rgb(ts_diff / self.HUE_PERIOD_S, 1, 255)
        self._ledbuffer.set_all(rgb)
