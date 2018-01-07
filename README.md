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
- `MIND_ORB_LED_STRIP_LEN` (Default: `41`) -> Length in LEDs of the DotStar LED strip
- `MIND_ORB_DEFAULT_SCENE` -> (Default: `SolidBlack`) -> Scene name to use at power-on if the device is not connected to an orb-control server or if the server has no scene to command 

### Fleet Configuration
- `RESIN_HOST_CONFIG_gpu_mem=64` (Required) -> Reserve more GPU memory for video playback using `omxplayer`
- `RESIN_HOST_CONFIG_display_rotate=0x10000` (Required) -> Flip the display output horizontally since the projector is a normal projector, but rear-projecting onto the orb housing
