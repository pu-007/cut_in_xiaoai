import screeninfo
from os import system


def PC():
    # switch to PC
    system("displayswitch.exe 1")


def copy():
    # copying mode
    system("displayswitch.exe 2")


def extend():
    # copying mode
    system("displayswitch.exe 3")


def TV():
    # switch to TV
    system("displayswitch.exe 4")


def switch():
    if screeninfo.get_monitors()[0].width == 1920:
        TV()
    else:
        PC()
