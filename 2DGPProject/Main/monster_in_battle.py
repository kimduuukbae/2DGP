from object import *
import game_framework
from status_condition import *
import random
from sound_manager import *


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
        self.num_dice = 0
        self.hp = 0
        self.pivot = 0
        self.item_list = None
        self.effectsound = None

    def get_numeric_dice(self):
        return self.num_dice

    def get_hp(self):
        return self.hp

    def get_name(self):
        return self.type

    def get_pivot(self):
        return self.pivot

    def get_item_list(self):
        return self.item_list

    def get_sound(self):
        return self.effectsound

    def play_sound(self, value):
        if -value > 4:
            SoundManager.play_sound("hdamage", False)
        SoundManager.play_sound("Defense", False)



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
        self.num_dice = 2
        self.info = "슬라임은 기본 공격에 약합니다."

        SoundManager.add_effect_sound("../Resources/sound/effect/slime_attack.wav", "Attack")
        SoundManager.add_effect_sound("../Resources/sound/effect/slime_defense.wav", "Defense")

        self.item_list = ["poison", "poison", "poison"]

    def update(self):
        self.frameTime += game_framework.frame_time
        if self.frameTime > 0.2:
            self.frameTime = 0.0
            self.frame = (self.frame + 1)%10

    def draw(self, x=0, y=0):
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
        self.num_dice = 3
        self.info = "새끼오징어는 기본 공격에 약합니다."

        self.item_list = ["poison", "inkattack", "inkattack"]

        SoundManager.add_effect_sound("../Resources/sound/effect/baby_attack.wav", "Attack")
        SoundManager.add_effect_sound("../Resources/sound/effect/baby_defense.wav", "Defense")

    def update(self):
        self.frameTime += game_framework.frame_time
        if self.frameTime > 0.1:
            self.frameTime = 0.0
            self.frame = (self.frame + 1)%10

    def draw(self, x=0, y=0):
        self.image.clip_draw(self.frame % 5 * self.imageWidth,(1 - (self.frame // 5)) * self.imageHeight,
                             self.clipWidth, self.clipHeight, self.x + x, self.y + y, self.imageWidth, self.imageHeight)


class MashMellow(Inbattlemonster):
    def __init__(self):
        super().__init__("마시멜로우")
        self.image = pico2d.load_image('../Resources/battle/mashmallowAtlas.png')
        self.imageWidth = self.image.w // 6
        self.imageHeight = self.image.h
        self.clipWidth = self.imageWidth
        self.clipHeight = self.imageHeight
        self.hp = 13
        self.pivot = 11
        self.num_dice = 2
        self.info = "새끼오징어는 기본 공격에 약합니다."

        self.item_list = ["snowball", "fireball"]

        SoundManager.add_effect_sound("../Resources/sound/effect/marshmallow_attack.wav", "Attack")
        SoundManager.add_effect_sound("../Resources/sound/effect/marshmallow_defense.wav", "Defense")

    def update(self):
        self.frameTime += game_framework.frame_time
        if self.frameTime > 0.1:
            self.frameTime = 0.0
            self.frame = (self.frame + 1) % 6

    def draw(self, x=0, y=0):
        self.image.clip_draw((self.frame % 6) * self.imageWidth, 0,
                             self.clipWidth, self.clipHeight, self.x + x, self.y + y, self.imageWidth, self.imageHeight)



class FinaleBoss(Inbattlemonster):
    def __init__(self):
        super().__init__("행운의여왕")
        self.image = pico2d.load_image('../Resources/battle/ladyluck_mouse_animation.png')
        self.imageWidth = self.image.w // 5
        self.imageHeight = self.image.h
        self.clipWidth = self.imageWidth
        self.clipHeight = self.imageHeight
        self.x = 1250
        self.y = 1160
        self.hp = 45
        self.pivot = 3.3
        self.num_dice = 1
        self.info = "행운의 여왕은 장비를 계속 변경합니다."
        self.page = 1
        self.item_list = []
        self.random_item = ["verdict1", "verdict2", "verdict3"]

        SoundManager.add_effect_sound('../Resources/sound/effect/ladyluckattack.wav', "Attack")
        SoundManager.add_effect_sound("../Resources/sound/effect/ladyluckdefence.wav", "Defense")
        SoundManager.add_effect_sound('../Resources/sound/effect/ladyluckattack_h.wav', "AttackH")
        SoundManager.add_effect_sound("../Resources/sound/effect/ladyluckdefence_h.wav", "DefenseH")

    def update(self):
        self.frameTime += game_framework.frame_time
        if self.frameTime > 0.1:
            self.frameTime = 0.0
            self.frame = (self.frame + 1) % 5

    def draw(self, x=0, y=0):
        self.image.clip_composite_draw(self.frame * self.imageWidth, 0,
                             self.clipWidth, self.clipHeight, -0.2, 'a',  self.x + x, self.y - y, self.imageWidth,
                             self.imageHeight)

    def change_item(self):
        if self.page == 1:
            self.item_list.clear()
            self.item_list.append(self.random_item[random.randint(0, 2)])
        else:
            self.item_list.clear()
            for i in self.random_item:
                self.item_list.append(i)

    def change_page(self):
        self.page = 2
        self.num_dice = 3

    def get_page(self):
        return self.page

    def play_sound(self, value):
        if -value < 4:
            SoundManager.play_sound("Defense", False)
        else:
            SoundManager.play_sound("DefenseH", False)
            SoundManager.play_sound("hdamage", False)



MONSTER_LIST = {"슬라임" : Slime, "새끼오징어" : BabySquid, "행운의여왕": FinaleBoss, "마시멜로우": MashMellow}


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
    save_obj = None
    m_status_conditon = StatusCondition()

    def __init__(self):
        if Monsterstatus.background_image is None and Monsterstatus.img is None:
            Monsterstatus.background_image = pico2d.load_image("../Resources/common/hpbarback.png")
            Monsterstatus.img = pico2d.load_image("../Resources/common/hpbar.png")

    @staticmethod
    def get_condition():
        return Monsterstatus.m_status_condition

    @staticmethod
    def set_status(obj):
        Monsterstatus.hp = obj.get_hp()
        Monsterstatus.max_hp = obj.get_hp()
        Monsterstatus.name = obj.get_name()
        Monsterstatus.pivot = obj.get_pivot()
        if Monsterstatus.save_obj is not None:
            del Monsterstatus.save_obj

        Monsterstatus.save_obj = obj
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
        if value < 0:
            Monsterstatus.save_obj.play_sound(value)
        if -value < 4:
            SoundManager.play_sound("hdamage", False)

    @staticmethod
    def change_item():
        Monsterstatus.item_list.clear()
        Monsterstatus.save_obj.change_item()
        Monsterstatus.item_list = Monsterstatus.save_obj.get_item_list()



