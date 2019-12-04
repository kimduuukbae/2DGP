import object as o
from hero import *
from font import *
class main_state_spritelist:
    def __init__(self):
        self.hero = HeroStatus()
        self.font = font()
        self.spriteList = []
        self.spriteList.append(o.Object('../Resources/stage/uiShader.png'))
        self.spriteList.append(o.Object('../Resources/stage/character_Icon.png'))
        self.spriteList[0].set_position(960, 100)
        self.spriteList[1].set_position(100, 100)

    def clear(self):
        self.spriteList.clear()

    def draw(self):
        for i in self.spriteList:
            i.draw()
        self.hero.draw(400,100)
        self.font.draw(250,160,"전사", (255,255,255))
        self.font.draw(355, 102, str(self.hero.get_hp()) + ' / ' + str(self.hero.get_maxhp()), (255, 255, 255))

    def reset(self):
        self.hero.shield = 0

    def add_image(self, string):
        self.spriteList.insert(0, o.Object(string))
        self.spriteList[0].set_position(960, 540)