import keyboard
import VoicePlayer


class KeyListener:
    def __init__(self):
        self.event = None
        self.state = False

    def start(self):
        try:
            self.state = True
            while True:
                self.event = keyboard.read_event()
                if self.event.name == "esc":
                    self.checked_pressed()
                if self.state:
                    if self.event.name.isdigit():
                        VoicePlayer.play_sound(int(self.event.name))
                    else:
                        self.HandleLetters()
        except ImportError:
            print("Error occurred while reading the keyboard")

    def checked_pressed(self):
        if not self.state:
            VoicePlayer.state(1)
            self.state = True
        else:
            VoicePlayer.state(2)
            self.state = False

    def HandleLetters(self):
        keyboard_map = {
            'q': 10,
            'w': 11,
            'e': 12,
            'r': 13,
            't': 14,
            'y': 15,
            'u': 16,
            'i': 17,
            'o': 18,
            'p': 19,
            'a': 20,
            's': 21,
            'd': 22,
            'f': 23,
            'g': 24,
            'h': 25,
            'j': 26,
            'k': 27,
            'l': 28,
            'z': 29,
            'x': 30,
            'c': 31,
            'v': 32,
            'b': 33,
            'n': 34,
            'm': 35,
            '`': 36,
            '-': 37,
            '=': 38,
            '[': 39,
            ']': 40,
            '\\': 41,
            ';': 42,
            '\'': 43,
            ',': 44,
            '.': 45,
            '/': 46,
            ' ': 47,
            '~': 48,
            '!': 49,
            '@': 50,
            '#': 51,
            '$': 52,
            '%': 53,
            '^': 54,
            '&': 55,
            '*': 56,
            '(': 57,
            ')': 58,
            '_': 59,
            '+': 60,
            '{': 61,
            '}': 62,
            '|': 63,
            ':': 64,
            '"': 65,
            '<': 66,
            '>': 67,
            '?': 68
        }
        letter = self.event.name
        for i in keyboard_map.keys():
            if f"{letter}".lower() == i:
                value = keyboard_map[i]
                VoicePlayer.play_sound(int(value))
