"""Misc low-level types shared across modules"""

from __future__ import division, absolute_import, print_function

from enum import Enum


class LedColor(Enum):
    black = (0, 0, 0)
    red = (255, 0, 0)
    green = (0, 255, 0)
    blue = (0, 0, 255)


class SceneBase(object):
    def __init__(self, ledbuffer, fadetime):
        self.video_name = None
