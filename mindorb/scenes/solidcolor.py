"""Basic / static solid color scene"""

from __future__ import division, absolute_import, print_function

from mindorb.scenetypes import LedColor
from mindorb.scenetypes import SceneBase


class SolidColorBase(SceneBase):
    def __init__(self, ledbuffer, fadetime, color):
        super(SolidColorBase, self).__init__(ledbuffer, fadetime)

        self._ledbuffer = ledbuffer
        self._fadetime = fadetime
        self.color = color

    def loop(self, frame_timestamp):
        self._ledbuffer.set_all(self.color)


class SolidBlack(SolidColorBase):
    def __init__(self, ledbuffer, fadetime):
        super(SolidBlack, self).__init__(ledbuffer, fadetime, LedColor.black)


class SolidRed(SolidColorBase):
    def __init__(self, ledbuffer, fadetime):
        super(SolidRed, self).__init__(ledbuffer, fadetime, LedColor.red)


class SolidGreen(SolidColorBase):
    def __init__(self, ledbuffer, fadetime):
        super(SolidGreen, self).__init__(ledbuffer, fadetime, LedColor.green)


class SolidBlue(SolidColorBase):
    def __init__(self, ledbuffer, fadetime):
        super(SolidBlue, self).__init__(ledbuffer, fadetime, LedColor.blue)
