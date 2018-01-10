"""Core Memory / Projector Memory scene definitions for kickoff"""

from __future__ import division, absolute_import, print_function

from mindorb.scenetypes import LedColor
from mindorb.scenetypes import SceneBase


class KickoffCoreGames(SceneBase):
    def __init__(self, ledbuffer, fadetime):
        super(KickoffCoreGames, self).__init__(ledbuffer, fadetime)
        self.video_name = 'kickoff-core-games'

    def loop(self, frame_timestamp):
        self._ledbuffer.set_all(LedColor.red)


class KickoffCoreHacking(SceneBase):
    def __init__(self, ledbuffer, fadetime):
        super(KickoffCoreHacking, self).__init__(ledbuffer, fadetime)
        self.video_name = 'kickoff-core-hacking'

    def loop(self, frame_timestamp):
        self._ledbuffer.set_all(LedColor.purple)


class KickoffCorePokemon(SceneBase):
    def __init__(self, ledbuffer, fadetime):
        super(KickoffCorePokemon, self).__init__(ledbuffer, fadetime)
        self.video_name = 'kickoff-core-pokemon'

    def loop(self, frame_timestamp):
        self._ledbuffer.set_all(LedColor.green)


class KickoffCoreScifi(SceneBase):
    def __init__(self, ledbuffer, fadetime):
        super(KickoffCoreScifi, self).__init__(ledbuffer, fadetime)
        self.video_name = 'kickoff-core-scifi'

    def loop(self, frame_timestamp):
        self._ledbuffer.set_all(LedColor.blue)
