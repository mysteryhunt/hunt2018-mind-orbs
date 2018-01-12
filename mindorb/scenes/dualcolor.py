"""Dual color Hero Orbs"""

from __future__ import division, absolute_import, print_function

from mindorb.effects import breathe
from mindorb.scenetypes import LedColor
from mindorb.scenetypes import SceneBase


class HeroOrbDualColor(SceneBase):
    def __init__(self, ledbuffer, fadetime, frame_timestamp, colors):
        super(HeroOrbDualColor, self).__init__(
            ledbuffer, fadetime, frame_timestamp)
        self.colors = colors

    def loop(self, frame_timestamp):
        out_colors = tuple(breathe(
            frame_timestamp, color.value if isinstance(color, LedColor)
            else color)
            for color in self.colors)

        for idx in self.ledbuffer.mapping.leds_left_idxs:
            self.ledbuffer.leds[idx] = out_colors[0]
        for idx in self.ledbuffer.mapping.leds_right_idxs:
            self.ledbuffer.leds[idx] = out_colors[1]
