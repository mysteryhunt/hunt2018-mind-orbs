"""Misc low-level types shared across modules"""

from __future__ import division, absolute_import, print_function

from enum import Enum


class LedColor(Enum):
    black = (0, 0, 0)
    red = (255, 0, 0)
    green = (0, 255, 0)
    blue = (0, 0, 255)
    yellow = (255, 255, 0)
    purple = (128, 0, 128)


EMOTION_COLORS = {
    LedColor.red,
    LedColor.green,
    LedColor.blue,
    LedColor.yellow,
    LedColor.purple
}


class SceneBase(object):
    def __init__(self, ledbuffer, fadetime):
        self._ledbuffer = ledbuffer
        self._fadetime = fadetime

        self.video_name = None
