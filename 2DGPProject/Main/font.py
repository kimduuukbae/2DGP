from pico2d import *


class Font:
    font = None

    def __init__(self):
        if Font.font is None:
            Font.font = load_font("../Resources/font.ttf", 30)

    @staticmethod
    def draw(x, y, str, color=(0, 0, 0)):
        Font.font.draw(x, y, str, color)


class Semifont:

    def __init__(self, size=30):
        self.font = load_font("../Resources/font.ttf", size)

    def draw(self, x, y, str, color=(0, 0, 0)):
        self.font.draw(x, y, str, color)
