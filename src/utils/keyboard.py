from pyautogui import press, hotkey


def space():
    press("space")


def esc():
    press("esc")


def close():
    hotkey("shift", "alt", "esc")


def fullscreen():
    hotkey("alt", "enter")
