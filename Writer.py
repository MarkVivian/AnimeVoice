import pyautogui as pg


class Write:
    def __init__(self):
        value = input("the first part of the sentence")

    @staticmethod
    def writer():
        pg.write("hello world")
