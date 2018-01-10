"""Memory Rack scenes"""

from __future__ import division, absolute_import, print_function

from collections import namedtuple
import random

from mindorb.effects import breathe
from mindorb.scenetypes import DUAL_COLOR_WITH_SOLIDS, SceneBase


OrbParamTracker = namedtuple('OrbParamTracker',
                             ('orig_colors', 'breath_period', 'breath_phase'))


class RackBreathingOrbs(SceneBase):
    def __init__(self, ledbuffer, fadetime):
        super(RackBreathingOrbs, self).__init__(ledbuffer, fadetime)
        self._all_orbs = self._ledbuffer.mapping.all_orbs

        self.orb_param_tracking = []
        for orb in self._all_orbs:
            orb.set_colors(*random.choice(tuple(DUAL_COLOR_WITH_SOLIDS)))
            self.orb_param_tracking.append(OrbParamTracker(
                orb.colors, 3.5 + random.random(), random.random()))

        # from IPython import embed; embed()

    def loop(self, frame_timestamp):
        for idx, orb in enumerate(self._all_orbs):
            params = self.orb_param_tracking[idx]
            breathe_colors = tuple(
                breathe(frame_timestamp, color,
                        period=params.breath_period, phase=params.breath_phase)
                for color in params.orig_colors)
            orb.set_colors(*breathe_colors)
