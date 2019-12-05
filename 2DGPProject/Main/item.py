from font import *
import game_framework
from hero import *
from status_condition import *
ITEM_RULE = {'MAX': '최대', "BELOW": "이하", "ANY": "아무나", "COUNT": "합"}

class Item:
    volX = 30
    volY = 30
    collisionImage = None
    def __init__(self):
        self.namefont = font()
        self.itemName = None
        self.itemInfo = None
        self.image = None
        if Item.collisionImage == None:
            Item.collisionImage = pico2d.load_image('../Resources/common/itemcollisionbox.png')
        self.x = -100
        self.y = 540
        self.imagewidth = 0
        self.imageheight = 0
        self.pivotItemName = 0
        self.pivotItemInfo = 0
        self.turnFirst = True
        self.stopX = 0
        self.startX = 0
        self.used = False
        self.effect = False
        self.effecttime = 0.0
        self.effectdir = -1
        self.exitturn = False
        self.rule = None
        self.rule_count = 0

        self.dir = 1    # dir == 1 : hero, dir == -1 : monster

    def get_use(self):
        return self.used

    def draw(self):
        self.image.draw(self.x,self.y, self.imagewidth, self.imageheight)
        self.namefont.draw(self.x + self.pivotItemName,self.y + 120,self.itemName,(255,255,255))
        self.namefont.draw(self.x + self.pivotItemInfo,self.y - 100,self.itemInfo,(255,255,255))
        Item.collisionImage.draw(self.x, self.y)
        if self.rule is not 'ANY':
            self.namefont.draw(self.x - 30, self.y + 40, ITEM_RULE[self.rule], (255, 255, 255))
            self.namefont.draw(self.x - 10, self.y, str(self.rule_count), (255, 255, 255))

    def get_box(self):
        return self.x - Item.collisionImage.w // 2, self.y - Item.collisionImage.h // 2, \
               self.x + Item.collisionImage.w // 2, self.y + Item.collisionImage.h // 2

    def active(self, obj):
        pass

    def update(self):
        if self.dir == 1:
            if self.turnFirst:
                self.x += 25
                if self.x > self.stopX:
                    self.turnFirst = False
            if self.used and self.y < 1300:
                self.y += 50
            if self.exitturn:
                self.x -= 25
                if self.x < self.startX:
                    self.exitturn = False
        else:
            if self.turnFirst:
                self.x -= 25
                if self.x < self.stopX:
                    self.turnFirst = False
            if self.used and self.y > -200:
                self.y -= 50
            if self.exitturn:
                self.x += 25
                if self.x > self.startX:
                    self.exitturn = False
        if self.effect:
            self.effecttime += game_framework.frame_time
            self.imagewidth += self.effectdir * 3
            self.imageheight += self.effectdir * 3
            if self.effecttime > 0.1:
                if self.effectdir == -1:
                    self.effectdir = -self.effectdir
                else:
                    self.effectdir = -self.effectdir
                    self.effect = False
                self.effecttime = 0.0

    def set_exit_turn(self):
        if not self.used:
            self.exitturn = True

    def first(self):
        self.x = self.startX
        self.used = False
        self.turnFirst = True
        self.y = 540

    def reuse(self):
        self.first()

    def set_enemy_turn(self):
        self.dir = -1

    def setx(self,x1,x2):
        self.x = x1
        self.startX = x1
        self.stopX = x2

    def add_x_position(self, x):
        self.x += x

    def check_condition(self, object_dice):
        if self.rule == 'MAX':
            if object_dice.get_count() > self.rule_count:
                return False
        elif self.rule == 'BELOW':
            if object_dice.get_count() > self.rule_count:
                return False

        return True

    def get_position(self):
        return self.x, self.y

class BaseAttack(Item):
    def __init__(self):
        super().__init__()
        self.x = -800
        self.itemName = "기본 공격"
        self.itemInfo = "□ 만큼 데미지를 입힌다."
        self.image = pico2d.load_image('../Resources/common/small_blue.png')
        self.pivotItemName = -60
        self.pivotItemInfo = -145
        self.stopX = 400
        self.startX = -800
        self.imagewidth = self.image.w
        self.imageheight = self.image.h
        self.rule = 'ANY'

    def active(self, obj, status):
        self.used = True
        status.add_hp(-obj.get_count())
        obj.set_use()


class IronShield(Item):
    def __init__(self):
        super().__init__()
        self.itemName = "철 방패"
        self.itemInfo = "□ 만큼 실드를 얻는다."
        self.image = pico2d.load_image('../Resources/common/small_orange.png')
        self.pivotItemName = -45
        self.pivotItemInfo = -140
        self.imagewidth = self.image.w
        self.imageheight = self.image.h
        self.rule = 'MAX'
        self.rule_count = 4

    def active(self, obj, status):
        self.used = True
        obj.set_use()
        HeroStatus.add_shield(obj.get_count())


class ReloadDice(Item):
    def __init__(self):
        super().__init__()
        self.count = 3
        self.itemName = "다시 굴리기"
        self.itemInfo = "주사위를 " + str(self.count) + "회 다시 굴린다."
        self.image = pico2d.load_image('../Resources/common/small_grey.png')
        self.pivotItemName = -75
        self.pivotItemInfo = -160
        self.imagewidth = self.image.w
        self.imageheight = self.image.h
        self.rule = 'ANY'

    def active(self, obj, status):
        obj.set_use()
        obj.redice()
        self.count = self.count - 1
        self.itemInfo = "주사위를 " + str(self.count) + "회 다시 굴린다."
        self.effect = True
        if self.count == 0:
            self.used = True

    def first(self):
        super().first()
        self.count = 3
        self.itemInfo = "주사위를 " + str(self.count) + "회 다시 굴린다."

class Poison(Item):
    def __init__(self):
        super().__init__()
        self.itemName = "중독"
        self.itemInfo = "2의 독을 가한다."
        self.image = pico2d.load_image('../Resources/common/small_purple.png')
        self.pivotItemName = -32
        self.pivotItemInfo = -100
        self.imagewidth = self.image.w
        self.imageheight = self.image.h
        self.rule = 'ANY'

    def active(self, obj, status):
        self.used = True
        status.get_condition().add_condition("독", 2)
        obj.set_use()

class InkAttack(Item):
    def __init__(self):
        super().__init__()
        self.itemName = "먹물 공격"
        self.itemInfo = "1의 독과 데미지를 입힌다."
        self.image = pico2d.load_image('../Resources/common/small_purple.png')
        self.pivotItemName = -60
        self.pivotItemInfo = -155
        self.imagewidth = self.image.w
        self.imageheight = self.image.h
        self.rule = 'BELOW'
        self.rule_count = 3

    def active(self, obj, status):
        self.used = True
        status.add_hp(-status.min_shield(1))
        status.get_condition().add_condition("독", 1)
        obj.set_use()


ITEM_LIST = {"baseattack" : BaseAttack, "reloaddice" : ReloadDice, "ironshield" : IronShield, "poison" : Poison,
             "inkattack" : InkAttack}


def itemfactory(name):
    return ITEM_LIST[name]()

class item_manager:
    def __init__(self, type):
        self.itemlist = []
        self.startX = 0
        self.stopX = 0
        self.x = 0
        self.type = type
        if type == "hero":
            self.startX = -200
            self.x = self.startX
            self.stopX = 400
        else:
            self.startX = 2100
            self.x = self.startX
            self.stopX = 1440

    def push_item(self, itemname):
        self.itemlist.append(itemfactory(itemname))
        if self.type == "hero":
            self.itemlist[-1].setx(self.startX, self.stopX + ((len(self.itemlist)-1)*500))
        else:
            self.itemlist[-1].setx(self.startX, self.stopX - ((len(self.itemlist) - 1) * 500))
            self.itemlist[-1].set_enemy_turn()

    def push_item_list(self, item_list):
        for i in item_list:
            self.itemlist.append(itemfactory(i))

            if self.type == "hero":
                self.itemlist[-1].setx(self.startX, self.stopX + ((len(self.itemlist) - 1) * 500))
            else:
                self.itemlist[-1].setx(self.startX, self.stopX - ((len(self.itemlist) - 1) * 500))
                self.itemlist[-1].set_enemy_turn()

    def draw(self):
        for i in self.itemlist:
            i.draw()

    def getlist(self):
        return self.itemlist

    def update(self):
        for i in self.itemlist:
            i.update()

    def changeturn(self):
        for i in self.itemlist:
            i.set_exit_turn()

    def item_clear(self):
        self.itemlist.clear()



