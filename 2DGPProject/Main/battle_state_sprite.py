from hero import *
from font import *
from monster_in_battle import *
import winsound
import banner


class Battle_state_sprite:
    stage_image = None
    back_image = None
    info_image = None
    banner = None

    def __init__(self):
        self.hero = Hero_status()
        self.monster = Monsterstatus()
        self.victory_flag = 0
        self.font = font()
        self.vertexX = 0
        if Battle_state_sprite.stage_image is None:
            Battle_state_sprite.stage_image = load_image("../Resources/battle/battle_gameshow.png")
        if Battle_state_sprite.back_image is None:
            Battle_state_sprite.back_image = load_image("../Resources/battle/warrior_back.png")
        if Battle_state_sprite.banner is None:
            Battle_state_sprite.banner = banner.WinBanner()

        self.monstersprite = make_monster(self.hero.enemy_type)
        self.monster.set_status(self.monstersprite)

        Battle_state_sprite.banner.init()

    def draw(self):
        Battle_state_sprite.stage_image.draw(960, 540)
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
            if self.monster.hp <= 0:
                self.victory_flag = 1
                winsound.PlaySound('../Resources/battle/herowinsound.wav', winsound.SND_FILENAME | winsound.SND_NOWAIT | \
                                   winsound.SND_ASYNC)
            elif self.hero.get_hp() <= 0:
                self.victory_flag = 2

        if self.victory_flag == 3:
            Battle_state_sprite.banner.update()
        if self.victory_flag == 1:
            self.vertexX += 10

    def getvictory(self):
        return self.victory_flag

    def setdefeat(self):
        self.victory_flag = 4

    def setvictory(self):
        self.victory_flag = 3
