#!/usr/bin/env python
"""Main Mind Orb application executable"""

from __future__ import division, absolute_import, print_function

from mindorb.commandreceiver import CommandReceiver
from mindorb.scenecontrol import SceneManager


def main():
    threads = []

    scene_manager = SceneManager(20)
    threads.append(scene_manager)
    command_rcvr = CommandReceiver(scene_manager)
    threads.append(command_rcvr)

    for t in threads:
        t.start()

    # TODO: do this all less shitty maybe?
    while len([t for t in threads if t.is_alive()]) > 0:
        try:
            for t in threads:
                if t.is_alive():
                    t.join(1)
        except KeyboardInterrupt:
            print("KeyboardInterrupt received! -> sending shutdown...")
            for t in threads:
                t.shutdown = True


if __name__ == '__main__':
    main()
