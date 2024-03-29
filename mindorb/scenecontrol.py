"""Dealing with LED control directly"""

from __future__ import division, absolute_import, print_function

import collections
import copy
from enum import Enum
import hashlib
from itertools import repeat
import json
import math
import os
import signal
import subprocess
import time
from threading import Thread
import urllib

if os.getenv('RESIN'):
    from dotstar import Adafruit_DotStar
else:
    from DotStar_Emulator import Adafruit_DotStar

from mindorb import scenes
import mindorb.ledmapping
from mindorb.scenes import get_scene
from mindorb.scenetypes import LedColor


ORB_VIDEO_DIR = "/data/orb-video" if os.getenv('RESIN') else "/tmp/orb-video"


class LedBuffer(object):
    LED_BRIGHTNESS = float(os.environ.get('MIND_ORB_LED_BRIGHTNESS', '0.25'))

    def __init__(self, mapping_class, brightness=None, initial_leds=None):
        # Initialize the buffer to all-black by default
        if initial_leds is not None:
            self.leds = copy.copy(initial_leds)
        else:
            self.leds = list(repeat(
                LedColor.black.value, mapping_class.LED_STRIP_LEN))

        self.brightness = self.LED_BRIGHTNESS if brightness is None \
            else brightness
        self.mapping = mapping_class(self.leds)

    def __deepcopy__(self, _):
        new_buffer = LedBuffer(
            self.mapping.__class__,
            brightness=self.brightness, initial_leds=self.leds)

        if hasattr(self.mapping, 'orb_param_tracking'):
            new_buffer.mapping.orb_param_tracking = \
                self.mapping.orb_param_tracking

        return new_buffer

    def set_from_other_buffer(self, other_buffer):
        for idx, _ in enumerate(self.leds):
            self.leds[idx] = other_buffer.leds[idx]

    def set_from_crossfade(
            self, incoming_buffer, outgoing_buffer, ts_relative, duration):
        def ease(start, end):
            # Sinusoidal easing
            return (start - end) / 2 * \
                (math.cos(math.pi * ts_relative / duration) - 1) + start

        for idx, _ in enumerate(self.leds):
            self.leds[idx] = tuple(
                ease(outgoing_buffer.leds[idx][rgb],
                     incoming_buffer.leds[idx][rgb])
                for rgb in (0, 1, 2))

    def set_all(self, color):
        if isinstance(color, LedColor):
            color = color.value

        for idx, _ in enumerate(self.leds):
            self.leds[idx] = color


class ProjectorControl(object):
    def __init__(self, video_manifest_url):
        self.video_manifest_url = video_manifest_url
        self.video_manifest = None
        self._player_proc = None
        self.video_name = None

        self._sync_all_videos()

    def _sync_all_videos(self):
        if not os.path.exists(ORB_VIDEO_DIR):
            os.makedirs(ORB_VIDEO_DIR)

        if self.video_manifest_url is None:
            print("No `video_manifest_url` specified -> skipping fetch")
            return

        local_manifest_file = os.path.join(ORB_VIDEO_DIR, "manifest.json")
        urllib.urlretrieve(self.video_manifest_url, local_manifest_file)
        self.video_manifest = json.load(open(local_manifest_file, 'r'))

        for name, info in self.video_manifest['videos'].iteritems():
            self._sync_video(name, info['url'], info['sha1'])

    def _sync_video(self, name, url, sha1):
        video_file = os.path.join(ORB_VIDEO_DIR, "{}.mp4".format(name))

        if os.path.exists(video_file):
            local_sha1 = hashlib.sha1()
            with open(video_file, 'rb') as f:
                # Do the hash in chunks to not use as much memory
                chunk = f.read(2**16)
                while len(chunk) != 0:
                    local_sha1.update(chunk)
                    chunk = f.read(2**16)

            if local_sha1.hexdigest() == sha1:
                print("Video up to date, skipping download: {}".format(
                    video_file))
                return

        print("Fetching video: {} -> {}".format(url, video_file))
        # TODO: check the SHA1 and only download if needed
        urllib.urlretrieve(url, video_file)

    def start(self, video_name):
        if self.video_name == video_name:
            return

        self.stop()
        print("Starting video: {}".format(video_name))
        video_file = os.path.join(ORB_VIDEO_DIR, "{}.mp4".format(video_name))

        if os.getenv('RESIN'):
            self._player_proc = subprocess.Popen(
                ["omxplayer",
                    "-n", "-1", "--no-osd", "--aspect-mode", "fill", "--loop",
                    video_file],
                stdin=subprocess.PIPE, stdout=open(os.devnull, 'wb'),
                # Assign a new process group so the child process can be killed
                preexec_fn=os.setsid)
        else:
            print("Not on a Pi, would open video: {}".format(video_file))

        self.video_name = video_name

    def stop(self):
        print("Stopping video: {}".format(self.video_name))
        self.video_name = None

        if self._player_proc is None:
            return

        # We need to kill the whole group because the `omxplayer` command
        # spawns a child process that doesn't get the normal `Popen.kill()`
        # signal.
        os.killpg(os.getpgid(self._player_proc.pid), signal.SIGTERM)


class SceneManager(Thread):
    def __init__(
        self, led_mapping=None,
        default_scene=None,
        spi_freq=1000000, led_order='bgr',
        video_manifest_url=None,
        target_frame_rate=60, perf_dump_pd=10
    ):
        super(SceneManager, self).__init__(name="scene-manager")
        self.shutting_down = False

        self.mapping_class = getattr(mindorb.ledmapping, led_mapping) \
            if led_mapping is not None else None
        self.ledbuffer = LedBuffer(mapping_class=self.mapping_class)
        self.num_pixels = len(self.ledbuffer.leds)

        print("SceneManager using mapping class: {}".format(led_mapping))
        print("SceneManager using {} pixels".format(self.num_pixels))

        self.projector = ProjectorControl(video_manifest_url)

        self._scene_queue = collections.deque()  # TODO: maybe bound this?
        self.scene_outgoing = None
        self.scene = None
        self._set_scene(default_scene, 0, time.time())

        self.scene_change_start_ts = 0
        self.scene_change_duration = 0

        if os.getenv('RESIN'):
            self._dotstar_strip = Adafruit_DotStar(
                self.num_pixels, spi_freq, order=led_order
            )
        else:
            # Unfortunately: the emulator doesn't support the `order` kwarg...
            self._dotstar_strip = Adafruit_DotStar(self.num_pixels)

        self._dotstar_strip.begin()

        self.target_frame_rate = target_frame_rate
        self.perf_dump_pd = perf_dump_pd
        self.perf_last_dump = None
        self.perf_frames = None

    def shutdown(self):
        self.shutting_down = True

    def push_scene(self, new_scene, fadetime):
        new_scene = get_scene(new_scene)

        print("Queueing scene change: new_scene={}, fadetime={}".format(
            new_scene, fadetime
        ))

        # TODO: Maybe make this bounded?
        self._scene_queue.append((new_scene, fadetime))

    def run(self):
        print("Running SceneManager...")
        while not self.shutting_down:
            frame_timestamp = time.time()
            self.scene.loop(frame_timestamp)
            self._run_leds(frame_timestamp)
            self._run_projector(frame_timestamp)
            self._pop_scene(frame_timestamp)

            self._run_perf(frame_timestamp)

            desired_sleep = (
                1.0 / self.target_frame_rate - (time.time() - frame_timestamp))
            if desired_sleep > 0:
                time.sleep(desired_sleep)

        self._cleanup()

    def _run_perf(self, frame_timestamp):
        if self.perf_last_dump is None:
            self.perf_last_dump = frame_timestamp
            self.perf_frames = 1

        time_since_last_perf = frame_timestamp - self.perf_last_dump
        if time_since_last_perf > self.perf_dump_pd:
            print("SceneManager FPS: target={}, actual={}".format(
                self.target_frame_rate,
                self.perf_frames / time_since_last_perf))
            self.perf_last_dump = frame_timestamp
            self.perf_frames = 1
        else:
            self.perf_frames += 1

    def _pop_scene(self, frame_timestamp):
        try:
            new_scene, fadetime = self._scene_queue.popleft()
            self._set_scene(new_scene, fadetime, frame_timestamp)
        except IndexError:
            # This is fine -> no scene is available to change
            pass

    def _set_scene(self, new_scene, fadetime, frame_timestamp):
        if self.scene.__class__ is new_scene:
            # Make this a no-op if the scene has not changed
            print("Ignoring scene change: old={}, new={}".format(
                self.scene, new_scene
            ))
            return

        print("Changing scene: old={}, new={}, fadetime={}".format(
            self.scene, new_scene, fadetime))

        self.scene_outgoing = self.scene
        if self.scene_outgoing is None:
            outgoing_ledbuffer = LedBuffer(mapping_class=self.mapping_class)
        else:
            outgoing_ledbuffer = copy.deepcopy(self.scene_outgoing.ledbuffer)
        self.scene = new_scene(outgoing_ledbuffer, fadetime, frame_timestamp)

        self.scene_change_start_ts = frame_timestamp
        self.scene_change_duration = fadetime

    def _run_leds(self, frame_timestamp):
        # Check if there's an in-progress scene change and do the crossfade
        scene_change_progress = frame_timestamp - self.scene_change_start_ts
        if scene_change_progress < self.scene_change_duration and \
                self.scene_outgoing is not None:
            self.ledbuffer.set_from_crossfade(
                self.scene.ledbuffer, self.scene_outgoing.ledbuffer,
                scene_change_progress, self.scene_change_duration)
        else:
            self.ledbuffer.set_from_other_buffer(self.scene.ledbuffer)

        # Special-case the the up-facing LED off in there is a video running
        if self.scene.video_name is not None and \
                isinstance(self.ledbuffer.mapping,
                           mindorb.ledmapping.HeroOrbMapping):
            self.ledbuffer.leds[40] = LedColor.black.value

        self._dotstar_strip.setBrightness(
            int(255 * self.ledbuffer.brightness)
        )

        for idx in xrange(self.num_pixels):
            color = self.ledbuffer.leds[idx]
            self._dotstar_strip.setPixelColor(
                idx,
                int(round(color[0])) << (2 * 8) |
                int(round(color[1])) << (1 * 8) |
                int(round(color[2])) << (0 * 8)
            )

        self._dotstar_strip.show()

    def _run_projector(self, frame_timestamp):
        if self.scene.video_name is None and \
                self.projector.video_name is not None:
            self.projector.stop()
        elif self.scene.video_name != self.projector.video_name:
            self.projector.start(self.scene.video_name)

    def _cleanup(self):
        print("Cleaning up SceneManager...")

        print("Blanking LEDs...")
        for idx in xrange(self.num_pixels):
            self._dotstar_strip.setPixelColor(idx, 0x000000)
        self._dotstar_strip.show()

        print("Done cleaning up SceneManager")
