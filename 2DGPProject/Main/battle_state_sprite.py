from pico2d import *

class battle_state_spritelist:
    stage_image = None
    back_image = None
    def __init__(self):

        if battle_state_spritelist.stage_image == None:
            battle_state_spritelist.stage_image = load_image("../Resources/battle/battle_gameshow.png")
        if battle_state_spritelist.back_image == None:
            battle_state_spritelist.back_image = load_image("../Resources/battle/warrior_back.png")
    def draw(self):
        battle_state_spritelist.stage_image.draw(960,540)
        battle_state_spritelist.back_image.draw(200,170)
