# cut_in_xiaoai

WOL 功能现在可以使用 open-xiaoai 项目的 server 来实现。

而其他功能可以考虑增加一个新的服务端，替换掉巴法云。或者整体重构，与 open-xiaoai server 通信。

## Usage

run `python /path/to/src`

## Config

create `src/config.py`

```python
# use built-in functions
import modules
# client_id of Bafa Cloud
client_id = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"

# you can custom your own modules
@modules.wrapper
def func(): ...

def MonitorHook(mode: str):
    pass

# initialize the modules you need
power = modules.Power()
monitor = modules.Monitor(hook=MonitorHook)
keyboard = modules.Keyboard()
player = modules.Player("<your_video_player_command>")

commands_table = {
    # wake computer on another server
    "on": power.WOL("<your_mac_address>"),
    "off": power.shutdown,
    "on#1": power.reboot,
    "on#2": monitor.copy,
    "on#3": monitor.switch(default_width=2560),
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

## References

- [xiaogpt](https://github.com/yihong0618/xiaogpt?tab=readme-ov-file)
- [xiaomusic](https://github.com/hanxi/xiaomusic)
