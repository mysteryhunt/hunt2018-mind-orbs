"""Remote command & control for scene changes"""

from __future__ import division, absolute_import, print_function

import json
import logging
from threading import Thread

import websocket


class CommandReceiver(Thread):
    def __init__(self, scene_manager, websocket_url, device_id):
        super(CommandReceiver, self).__init__(name="command-receiver")
        self.shutting_down = False

        self.scene_manager = scene_manager
        self.device_url = websocket_url
        if not self.device_url.endswith('/'):
            self.device_url += '/'
        self.device_url += device_id
        self.connection = None

    def shutdown(self):
        self.shutting_down = True
        if self.connection:
            self.connection.abort()

    def run(self):
        print("Running CommandReceiver...")
        while not self.shutting_down:
            try:
                self.connection = websocket.create_connection(self.device_url)
                for raw_message in self.connection:
                    message = json.loads(raw_message)
                    self.scene_manager.push_scene(message['scene'],
                                                  message['fade'])
            except websocket.WebSocketConnectionClosedException:
                pass
            except StandardError:
                logging.exception('error with command receiver')
            finally:
                if self.connection and self.connection.connected:
                    self.connection.close()
