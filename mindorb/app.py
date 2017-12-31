#!/usr/bin/env python
"""Main Mind Orb application executable"""

from __future__ import division, absolute_import, print_function

from threading import Thread

from mindorb.scenecontrol import SceneManager
from mindorb import scenes


def main():
    scene_manager = SceneManager(20)
    scene_thread = Thread(name="scene-manager", target=scene_manager.run)
    scene_thread.run()

    # TODO: hard-fail if any sub-thread exits -> process restart from systemd
    scene_thread.join()


if __name__ == '__main__':
    main()
