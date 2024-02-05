from utils.monitor_switch import switch

client_id = "<YOUR_ID>"
commands_table = {
    "off": "run('shutdown /s /t 0')",
    "on#1": "run('shutdown /r /t 0')",
    "on#3": switch,
}
