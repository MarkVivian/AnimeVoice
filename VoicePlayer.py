import os

from playsound import playsound

path = "/home/mark/Documents/Online/Backend/python_for_backend/AnimeVoice/"


# this will check the index.
def play_sound(index):
    try:
        # this will list all the files in the directory specified.
        filepath = os.listdir(path + "Voices/")
        if len(filepath) >= index:
            print(filepath[index - 1])
            playsound(path + "Voices/" + filepath[index - 1])
    except Exception:
        print("an error occurred while finding the song")


def state(st):
    if st == 1:
        playsound(f"{path}State/Listen.mp3")
    else:
        playsound(f"{path}State/Quit.mp3")