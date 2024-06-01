# cut_in_xiaoai

## config

create `config.py` in `src`

```python
# use built-in functions
from utils import *
# or you can
def custom_your_own_function(): ...

# Your Bafa Cloud ID
client_id = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"

power = Power()
monitor = Monitor()
keyboard = Keyboard()
player = Player(r"C:\Users\Administrator\scoop\apps\mpv-git\current\mpv.exe")

commands_table = {
    "on": power.WOL(),  # wake computer on another server
    "off": power.shutdown(),
    "on#1": power.reboot(),
    "on#2": monitor.copy(),
    "on#3": monitor.switch(),
    "on#4": monitor.extend(),
    "on#5": monitor.PC(),
    "on#6": monitor.TV(),
    "on#7": keyboard.space(),
    "on#8": keyboard.close(),
    "on#9": keyboard.fullscreen(),
    "on#10": player.play(r"F:\Practice\身体\起床拉伸.mp4"),
    "on#11": player.random_play(r"F:\Practice\冥想", ignore=["正念冥想.mp4"]),
    "on#12": power.hibernate(),
}
```
