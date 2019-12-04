from object import *
import game_framework


class Inbattlemonster(Object):
    def __init__(self, name):
        super().__init__(None)
        self.type = name
        self.frame = 0
        self.frameTime = 0.0
        self.imageWidth = 0
        self.imageHeight = 0
        self.x = 1700
        self.y = 800
        self.hp = 0
        self.pivot = 0
        self.item_list = None

    def get_hp(self):
        return self.hp

    def get_name(self):
        return self.type

    def get_pivot(self):
        return self.pivot

    def get_item_list(self):
        return self.item_list


class Slime(Inbattlemonster):
    def __init__(self):
        super().__init__("슬라임")
        self.image = pico2d.load_image('../Resources/battle/slimeAtlas.png')
        self.imageWidth = self.image.w // 5
        self.imageHeight = self.image.h // 2
        self.clipWidth = self.imageWidth
        self.clipHeight = self.imageHeight
        self.hp = 10
        self.pivot = 14.5
        self.info = "슬라임은 기본 공격에 약합니다."

        self.item_list = ["poison", "poison", "poison"]

    def update(self):
        self.frameTime += game_framework.frame_time
        if self.frameTime > 0.2:
            self.frameTime = 0.0
            self.frame = (self.frame + 1)%10

    def draw(self, x = 0, y = 0):
        self.image.clip_draw(self.frame % 5 * self.imageWidth,(1 - (self.frame // 5)) * self.imageHeight,
                             self.clipWidth, self.clipHeight, self.x + x, self.y + y, self.imageWidth, self.imageHeight)

class BabySquid(Inbattlemonster):
    def __init__(self):
        super().__init__("새끼오징어")
        self.image = pico2d.load_image('../Resources/battle/babysquidAtlas.png')
        self.imageWidth = self.image.w // 5
        self.imageHeight = self.image.h // 2
        self.clipWidth = self.imageWidth
        self.clipHeight = self.imageHeight
        self.hp = 15
        self.pivot = 10
        self.info = "새끼오징어는 기본 공격에 약합니다."

        self.item_list = ["poison", "inkattack", "inkattack"]

    def update(self):
        self.frameTime += game_framework.frame_time
        if self.frameTime > 0.1:
            self.frameTime = 0.0
            self.frame = (self.frame + 1)%10

    def draw(self, x=0, y=0):
        self.image.clip_draw(self.frame % 5 * self.imageWidth,(1 - (self.frame // 5)) * self.imageHeight,
                             self.clipWidth, self.clipHeight, self.x + x, self.y + y, self.imageWidth, self.imageHeight)


MONSTER_LIST = {"슬라임" : Slime, "새끼오징어" : BabySquid }


def make_monster(monster_type):
    return MONSTER_LIST[monster_type]()


class Monsterstatus:
    hp = 0
    max_hp = 0
    pivot = 0
    background_image = None
    img = None
    name = None
    item_list = None

    def __init__(self):
        if Monsterstatus.background_image is None and Monsterstatus.img is None:
            Monsterstatus.background_image = pico2d.load_image("../Resources/common/hpbarback.png")
            Monsterstatus.img = pico2d.load_image("../Resources/common/hpbar.png")


    @staticmethod
    def set_status(obj):
        Monsterstatus.hp = obj.get_hp()
        Monsterstatus.max_hp = obj.get_hp()
        Monsterstatus.name = obj.get_name()
        Monsterstatus.pivot = obj.get_pivot()
        Monsterstatus.item_list = obj.get_item_list()

    @staticmethod
    def draw(x, y):
        Monsterstatus.background_image.draw(x, y)

        Monsterstatus.img.draw(x - int((Monsterstatus.max_hp - Monsterstatus.hp) * Monsterstatus.pivot), y, \
                               Monsterstatus.img.w - (
                                 int((Monsterstatus.img.w / Monsterstatus.max_hp) * (Monsterstatus.max_hp - Monsterstatus.hp))), \
                               Monsterstatus.img.h)

    @staticmethod
    def add_hp(value):
        Monsterstatus.hp += value


