"""Remote command & control for scene changes"""

from __future__ import division, absolute_import, print_function

import time
from threading import Thread


class CommandReceiver(Thread):
    def __init__(self, scene_manager):
        super(CommandReceiver, self).__init__(name="command-receiver")
        self.shutdown = False

        self.scene_manager = scene_manager

    def run(self):
        print("Running CommandReceiver...")
        # TODO: implement this for real and take out the fake scene-changing
        last_change = None
        import itertools
        scene_iter = itertools.cycle((
            'SolidRed',
            'SolidGreen',
            'SolidBlue',
            'SolidBlack',
        ))

        while not self.shutdown:
            loop_ts = time.time()

            if last_change is None:
                last_change = loop_ts

            if loop_ts - last_change >= 5:
                self.scene_manager.push_scene(next(scene_iter), 3)
                last_change = loop_ts

            time.sleep(0.01)
