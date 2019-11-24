import pico2d
from object import *
from monster_type import monster_TYPE
import game_framework

class Monster_In_Battle(object):
    def __init__(self, name):
        super().__init__(None)
        self.type = monster_TYPE[name]
        self.frame = 0
        self.frameTime = 0.0
        self.imageWidth = 0
        self.imageHeight = 0


class slime(Monster_In_Battle):
    def __init__(self):
        super().__init__("SLIME")
        self.image = pico2d.load_image('../Resources/battle/slimeAtlas.png')
        self.imageWidth = self.image.w // 5
        self.imageHeight = self.image.h // 2
        self.clipWidth = self.imageWidth
        self.clipHeight = self.imageHeight
        self.x = 1700
        self.y = 800
    def update(self):
        self.frameTime += game_framework.frame_time
        if self.frameTime > 0.2:
            self.frameTime = 0.0
            self.frame = (self.frame + 1)%10
    def draw(self):
        self.image.clip_draw(self.frame % 5 * self.imageWidth,(1 - (self.frame // 5)) * self.imageHeight,
                             self.clipWidth, self.clipHeight, self.x, self.y, self.imageWidth, self.imageHeight)


