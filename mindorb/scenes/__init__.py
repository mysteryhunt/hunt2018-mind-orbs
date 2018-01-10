"""Top-level container module for scene classes"""

from __future__ import division, absolute_import, print_function

from enum import Enum
import inspect

from mindorb.scenetypes import SceneBase

from . import interactions
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
    SolidBlack = solidcolor.SolidBlack
    SolidRed = solidcolor.SolidRed
    SolidGreen = solidcolor.SolidGreen
    SolidBlue = solidcolor.SolidBlue
    SolidYellow = solidcolor.SolidYellow
    SolidPurple = solidcolor.SolidPurple
    TestStripChase = test.TestStripChase
    TestMemoryRackRandom = test.TestMemoryRackRandom
