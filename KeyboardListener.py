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
        except ImportError:
            print("Error occurred while reading the keyboard")

    def checked_pressed(self):
        if not self.state:
            VoicePlayer.state(1)
            self.state = True
        else:
            VoicePlayer.state(2)
            self.state = False
