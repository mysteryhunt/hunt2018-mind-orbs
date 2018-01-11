"""Memory Rack scenes"""

from __future__ import division, absolute_import, print_function

from collections import namedtuple
import os
import random

from mindorb.effects import breathe
from mindorb.scenetypes import DUAL_COLOR_WITH_SOLIDS, LedColor, SceneBase


OrbParamTracker = namedtuple('OrbParamTracker',
                             ('orig_colors', 'breath_period', 'breath_phase'))


class RackBreathingOrbs(SceneBase):
    def __init__(self, ledbuffer, fadetime, frame_timestamp):
        super(RackBreathingOrbs, self).__init__(
            ledbuffer, fadetime, frame_timestamp)
        self._all_orbs = self.ledbuffer.mapping.all_orbs

        self.orb_param_tracking = []
        for orb in self._all_orbs:
            orb.set_colors(*random.choice(tuple(DUAL_COLOR_WITH_SOLIDS)))
            self.orb_param_tracking.append(OrbParamTracker(
                orb.colors, 3.5 + random.random(), random.random()))
        self.ledbuffer.mapping.orb_param_tracking = self.orb_param_tracking

        self.ledbuffer.set_all(LedColor.black)

    def loop(self, frame_timestamp):
        for idx, orb in enumerate(self._all_orbs):
            params = self.orb_param_tracking[idx]
            breathe_colors = tuple(
                breathe(frame_timestamp, color,
                        period=params.breath_period, phase=params.breath_phase)
                for color in params.orig_colors)
            orb.set_colors(*breathe_colors)


class RackFlickerOut(SceneBase):
    ALL_OUT_DURATION = \
        int(os.environ.get('MIND_ORB_RACK_FLICKER_OUT_DURATION', '5'))

    def __init__(self, ledbuffer, fadetime, frame_timestamp):
        super(RackFlickerOut, self).__init__(
            ledbuffer, fadetime, frame_timestamp)
        self._all_orbs = self.ledbuffer.mapping.all_orbs

        self.orb_param_tracking = self.ledbuffer.mapping.orb_param_tracking
        self.out_start_ts = frame_timestamp
        self.out_orb_times = [
            random.random() * self.ALL_OUT_DURATION for orb in self._all_orbs]

        self.ledbuffer.set_all(LedColor.black)

    def loop(self, frame_timestamp):
        for idx, orb in enumerate(self._all_orbs):
            if frame_timestamp - self.out_start_ts > self.out_orb_times[idx]:
                orb.set_colors(LedColor.black, LedColor.black)
            else:
                params = self.orb_param_tracking[idx]
                breathe_colors = tuple(
                    breathe(frame_timestamp, color,
                            period=params.breath_period,
                            phase=params.breath_phase)
                    for color in params.orig_colors)
                orb.set_colors(*breathe_colors)
