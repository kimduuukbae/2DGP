from hero import *
from font import *
from monster_in_battle import *
import winsound
import banner
import main_state
import math


class Battle_state_sprite:
    stage_image = []
    back_image = None
    info_image = None
    condition_image = None
    banner = None
    shake_flag = False
    shake_power = 7.0
    def __init__(self):
        self.hero = HeroStatus()
        self.monster = Monsterstatus()
        self.victory_flag = 0
        self.font = font()
        self.vertexX = 0
        self.time_to_banner = 0.0

        self.shake_float = 0.0
        self.shake_flag = False
        self.shake_power = 7.0

        if len(Battle_state_sprite.stage_image) == 0:
            Battle_state_sprite.stage_image.append(load_image("../Resources/battle/battle_gameshow.png"))
            Battle_state_sprite.stage_image.append(load_image("../Resources/battle/battle_ice.png"))
        if Battle_state_sprite.back_image is None:
            Battle_state_sprite.back_image = load_image("../Resources/battle/warrior_back.png")
        if Battle_state_sprite.banner is None:
            Battle_state_sprite.banner = banner.WinBanner()
        if Battle_state_sprite.condition_image is None:
            Battle_state_sprite.condition_image = load_image('../Resources/common/condition_text_bar.png')

        self.monstersprite = make_monster(self.hero.enemy_type)
        self.monster.set_status(self.monstersprite)

        Battle_state_sprite.banner.init()

    def draw(self):
        Battle_state_sprite.stage_image[main_state.stage_collection.get_stage_idx()].draw(960+ self.shake_float, 540+ self.shake_float)
        Battle_state_sprite.back_image.draw(200+ self.shake_float, 170+ self.shake_float)

        self.hero.draw(600 + self.shake_float, 100 + self.shake_float)
        self.font.draw(450 + self.shake_float, 160 + self.shake_float, "전사", (255, 255, 255))
        if self.hero.shield == 0:
            self.font.draw(555 + self.shake_float, 102 + self.shake_float, str(self.hero.get_hp()) + ' / ' + str(self.hero.get_maxhp()), (255, 255, 255))
        else:
            self.font.draw(535 + self.shake_float, 102 + self.shake_float, str(self.hero.get_hp()) + ' / ' + str(self.hero.get_maxhp()) + ' + ' + str(self.hero.shield), (255, 255, 150))

        self.monster.draw(1400 + self.vertexX+ self.shake_float,800 + self.shake_float)
        self.font.draw(1250 + self.vertexX+ self.shake_float, 860 + self.shake_float, self.monster.name, (255, 255, 255))
        self.font.draw(1355 + self.vertexX+ self.shake_float, 802 + self.shake_float, str(self.monster.hp) + ' / ' + str(self.monster.max_hp), (255, 255, 255))

        self.monstersprite.draw(self.vertexX+ self.shake_float, self.shake_float)
        Battle_state_sprite.condition_image.draw(600 + self.shake_float, 45 + self.shake_float)
        Battle_state_sprite.condition_image.draw(1400 + self.vertexX+ self.shake_float, 745 + self.shake_float)

        for i in range(len(self.hero.status_condition.get_condition_list())):
            condition_name = STATUS_CONDITION[self.hero.status_condition.get_condition_to_idx(i).get_type()]
            get_condition_count = self.hero.status_condition.get_condition_to_idx(i).get_count()
            self.font.draw(470 + (i * 150) + self.shake_float, 46 + self.shake_float, condition_name + "  " + str(get_condition_count), (139, 0, 255))

        if self.victory_flag == 3:
            Battle_state_sprite.banner.draw()

    def update(self):
        self.monstersprite.update()

        if self.victory_flag == 0:
            if HeroStatus.hp <= 0 or Monsterstatus.hp <= 0:
                self.victory_flag = 1
                winsound.PlaySound('../Resources/battle/herowinsound.wav', winsound.SND_FILENAME | winsound.SND_NOWAIT | \
                winsound.SND_ASYNC)

        if self.victory_flag == 1:
            self.time_to_banner += game_framework.frame_time
            self.vertexX += 10
            if self.time_to_banner > 2.0:
                if HeroStatus.hp <= 0:
                    self.victory_flag = 2
                elif Monsterstatus.hp <= 0:
                    self.victory_flag = 3
                self.time_to_banner = 0.0

        if self.victory_flag == 3:
            Battle_state_sprite.banner.update()

        if Battle_state_sprite.shake_flag:
            self.shake_float = math.sin(Battle_state_sprite.shake_power * 10.0) * math.pow(0.5, Battle_state_sprite.shake_power) * 20
            Battle_state_sprite.shake_power = Battle_state_sprite.shake_power - 1
            if Battle_state_sprite.shake_power < 0:
                Battle_state_sprite.shake_flag = False

    def get_victory_flag(self):
        return self.victory_flag

    @staticmethod
    def set_shake(value):
        Battle_state_sprite.shake_flag = True
        Battle_state_sprite.shake_power = value
