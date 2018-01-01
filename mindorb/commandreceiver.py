"""Remote command & control for scene changes"""

from __future__ import division, absolute_import, print_function

import json
import logging
import time
from threading import Thread

import websocket


class CommandReceiver(Thread):
    def __init__(self, scene_manager, websocket_url, device_id):
        super(CommandReceiver, self).__init__(name="command-receiver")
        self.shutdown = False

        self.scene_manager = scene_manager
        self.device_url = websocket_url
        if not self.device_url.endswith('/'):
            self.device_url += '/'
        self.device_url += device_id

    def run(self):
        print("Running CommandReceiver...")
        while not self.shutdown:
            try:
                connection = None
                try:
                    connection = websocket.create_connection(self.device_url)
                    for raw_message in connection:
                        message = json.loads(raw_message)
                        self.scene_manager.push_scene(message['scene'],
                                                      message['fade'])
                finally:
                    if connection:
                        connection.close()
            except StandardError:
                logging.exception('error with command receiver')
