import object as o
from hero import *
from font import *
class main_state_spritelist:
    def __init__(self):
        self.hero = hero_status()
        self.font = font()
        self.spriteList = []
        self.spriteList.append(o.object('../Resources/stage/stageArea.png'))
        self.spriteList.append(o.object('../Resources/stage/uiShader.png'))
        self.spriteList.append(o.object('../Resources/stage/character_Icon.png'))

        self.spriteList[0].setPos(960, 540)
        self.spriteList[1].setPos(960, 100)
        self.spriteList[2].setPos(100, 100)

    def clear(self):
        self.spriteList.clear()

    def draw(self):
        for i in self.spriteList:
            i.draw()
        self.hero.draw(400,100)
        self.font.draw(250,160,"전사", (255,255,255))
        self.font.draw(355,102,str(self.hero.gethp()) + ' / ' + str(self.hero.getmaxhp()), (255,255,255))

    def reset(self):
        self.hero.shield = 0