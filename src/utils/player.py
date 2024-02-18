from subprocess import Popen
from random import choice
from pathlib import Path

# PLAYER_PATH = r"C:\Users\Administrator\scoop\apps\potplayer\current\PotPlayer64.exe"
PLAYER_PATH = r"C:\Users\Administrator\scoop\apps\mpv-git\current\mpv.exe"


def play(file_path):
    Popen([PLAYER_PATH, file_path])


def random_play(video_list, ignore=[]):
    video_list = [
        video for video in Path(video_list).iterdir() if video.name not in ignore
    ]
    play(choice(video_list))
