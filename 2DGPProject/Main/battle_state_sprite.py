from hero import *
from font import *
from monster_in_battle import *
import winsound
import banner
import main_state

class Battle_state_sprite:
    stage_image = []
    back_image = None
    info_image = None

    banner = None

    def __init__(self):
        self.hero = HeroStatus()
        self.monster = Monsterstatus()
        self.victory_flag = 0
        self.font = font()
        self.vertexX = 0
        self.time_to_banner = 0.0

        if len(Battle_state_sprite.stage_image) == 0:
            Battle_state_sprite.stage_image.append(load_image("../Resources/battle/battle_gameshow.png"))
            Battle_state_sprite.stage_image.append(load_image("../Resources/battle/battle_ice.png"))
        if Battle_state_sprite.back_image is None:
            Battle_state_sprite.back_image = load_image("../Resources/battle/warrior_back.png")
        if Battle_state_sprite.banner is None:
            Battle_state_sprite.banner = banner.WinBanner()

        self.monstersprite = make_monster(self.hero.enemy_type)
        self.monster.set_status(self.monstersprite)

        Battle_state_sprite.banner.init()

    def draw(self):
        Battle_state_sprite.stage_image[main_state.stage_collection.get_stage_idx()].draw(960, 540)
        Battle_state_sprite.back_image.draw(200, 170)

        self.hero.draw(600,100)
        self.font.draw(450,160,"전사",(255,255,255))
        if self.hero.shield == 0:
            self.font.draw(555, 102, str(self.hero.get_hp()) + ' / ' + str(self.hero.get_maxhp()), (255, 255, 255))
        else:
            self.font.draw(535, 102, str(self.hero.get_hp()) + ' / ' + str(self.hero.get_maxhp()) + ' + ' + str(self.hero.shield), (255, 255, 150))

        self.monster.draw(1400 + self.vertexX,800)
        self.font.draw(1250 + self.vertexX, 860, self.monster.name, (255, 255, 255))
        self.font.draw(1355 + self.vertexX, 802, str(self.monster.hp) + ' / ' + str(self.monster.max_hp), (255, 255, 255))

        self.monstersprite.draw(self.vertexX)

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

    def get_victory_flag(self):
        return self.victory_flag