import pico2d
from object import *
import game_framework
monster_TYPE = {"FIREMAN" : 1,}
class Monster_In_Menu(object):
    def __init__(self, name):
        super().__init__(None)
        self.type = monster_TYPE[name]
        self.frame = 0
        self.frameTime = 0.0
        pass
    def getMonsterType(self):
        return self.type
    def draw(self):
        self.image.clip_draw(self.clipWidth*self.frame, 0, self.clipWidth, self.clipHeight,
                             self.x + self.pivotX, self.y + self.pivotY, self.imageWidth, self.imageHeight)
    def update(self):
        self.frameTime += game_framework.frame_time
        if self.frameTime > 1.0:
            self.frame = (self.frame + 1)%2
            self.frameTime = 0.0

class fireman(Monster_In_Menu):
    def __init__(self):
        super().__init__("FIREMAN")
        self.image = pico2d.load_image("../Resources/stage/firemanStage.png")
        self.imageWidth = self.image.w
        self.imageHeight = self.image.h + 50
        self.clipWidth = self.imageWidth // 2
        self.clipHeight = self.imageHeight
        self.id = 8
        self.pivotX = 0
        self.pivotY = 70

