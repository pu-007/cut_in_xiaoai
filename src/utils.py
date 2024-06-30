from subprocess import run, Popen, PIPE
from functools import wraps

from random import choice
from pathlib import Path


def wrapper(func):

    def pass_args(*args, **kwargs):

        @wraps(func)
        def pass_excutable():
            func(*args, **kwargs)

        return pass_excutable

    return pass_args


class Player:

    def __init__(self, player_path):
        assert Path(player_path).is_file()
        self.player_path = player_path

    def _play(self, file_path):
        Popen([self.player_path, file_path])

    @wrapper
    def play(self, file_path):
        self._play(file_path)

    @wrapper
    def random_play(self, video_dir, ignore=[], recursive=False, pattern="*"):

        if recursive:
            video_list = [
                str(video)
                for video in Path(video_dir).rglob(pattern)
                if video.name not in ignore
                and video.parent.name not in ignore
                and not video.is_dir()
            ]
        else:
            video_list = [
                str(video)
                for video in Path(video_dir).glob(pattern)
                if video.name not in ignore
            ]
        self._play(choice(video_list))


class Keyboard:

    def __init__(self):
        from pyautogui import press, hotkey

        self.press = press
        self.hotkey = hotkey

    def space(self):
        self.press("space")

    def esc(self):
        self.press("esc")

    def close(self):
        self.hotkey("shift", "alt", "esc")

    def fullscreen(self):
        self.hotkey("alt", "enter")


class Monitor:

    def __init__(self):
        from screeninfo import get_monitors

        self.get_monitors = get_monitors

    def PC(self):
        # switch to PC
        run(["displayswitch.exe", "1"])

    def copy(self):
        # copying mode
        run(["displayswitch.exe", "2"])

    def extend(self):
        # copying mode
        run(["displayswitch.exe", "3"])

    def TV(self):
        # switch to TV
        run(["displayswitch.exe", "4"])

    def switch(self):
        if self.get_monitors()[0].width == 1920:
            run(["displayswitch.exe", "4"])
        else:
            run(["displayswitch.exe", "1"])


class Power:

    def shutdown(self):
        run(["shutdown", "-s", "-t", "0"])

    def reboot(self):
        run(["shutdown", "-r", "-t", "0"])

    @wrapper
    def WOL(self, MAC, interface):
        if run(["which wol"], shell=True, stdout=PIPE, stderr=PIPE).returncode == 0:
            run(["wol", MAC])
        else:
            run(["etherwake", "-i", interface, MAC])

    def hibernate(self):
        # use `powercfg -hibernate off` to sleep(S3) into memory, or you'll hibernate(S4) into disk
        run(["rundll32.exe", "powrprof.dll,SetSuspendState"])
