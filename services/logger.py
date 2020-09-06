class Color:
    Orange = "\033[33m{}\033[00m"
    Red = "\033[91m{}\033[00m"
    Green = "\033[92m{}\033[00m"
    Yellow = "\033[93m{}\033[00m"
    Cyan = "\033[96m{}\033[00m"
    LightGray = "\033[97m{}\033[00m"


class Logger:
    def __init__(self, color=Color.LightGray, auto_clear=False):
        self.color = color
        self.auto_clear = auto_clear

    def color(self, color):
        self.color = color

    def auto_clear(self, auto_clear):
        self.auto_clear = auto_clear

    def log(self, text):
        print(self.color.format(text))
        if self.auto_clear:
            self.color = Color.LightGray
