"""Core Memory / Projector Memory scene definitions for kickoff"""

from __future__ import division, absolute_import, print_function

from mindorb.scenes.solidcolor import SolidColorBase
from mindorb.scenetypes import LedColor
from mindorb.scenetypes import SceneBase


class KickoffCoreGames(SceneBase):
    def __init__(self, ledbuffer, fadetime):
        super(KickoffCoreGames, self).__init__(ledbuffer, fadetime)
        self.video_name = 'kickoff-core-games'

    def loop(self, frame_timestamp):
        self._ledbuffer.set_all(LedColor.red)
        # TODO: add yellow combo


class KickoffCoreHacking(SceneBase):
    def __init__(self, ledbuffer, fadetime):
        super(KickoffCoreHacking, self).__init__(ledbuffer, fadetime)
        self.video_name = 'kickoff-core-hacking'

    def loop(self, frame_timestamp):
        self._ledbuffer.set_all(LedColor.purple)
        # TODO: add yellow combo


class KickoffCorePokemon(SceneBase):
    def __init__(self, ledbuffer, fadetime):
        super(KickoffCorePokemon, self).__init__(ledbuffer, fadetime)
        self.video_name = 'kickoff-core-pokemon'

    def loop(self, frame_timestamp):
        self._ledbuffer.set_all(LedColor.green)
        # TODO: add yellow combo


class KickoffCoreScifi(SceneBase):
    def __init__(self, ledbuffer, fadetime):
        super(KickoffCoreScifi, self).__init__(ledbuffer, fadetime)
        self.video_name = 'kickoff-core-scifi'

    def loop(self, frame_timestamp):
        self._ledbuffer.set_all(LedColor.blue)
        # TODO: add yellow combo


class KickoffProjDuckHunt(SceneBase):
    def __init__(self, ledbuffer, fadetime):
        super(KickoffProjDuckHunt, self).__init__(ledbuffer, fadetime)
        self.video_name = 'kickoff-solo-duckhunt'

    def loop(self, frame_timestamp):
        self._ledbuffer.set_all(LedColor.red)
        # TODO: add blue combo


class KickoffProjTriviaLouie(SolidColorBase):
    def __init__(self, ledbuffer, fadetime):
        super(KickoffProjTriviaLouie, self).__init__(
            ledbuffer, fadetime, LedColor.yellow)
        self.video_name = 'kickoff-trio-trivia-a-louie'


class KickoffProjTriviaZyzzlvaria(SolidColorBase):
    def __init__(self, ledbuffer, fadetime):
        super(KickoffProjTriviaZyzzlvaria, self).__init__(
            ledbuffer, fadetime, LedColor.yellow)
        self.video_name = 'kickoff-trio-trivia-b-zyzzlvaria'


class KickoffProjTriviaNpl(SolidColorBase):
    def __init__(self, ledbuffer, fadetime):
        super(KickoffProjTriviaNpl, self).__init__(
            ledbuffer, fadetime, LedColor.blue)
        self.video_name = 'kickoff-trio-trivia-c-npl'


class KickoffProjNetflixFindingDory(SolidColorBase):
    def __init__(self, ledbuffer, fadetime):
        super(KickoffProjNetflixFindingDory, self).__init__(
            ledbuffer, fadetime, LedColor.blue)
        self.video_name = 'kickoff-trio-netflix-a-findingdory'


class KickoffProjNetflixGoodDinosaur(SolidColorBase):
    def __init__(self, ledbuffer, fadetime):
        super(KickoffProjNetflixGoodDinosaur, self).__init__(
            ledbuffer, fadetime, LedColor.blue)
        self.video_name = 'kickoff-trio-netflix-b-gooddinosaur'


class KickoffProjNetflixInsideOut(SolidColorBase):
    def __init__(self, ledbuffer, fadetime):
        super(KickoffProjNetflixInsideOut, self).__init__(
            ledbuffer, fadetime, LedColor.blue)
        self.video_name = 'kickoff-trio-netflix-c-insideout'


class KickoffProjNetflixInsideOutBlueYellow(SceneBase):
    def __init__(self, ledbuffer, fadetime):
        super(KickoffProjNetflixInsideOutBlueYellow, self).__init__(
            ledbuffer, fadetime)
        self.video_name = 'kickoff-trio-netflix-c-insideout'

    def loop(self, frame_timestamp):
        self._ledbuffer.set_all(LedColor.blue)
        # TODO: add yellow combo
