from pico2d import *
class font:
    font = None
    def __init__(self):
        if font.font == None:
            font.font = load_font("../Resources/font.ttf",30)
    def draw(self,x,y,str,color=(0,0,0)):
        font.font.draw(x,y,str,color)