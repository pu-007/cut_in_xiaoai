import screeninfo
from os import system


def switch():
    if screeninfo.get_monitors()[0].width == 1920:
        # switch to TC
        system("displayswitch.exe 4")
    else:
        # switch to PC
        system("displayswitch.exe 1")
