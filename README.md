# MIT Mysery Hunt 2018 - Mind Orbs
TODO -> flesh this out more

## Local Dev Setup
1. Ensure you have a Python 2.7 install for this.
2. Make sure you have `pipenv` installed: https://docs.pipenv.org/
3. Install local dev requirements: `pipenv install --dev`
4. Start the local DotStart emulator (you can just leave thus running while you're developing): `scripts-dev/dotstar-emulator`
5. Run the main application (Ctrl-C to shutdown): `scripts-dev/mindorb`

## Resin App Configuration
These values are configured in the Resin App web interface

### Env Vars
- `MIND_ORB_WEBSOCKET_URL` (Required) -> Websocket URL for the orb-control server (https://github.com/mysteryhunt/hunt2018-orb-control).  Ex: `wss://orb-control.head-hunters.org/ws`
- `MIND_ORB_DEVICE_ID` (Required) -> Device name used when connecting to the orb-control server
- `MIND_ORB_LED_MAPPING` (Default: `HeroOrbMapping`) -> Class that determines the layout of the LED strips.  Minimally, defines the length of the strip.  Can also define other logical mappings useful to scenes.
- `MIND_ORB_DEFAULT_SCENE` -> (Default: None) -> Scene name to use at power-on if the device is not connected to an orb-control server or if the server has no scene to command.  Defaults to nothing (black).
- `MIND_ORB_VIDEO_MANIFEST_URL` -> URL for a manifest file mapping `video_name` for scenes to video URLs.  Videos will be downloaded at startup.  If unspecified, no videos are fetched, and it's the user's responsibility to manually place the needed videos in `/data/orb-video`.

### Fleet Configuration
- `RESIN_HOST_CONFIG_gpu_mem=64` (Required) -> Reserve more GPU memory for video playback using `omxplayer`
- `RESIN_HOST_CONFIG_display_rotate=0x10000` (Required) -> Flip the display output horizontally since the projector is a normal projector, but rear-projecting onto the orb housing
