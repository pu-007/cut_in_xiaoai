# use built-in functions
import modules


def MonitorHook(mode: str):
    return mode


DEBUG = False

# initialize the modules you need
power = modules.Power()
monitor = modules.Monitor(hook=MonitorHook)
keyboard = modules.Keyboard()

commands_table = {
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
    "on#12": power.hibernate,
}
