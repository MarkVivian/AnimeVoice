import os

from playsound import playsound

path = "/home/mark/AnimeVoice/Voices/"


# this will check the index.
def play_sound(index):
    # this will list all the files in the directory specified.
    filepath = os.listdir(path)
    if len(filepath) >= index:
        playsound(path + filepath[index - 1])


def state(st):
    if st == 1:
        playsound(f"{path}State/Listen.mp3")
    else:
        playsound(f"{path}State/Quit.mp3")
