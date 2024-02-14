from apis import bafa
import config
from utils import monitor_switch

# TODO: is local MQTT possible?
# TODO: extend more features to Xiaoai in server side, like playing local music, and insert XiaoaiGPT
# TODO: refactor the archetecture to Client and Server,
# client only executes the commands, server provides the commands
# TODO: Add more functions like open browser, open file, open app, etc.
commands_table = {
    "off": "run('shutdown /s /t 0')",
    "on#1": "run('shutdown /r /t 0')",
    "on#2": monitor_switch.copy,
    "on#3": monitor_switch.switch,
    "on#4": monitor_switch.extend,
    "on#5": monitor_switch.PC,
    "on#6": monitor_switch.TV,
}

bafa.Bafa(config.client_id, commands_table).loop_forever()
