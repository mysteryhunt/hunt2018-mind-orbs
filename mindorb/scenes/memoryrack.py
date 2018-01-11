"""Memory Rack scenes"""

from __future__ import division, absolute_import, print_function

from collections import namedtuple
import os
import random

from mindorb.effects import breathe
from mindorb.scenetypes import DUAL_COLORS, EMOTION_COLORS, LedColor, SceneBase


OrbParamTracker = namedtuple('OrbParamTracker',
                             ('orig_colors', 'breath_period', 'breath_phase'))


class RackBreathingOrbs(SceneBase):
    SOLID_WEIGHT = \
        int(os.environ.get('MIND_ORB_RACK_SOLID_WEIGHT', '5'))

    def __init__(self, ledbuffer, fadetime, frame_timestamp):
        super(RackBreathingOrbs, self).__init__(
            ledbuffer, fadetime, frame_timestamp)
        self._all_orbs = self.ledbuffer.mapping.all_orbs

        orb_color_distribution = []
        orb_color_distribution.extend(DUAL_COLORS)
        for _ in range(0, self.SOLID_WEIGHT):
            for single_color in EMOTION_COLORS:
                orb_color_distribution.append((single_color, single_color))

        self.orb_param_tracking = []
        for orb in self._all_orbs:
            orb.set_colors(*random.choice(orb_color_distribution))
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
            random.gauss(0.5, 0.2) * self.ALL_OUT_DURATION
            for orb in self._all_orbs]

        self.ledbuffer.set_all(LedColor.black)

    def loop(self, frame_timestamp):
        for idx, orb in enumerate(self._all_orbs):
            orb_zero_time = frame_timestamp - self.out_start_ts - \
                self.out_orb_times[idx]
            if orb_zero_time > 0.25:
                orb.set_colors(LedColor.black, LedColor.black)
            elif orb_zero_time > 0:
                orb.set_colors(LedColor.white, LedColor.white)
            else:
                params = self.orb_param_tracking[idx]
                breathe_colors = tuple(
                    breathe(frame_timestamp, color,
                            period=params.breath_period,
                            phase=params.breath_phase)
                    for color in params.orig_colors)
                orb.set_colors(*breathe_colors)
