from hero import *
from font import *
from monster_in_battle import *
import banner
class battle_state_spritelist:
    stage_image = None
    back_image = None
    info_image = None
    banner = None
    def __init__(self):
        self.hero = hero_status()
        self.monster = monster_status()
        self.victory = 0
        self.font = font()
        self.vertexX = 0
        if battle_state_spritelist.stage_image == None:
            battle_state_spritelist.stage_image = load_image("../Resources/battle/battle_gameshow.png")
        if battle_state_spritelist.back_image == None:
            battle_state_spritelist.back_image = load_image("../Resources/battle/warrior_back.png")
        if battle_state_spritelist.banner == None:
            battle_state_spritelist.banner = banner.WinBanner()

        self.monstersprite = monsterFactory(self.hero.enemytype)
        self.monster.setstatus(self.monstersprite)

        battle_state_spritelist.banner.init()
    def draw(self):
        battle_state_spritelist.stage_image.draw(960,540)
        battle_state_spritelist.back_image.draw(200,170)

        self.hero.draw(600,100)
        self.font.draw(450,160,"전사",(255,255,255))
        self.font.draw(555,102,str(self.hero.gethp()) +' / ' + str(self.hero.getmaxhp()), (255,255,255))

        self.monster.draw(1400 + self.vertexX,800)
        self.font.draw(1250 + self.vertexX, 860, self.monster.name, (255, 255, 255))
        self.font.draw(1355 + self.vertexX, 802, str(self.monster.hp) + ' / ' + str(self.monster.maxhp), (255, 255, 255))

        self.monstersprite.draw(self.vertexX)

        if self.victory == 3:
            battle_state_spritelist.banner.draw()

    def update(self):
        self.monstersprite.update()
        if self.victory == 0:
            if self.monster.hp <= 0:
                self.victory = 1
            elif self.hero.gethp() <= 0:
                self.victory = 2

        if self.victory == 3:
            battle_state_spritelist.banner.update()
        if self.victory == 1:
            self.vertexX += 10

    def getvictory(self):
        return self.victory
    def setdefeat(self):
        self.victory = 4
    def setvictory(self):
        self.victory = 3