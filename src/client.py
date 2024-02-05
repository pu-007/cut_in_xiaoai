from apis import bafa
import config
from utils.monitor_switch import switch

commands_table = {
    "off": "run('shutdown /s /t 0')",
    "on#1": "run('shutdown /r /t 0')",
    "on#3": switch,
}

bafa.Bafa(config.client_id, commands_table).loop_forever()
