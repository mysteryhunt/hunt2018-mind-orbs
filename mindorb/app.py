#!/usr/bin/env python
"""Main Mind Orb application executable"""

from __future__ import division, absolute_import, print_function

from threading import Thread

from mindorb.scenecontrol import SceneManager
from mindorb import scenes


def main():
    scene_manager = SceneManager(20)
    scene_manager.run()


if __name__ == '__main__':
    main()
