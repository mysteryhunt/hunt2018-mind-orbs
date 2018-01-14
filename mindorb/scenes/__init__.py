"""Top-level container module for scene classes"""

from __future__ import division, absolute_import, print_function

from enum import Enum
import inspect

from mindorb.scenetypes import SceneBase

from . import interactions
from . import kickoff
from . import memoryrack
from . import solidcolor
from . import test


def get_scene(scene):
    if scene is None:
        return solidcolor.SolidBlack
    elif inspect.isclass(scene) and issubclass(scene, SceneBase):
        return scene
    elif isinstance(scene, AllScenes):
        return scene.value
    elif isinstance(scene, basestring):
        try:
            return getattr(AllScenes, scene).value
        except AttributeError:
            raise ValueError("`scene` '{}' not found!".format(scene))
    else:
        raise TypeError("Cannot convert to scene from: `{}`".format(scene))


class AllScenes(Enum):
    InteractionGames = interactions.InteractionGames
    InteractionHacking = interactions.InteractionHacking
    InteractionPokemon = interactions.InteractionPokemon
    InteractionScifi = interactions.InteractionScifi
    InteractionFinaleWin = interactions.InteractionFinaleWin

    KickoffCoreGames = kickoff.KickoffCoreGames
    KickoffCoreHacking = kickoff.KickoffCoreHacking
    KickoffCorePokemon = kickoff.KickoffCorePokemon
    KickoffCoreScifi = kickoff.KickoffCoreScifi

    KickoffProjDuckHunt = kickoff.KickoffProjDuckHunt

    KickoffProjTriviaLouie = kickoff.KickoffProjTriviaLouie
    KickoffProjTriviaLouieTouched = kickoff.KickoffProjTriviaLouieTouched
    KickoffProjTriviaZyzzlvaria = kickoff.KickoffProjTriviaZyzzlvaria
    KickoffProjTriviaZyzzlvariaTouched = \
        kickoff.KickoffProjTriviaZyzzlvariaTouched
    KickoffProjTriviaNpl = kickoff.KickoffProjTriviaNpl

    KickoffProjNetflixFindingDory = kickoff.KickoffProjNetflixFindingDory
    KickoffProjNetflixGoodDinosaur = kickoff.KickoffProjNetflixGoodDinosaur
    KickoffProjNetflixInsideOut = kickoff.KickoffProjNetflixInsideOut
    KickoffProjNetflixInsideOutTouched = \
        kickoff.KickoffProjNetflixInsideOutTouched

    RackBreathingOrbs = memoryrack.RackBreathingOrbs
    RackFlickerOut = memoryrack.RackFlickerOut

    SolidBlack = solidcolor.SolidBlack
    SolidRed = solidcolor.SolidRed
    SolidGreen = solidcolor.SolidGreen
    SolidBlue = solidcolor.SolidBlue
    SolidYellow = solidcolor.SolidYellow
    SolidPurple = solidcolor.SolidPurple

    TestStripChase = test.TestStripChase
    TestMemoryRackRandom = test.TestMemoryRackRandom
    TestHueFade = test.TestHueFade
