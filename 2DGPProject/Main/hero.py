from object import *
import pico2d

class hero(Object):
    def __init__(self, image_name = None):
        super().__init__(image_name)
        self.id = 1
        self.moveFlag = False
        self.name = "전사"

        self.toX = 0
        self.toY = 0

        self.distanceX = 0
        self.distanceY = 0

        self.count = 0

        self.battle = False
        self.battleEffectFlag = False
        self.battleEffectSize = -1

        self.moveLists = []

    def update(self):
        if self.battle:
            if not self.battleEffectFlag:
                self.x -= 3
                self.battleEffectSize -= 2
                if self.battleEffectSize < -100:
                    self.battleEffectSize = -1
                    self.battleEffectFlag = True
            else:
                self.x += 2
                self.battleEffectSize -= 2
                if self.battleEffectSize < -20:
                    self.battleEffectFlag = False
                    self.battle = False
        if self.moveFlag:
            self.x += self.distanceX
            self.y += self.distanceY
            self.count += 1
            if self.count == 100:
                self.count = 0
                self.id = self.moveLists[0][2]
                self.moveFlag = False
                self.moveLists.pop(0)
                if len(self.moveLists):
                    self.move_to_tile(self.moveLists)

    def get_id(self):
        return self.id

    def move_to_tile(self, lists):
        if not self.moveFlag:
            self.moveLists = lists
            self.toX = self.moveLists[0][0]
            self.toY = self.moveLists[0][1]
            self.distanceX = (self.toX - self.x) / 100
            self.distanceY = (self.toY - self.y) / 100
            self.moveFlag = True

    def get_moving(self):
        return self.moveFlag

    def get_in_battle(self):
        return self.battle

    def set_in_battle(self, flag):
        self.battle = flag

    def add_position_x(self, value):
        self.x += value


class Hero_status:
    hp = 24
    maxhp = 24  # 24 = 6 28 = 5.5 32 = 5
    pivot = 6
    shield = 0
    background_image = None
    img = None
    enemy_type = None

    def __init__(self):
        if Hero_status.background_image is None and Hero_status.img is None:
            Hero_status.background_image = pico2d.load_image("../Resources/common/hpbarback.png")
            Hero_status.img = pico2d.load_image("../Resources/common/hpbar.png")

    @staticmethod
    def get_hp():
        return Hero_status.hp

    @staticmethod
    def set_hp(hp):
        Hero_status.hp = hp

    @staticmethod
    def set_maxhp(hp):
        Hero_status.maxhp = hp
        Hero_status.pivot -= 0.5

    @staticmethod
    def get_maxhp():
        return Hero_status.maxhp

    @staticmethod
    def draw(x, y):
        Hero_status.background_image.draw(x, y)
        Hero_status.img.draw(x - int((Hero_status.maxhp - Hero_status.hp) * Hero_status.pivot), y, \
                             Hero_status.img.w - (int((Hero_status.img.w / Hero_status.maxhp) * (Hero_status.maxhp - Hero_status.hp))), \
                             Hero_status.img.h)

    @staticmethod
    def add_hp(value):
        Hero_status.hp += value

    @staticmethod
    def add_shield(value):
        Hero_status.shield += value

    @staticmethod
    def set_enemy_type(enemytype):
        Hero_status.enemy_type = enemytype
