from object import *
import game_framework

class Monster_In_Battle(object):
    def __init__(self, name):
        super().__init__(None)
        self.type = name
        self.frame = 0
        self.frameTime = 0.0
        self.imageWidth = 0
        self.imageHeight = 0
        self.hp = 0

    def gethp(self):
        return self.hp
    def getname(self):
        return self.type

class slime(Monster_In_Battle):
    def __init__(self):
        super().__init__("슬라임")
        self.image = pico2d.load_image('../Resources/battle/slimeAtlas.png')
        self.imageWidth = self.image.w // 5
        self.imageHeight = self.image.h // 2
        self.clipWidth = self.imageWidth
        self.clipHeight = self.imageHeight
        self.x = 1700
        self.y = 800
        self.hp = 10
        self.info = "슬라임은 기본 공격에 약합니다."
    def update(self):
        self.frameTime += game_framework.frame_time
        if self.frameTime > 0.2:
            self.frameTime = 0.0
            self.frame = (self.frame + 1)%10
    def draw(self):
        self.image.clip_draw(self.frame % 5 * self.imageWidth,(1 - (self.frame // 5)) * self.imageHeight,
                             self.clipWidth, self.clipHeight, self.x, self.y, self.imageWidth, self.imageHeight)


def monsterFactory(type):
    temp = None
    if type == "슬라임":
        temp = slime()
    return temp

class monster_status:
    hp = 0
    maxhp = 0
    backimg = None
    img = None
    name = None
    def __init__(self):
        if monster_status.backimg == None and monster_status.img == None:
            monster_status.backimg = pico2d.load_image("../Resources/common/hpbarback.png")
            monster_status.img = pico2d.load_image("../Resources/common/hpbar.png")
    def setstatus(self, obj):
        monster_status.hp = obj.gethp()
        monster_status.maxhp = obj.gethp()
        monster_status.name = obj.getname()
    def draw(self,x,y):
        monster_status.backimg.draw(x, y)

        monster_status.img.draw(x - int((monster_status.maxhp - monster_status.hp) * 6), y, \
                             monster_status.img.w - (
                                 int((monster_status.img.w / monster_status.maxhp) * (monster_status.maxhp - monster_status.hp))), \
                             monster_status.img.h)