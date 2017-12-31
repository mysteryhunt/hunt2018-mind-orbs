"""Basic / static solid color effect"""

from __future__ import division, absolute_import, print_function

from mindorb.scenetypes import LedColor


class SolidColorBase(object):
    def __init__(self, ledbuffer, fadetime, color):
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
