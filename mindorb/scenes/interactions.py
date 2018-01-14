"""Always-on scenes for Orb Interactions"""

from __future__ import division, absolute_import, print_function

from mindorb.scenes.dualcolor import HeroOrbDualColor
from mindorb.scenetypes import LedColor


class InteractionGames(HeroOrbDualColor):
    def __init__(self, ledbuffer, fadetime, frame_timestamp):
        super(InteractionGames, self).__init__(
            ledbuffer, fadetime, frame_timestamp,
            (LedColor.red, LedColor.yellow))
        self.video_name = 'interaction-games'


class InteractionHacking(HeroOrbDualColor):
    def __init__(self, ledbuffer, fadetime, frame_timestamp):
        super(InteractionHacking, self).__init__(
            ledbuffer, fadetime, frame_timestamp,
            (LedColor.purple, LedColor.yellow))
        self.video_name = 'interaction-hacking'


class InteractionPokemon(HeroOrbDualColor):
    def __init__(self, ledbuffer, fadetime, frame_timestamp):
        super(InteractionPokemon, self).__init__(
            ledbuffer, fadetime, frame_timestamp,
            (LedColor.green, LedColor.yellow))
        self.video_name = 'interaction-pokemon'


class InteractionScifi(HeroOrbDualColor):
    def __init__(self, ledbuffer, fadetime, frame_timestamp):
        super(InteractionScifi, self).__init__(
            ledbuffer, fadetime, frame_timestamp,
            (LedColor.blue, LedColor.yellow))
        self.video_name = 'interaction-scifi'

class InteractionFinaleWin(HeroOrbDualColor):
    def __init__(self, ledbuffer, fadetime, frame_timestamp):
        super(InteractionFinaleWin, self).__init__(
            ledbuffer, fadetime, frame_timestamp,
            (LedColor.yellow, LedColor.yellow))
        self.video_name = 'interaction-finale-win'
