"""Core Memory / Projector Memory scene definitions for kickoff"""

from __future__ import division, absolute_import, print_function

from mindorb.scenes.dualcolor import HeroOrbDualColor
from mindorb.scenes.solidcolor import SolidColorBase
from mindorb.scenetypes import LedColor


class KickoffCoreGames(HeroOrbDualColor):
    def __init__(self, ledbuffer, fadetime, frame_timestamp):
        super(KickoffCoreGames, self).__init__(
            ledbuffer, fadetime, frame_timestamp,
            (LedColor.red, LedColor.yellow))
        self.video_name = 'kickoff-core-games'


class KickoffCoreHacking(HeroOrbDualColor):
    def __init__(self, ledbuffer, fadetime, frame_timestamp):
        super(KickoffCoreHacking, self).__init__(
            ledbuffer, fadetime, frame_timestamp,
            (LedColor.purple, LedColor.yellow))
        self.video_name = 'kickoff-core-hacking'


class KickoffCorePokemon(HeroOrbDualColor):
    def __init__(self, ledbuffer, fadetime, frame_timestamp):
        super(KickoffCorePokemon, self).__init__(
            ledbuffer, fadetime, frame_timestamp,
            (LedColor.green, LedColor.yellow))
        self.video_name = 'kickoff-core-pokemon'


class KickoffCoreScifi(HeroOrbDualColor):
    def __init__(self, ledbuffer, fadetime, frame_timestamp):
        super(KickoffCoreScifi, self).__init__(
            ledbuffer, fadetime, frame_timestamp,
            (LedColor.blue, LedColor.yellow))
        self.video_name = 'kickoff-core-scifi'


class KickoffProjDuckHunt(HeroOrbDualColor):
    def __init__(self, ledbuffer, fadetime, frame_timestamp):
        super(KickoffProjDuckHunt, self).__init__(
            ledbuffer, fadetime, frame_timestamp,
            (LedColor.red, LedColor.blue))
        self.video_name = 'kickoff-solo-duckhunt'


class KickoffProjTriviaLouie(SolidColorBase):
    def __init__(self, ledbuffer, fadetime, frame_timestamp):
        super(KickoffProjTriviaLouie, self).__init__(
            ledbuffer, fadetime, frame_timestamp, LedColor.yellow)
        self.video_name = 'kickoff-trio-trivia-a-louie'


class KickoffProjTriviaLouieTouched(HeroOrbDualColor):
    def __init__(self, ledbuffer, fadetime, frame_timestamp):
        super(KickoffProjTriviaLouieTouched, self).__init__(
            ledbuffer, fadetime, frame_timestamp,
            (LedColor.yellow, LedColor.blue))
        self.video_name = 'kickoff-trio-trivia-a-louie'


class KickoffProjTriviaZyzzlvaria(SolidColorBase):
    def __init__(self, ledbuffer, fadetime, frame_timestamp):
        super(KickoffProjTriviaZyzzlvaria, self).__init__(
            ledbuffer, fadetime, frame_timestamp, LedColor.yellow)
        self.video_name = 'kickoff-trio-trivia-b-zyzzlvaria'


class KickoffProjTriviaZyzzlvariaTouched(HeroOrbDualColor):
    def __init__(self, ledbuffer, fadetime, frame_timestamp):
        super(KickoffProjTriviaZyzzlvariaTouched, self).__init__(
            ledbuffer, fadetime, frame_timestamp,
            (LedColor.yellow, LedColor.blue))
        self.video_name = 'kickoff-trio-trivia-b-zyzzlvaria'


class KickoffProjTriviaNpl(SolidColorBase):
    def __init__(self, ledbuffer, fadetime, frame_timestamp):
        super(KickoffProjTriviaNpl, self).__init__(
            ledbuffer, fadetime, frame_timestamp, LedColor.blue)
        self.video_name = 'kickoff-trio-trivia-c-npl'


class KickoffProjNetflixFindingDory(SolidColorBase):
    def __init__(self, ledbuffer, fadetime, frame_timestamp):
        super(KickoffProjNetflixFindingDory, self).__init__(
            ledbuffer, fadetime, frame_timestamp, LedColor.blue)
        self.video_name = 'kickoff-trio-netflix-a-findingdory'


class KickoffProjNetflixGoodDinosaur(SolidColorBase):
    def __init__(self, ledbuffer, fadetime, frame_timestamp):
        super(KickoffProjNetflixGoodDinosaur, self).__init__(
            ledbuffer, fadetime, frame_timestamp, LedColor.blue)
        self.video_name = 'kickoff-trio-netflix-b-gooddinosaur'


class KickoffProjNetflixInsideOut(SolidColorBase):
    def __init__(self, ledbuffer, fadetime, frame_timestamp):
        super(KickoffProjNetflixInsideOut, self).__init__(
            ledbuffer, fadetime, frame_timestamp, LedColor.blue)
        self.video_name = 'kickoff-trio-netflix-c-insideout'


class KickoffProjNetflixInsideOutTouched(HeroOrbDualColor):
    def __init__(self, ledbuffer, fadetime, frame_timestamp):
        super(KickoffProjNetflixInsideOutTouched, self).__init__(
            ledbuffer, fadetime, frame_timestamp,
            (LedColor.yellow, LedColor.blue))
        self.video_name = 'kickoff-trio-netflix-c-insideout'
