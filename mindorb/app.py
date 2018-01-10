#!/usr/bin/env python
"""Main Mind Orb application executable"""

from __future__ import division, absolute_import, print_function

import os
import signal
import sys

from mindorb.commandreceiver import CommandReceiver
from mindorb.scenecontrol import SceneManager
from mindorb.scenes import get_scene

DEFAULT_LED_STRIP_LEN = 41  # 24 (ring) + 4 * 4 (wedges) + 1 (up)

threads = []


def shutdown(signum, _):
    print("Signal {} received! -> sending shutdown...".format(signum))
    for t in threads:
        t.shutdown()


def main():
    try:
        websocket_url = os.environ['MIND_ORB_WEBSOCKET_URL']
        print("Using MIND_ORB_WEBSOCKET_URL='{}'".format(websocket_url))
    except KeyError:
        print('Missing environment variable: MIND_ORB_WEBSOCKET_URL',
              file=sys.stderr)
        sys.exit(1)
    try:
        device_id = os.environ['MIND_ORB_DEVICE_ID']
        print("Using MIND_ORB_DEVICE_ID='{}'".format(device_id))
    except KeyError:
        print('Missing environment variable: MIND_ORB_DEVICE_ID',
              file=sys.stderr)
        sys.exit(1)

    signal.signal(signal.SIGINT, shutdown)
    signal.signal(signal.SIGTERM, shutdown)

    scene_manager = SceneManager(
        num_pixels=int(os.environ.get('MIND_ORB_LED_STRIP_LEN', 0)),
        led_mapping=os.environ.get('MIND_ORB_LED_MAPPING'),
        default_scene=get_scene(os.environ.get('MIND_ORB_DEFAULT_SCENE')),
        video_manifest_url=os.environ.get('MIND_ORB_VIDEO_MANIFEST_URL')
    )
    threads.append(scene_manager)
    command_rcvr = CommandReceiver(scene_manager, websocket_url, device_id)
    threads.append(command_rcvr)

    for t in threads:
        t.start()

    # TODO: do this all less shitty maybe?
    while len([t for t in threads if t.is_alive()]) > 0:
        for t in threads:
            if t.is_alive():
                t.join(1)


if __name__ == '__main__':
    main()
