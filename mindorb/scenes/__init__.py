"""Top-level container module for scene classes"""

from __future__ import division, absolute_import, print_function

from enum import Enum

from .solidcolor import SolidBlack
from .solidcolor import SolidRed
from .solidcolor import SolidGreen
from .solidcolor import SolidBlue


class AllScenes(Enum):
    SolidBlack = SolidBlack
    SolidRed = SolidRed
    SolidGreen = SolidGreen
    SolidBlue = SolidBlue
