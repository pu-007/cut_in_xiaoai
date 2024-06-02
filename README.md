# cut_in_xiaoai

## config

create `config.py` in `src`

```python
# use built-in functions
import utils
# client_id of Bafa Cloud
client_id = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"

# initialize the utils you need
power = utils.Power()
monitor = utils.Monitor()
keyboard = utils.Keyboard()
player = utils.Player("<your_video_player_command>")
# or you can custom your own utils
@utils.wrapper
def func(): ...

commands_table = {
    # wake computer on another server
    "on": power.WOL("<your_mac_address>"),
    "off": power.shutdown,
    "on#1": power.reboot,
    "on#2": monitor.copy,
    "on#3": monitor.switch,
    "on#4": monitor.extend,
    "on#5": monitor.PC,
    "on#6": monitor.TV,
    "on#7": keyboard.space,
    "on#8": keyboard.close,
    "on#9": keyboard.fullscreen,
    "on#10": player.play(r"/path/to/video"),
    "on#11": player.random_play(r"/path/to/video_directory", ignore=["<video_name>"]),
    "on#12": power.hibernate,
}
```
