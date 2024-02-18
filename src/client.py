from apis import bafa
import config

# TODO: is local MQTT possible?
# TODO: extend more features to Xiaoai in server side, like playing local music, and insert XiaoaiGPT
# TODO: refactor the archetecture to Client and Server,
# client only executes the commands, server provides the commands
# TODO: Add more functions like open browser, open file, open app, etc.
# TODO a better format
commands_table = {
    "off": "run('shutdown /s /t 0')",
    "on#1": "run('shutdown /r /t 0')",
    "on#2": "monitor_switch.copy()",
    "on#3": "monitor_switch.switch()",
    "on#4": "monitor_switch.extend()",
    "on#5": "monitor_switch.PC()",
    "on#6": "monitor_switch.TV()",
    "on#7": "keyboard.space()",
    "on#8": "keyboard.close()",
    "on#9": "keyboard.fullscreen()",
    "on#10": r"player.play('D:\Videos\Practice\身体\起床拉伸.mp4')",
    "on#11": r"player.random_play('D:\Videos\Practice\冥想', ignore=['正念冥想.mp4'])",
}
# TODO ANDROID auto add commands by autogui

bafa.Bafa(config.client_id, commands_table).loop_forever()
