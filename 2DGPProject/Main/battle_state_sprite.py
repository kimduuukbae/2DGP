from pico2d import *
from hero import *
from font import *
class battle_state_spritelist:
    stage_image = None
    back_image = None
    def __init__(self):
        self.hero = hero_status()
        self.font = font()
        if battle_state_spritelist.stage_image == None:
            battle_state_spritelist.stage_image = load_image("../Resources/battle/battle_gameshow.png")
        if battle_state_spritelist.back_image == None:
            battle_state_spritelist.back_image = load_image("../Resources/battle/warrior_back.png")


    def draw(self):
        battle_state_spritelist.stage_image.draw(960,540)
        battle_state_spritelist.back_image.draw(200,170)
        self.hero.draw(600,100)
        self.font.draw(450,160,"전사",(255,255,255))
        self.font.draw(555,102,str(self.hero.gethp()) +' / ' + str(self.hero.getmaxhp()), (255,255,255))
