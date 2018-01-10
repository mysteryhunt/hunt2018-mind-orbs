"""Always-on scenes for Orb Interactions"""

from __future__ import division, absolute_import, print_function

from mindorb.scenetypes import LedColor
from mindorb.scenetypes import SceneBase


class InteractionGames(SceneBase):
    def __init__(self, ledbuffer, fadetime):
        super(InteractionGames, self).__init__(ledbuffer, fadetime)
        self.video_name = 'interaction-games'

    def loop(self, frame_timestamp):
        self._ledbuffer.set_all(LedColor.red)
        # TODO: add yellow combo


class InteractionHacking(SceneBase):
    def __init__(self, ledbuffer, fadetime):
        super(InteractionHacking, self).__init__(ledbuffer, fadetime)
        self.video_name = 'interaction-hacking'

    def loop(self, frame_timestamp):
        self._ledbuffer.set_all(LedColor.purple)
        # TODO: add yellow combo


class InteractionPokemon(SceneBase):
    def __init__(self, ledbuffer, fadetime):
        super(InteractionPokemon, self).__init__(ledbuffer, fadetime)
        self.video_name = 'interaction-pokemon'

    def loop(self, frame_timestamp):
        self._ledbuffer.set_all(LedColor.green)
        # TODO: add yellow combo


class InteractionScifi(SceneBase):
    def __init__(self, ledbuffer, fadetime):
        super(InteractionScifi, self).__init__(ledbuffer, fadetime)
        self.video_name = 'interaction-scifi'

    def loop(self, frame_timestamp):
        self._ledbuffer.set_all(LedColor.blue)
        # TODO: add yellow combo
