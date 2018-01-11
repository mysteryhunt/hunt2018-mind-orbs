"""Misc low-level types shared across modules"""

from __future__ import division, absolute_import, print_function

from enum import Enum
from itertools import combinations, combinations_with_replacement


class LedColor(Enum):
    black = (0, 0, 0)
    white = (255, 255, 255)
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

DUAL_COLORS = set(combinations(EMOTION_COLORS, 2))

DUAL_COLOR_WITH_SOLIDS = set(combinations_with_replacement(EMOTION_COLORS, 2))


class SceneBase(object):
    def __init__(self, ledbuffer, fadetime, frame_timestamp):
        self.ledbuffer = ledbuffer
        self._fadetime = fadetime

        self.video_name = None
