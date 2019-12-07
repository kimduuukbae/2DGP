import object as o
from hero import *
from font import *
import math

class main_state_spritelist:
    shake_flag = False
    shake_power = 7.0

    def __init__(self):
        self.hero = HeroStatus()
        self.font = font()
        self.spriteList = []
        self.spriteList.append(o.Object('../Resources/stage/uiShader.png'))
        self.spriteList.append(o.Object('../Resources/stage/character_Icon.png'))
        self.spriteList[0].set_position(960, 100)
        self.spriteList[1].set_position(100, 100)

        self.shake_float = 0.0


    def clear(self):
        self.spriteList.clear()

    def draw(self):
        for i in self.spriteList:
            i.draw(self.shake_float, self.shake_float)
        self.hero.draw(400,100 + self.shake_float)
        self.font.draw(250,160 + self.shake_float, "전사", (255,255,255))
        self.font.draw(355, 102 + self.shake_float, str(self.hero.get_hp()) + ' / ' + str(self.hero.get_maxhp()), (255, 255, 255))

    def reset(self):
        self.hero.shield = 0
        self.hero.get_condition().clear_condition()

    def add_image(self, string):
        self.spriteList.insert(0, o.Object(string))
        self.spriteList[0].set_position(960, 540)

    def list_pop(self):
        self.spriteList.pop(0)

    def update(self):
        if main_state_spritelist.shake_flag:
            self.shake_float = math.sin(main_state_spritelist.shake_power * 10.0) * math.pow(0.5, main_state_spritelist.shake_power) * 20
            main_state_spritelist.shake_power = main_state_spritelist.shake_power - 1
            if main_state_spritelist.shake_power < 0:
                main_state_spritelist.shake_flag = False
                self.shake_float = 0.0

    @staticmethod
    def set_shake(value):
        main_state_spritelist.shake_flag = True
        main_state_spritelist.shake_power = value
