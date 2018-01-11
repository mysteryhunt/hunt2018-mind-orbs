"""Basic / static solid color scene"""

from __future__ import division, absolute_import, print_function

from mindorb.effects import breathe
from mindorb.scenetypes import LedColor
from mindorb.scenetypes import SceneBase


class SolidColorBase(SceneBase):
    def __init__(self, ledbuffer, fadetime, frame_timestamp, color):
        super(SolidColorBase, self).__init__(
            ledbuffer, fadetime, frame_timestamp)
        self.color = color

    def loop(self, frame_timestamp):
        breathe_color = breathe(frame_timestamp, self.color.value)
        self.ledbuffer.set_all(breathe_color)


class SolidBlack(SolidColorBase):
    def __init__(self, ledbuffer, fadetime, frame_timestamp):
        super(SolidBlack, self).__init__(
            ledbuffer, fadetime, frame_timestamp, LedColor.black)


class SolidRed(SolidColorBase):
    def __init__(self, ledbuffer, fadetime, frame_timestamp):
        super(SolidRed, self).__init__(
            ledbuffer, fadetime, frame_timestamp, LedColor.red)


class SolidGreen(SolidColorBase):
    def __init__(self, ledbuffer, fadetime, frame_timestamp):
        super(SolidGreen, self).__init__(
            ledbuffer, fadetime, frame_timestamp, LedColor.green)


class SolidBlue(SolidColorBase):
    def __init__(self, ledbuffer, fadetime, frame_timestamp):
        super(SolidBlue, self).__init__(
            ledbuffer, fadetime, frame_timestamp, LedColor.blue)


class SolidYellow(SolidColorBase):
    def __init__(self, ledbuffer, fadetime, frame_timestamp):
        super(SolidYellow, self).__init__(
            ledbuffer, fadetime, frame_timestamp, LedColor.yellow)


class SolidPurple(SolidColorBase):
    def __init__(self, ledbuffer, fadetime, frame_timestamp):
        super(SolidPurple, self).__init__(
            ledbuffer, fadetime, frame_timestamp, LedColor.purple)
