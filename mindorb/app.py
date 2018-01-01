#!/usr/bin/env python
"""Main Mind Orb application executable"""

from __future__ import division, absolute_import, print_function

import os
import signal
import sys

from mindorb.commandreceiver import CommandReceiver
from mindorb.scenecontrol import SceneManager


threads = []


def shutdown(signum, _):
    print("Signal {} received! -> sending shutdown...".format(signum))
    for t in threads:
        t.shutdown()


def main():
    try:
        websocket_url = os.environ['MIND_ORB_WEBSOCKET_URL']
    except KeyError:
        print('Missing environment variable: MIND_ORB_WEBSOCKET_URL',
              file=sys.stderr)
        sys.exit(1)
    try:
        device_id = os.environ['MIND_ORB_DEVICE_ID']
    except KeyError:
        print('Missing environment variable: MIND_ORB_DEVICE_ID',
              file=sys.stderr)
        sys.exit(1)

    signal.signal(signal.SIGINT, shutdown)
    signal.signal(signal.SIGTERM, shutdown)

    scene_manager = SceneManager(20)
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
