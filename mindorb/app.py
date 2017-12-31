#!/usr/bin/env python
"""Main Mind Orb application executable"""

from __future__ import division, absolute_import, print_function

from mindorb.ledcontrol import LedManager
from mindorb import scenes


def main():
    led_manager = LedManager(20)
    led_manager.set_scene(scenes.SolidRed, 3)
    led_manager.run()


if __name__ == '__main__':
    main()
