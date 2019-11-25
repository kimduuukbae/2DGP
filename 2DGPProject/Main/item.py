from font import *
import pico2d
from monster_in_battle import monster_status
import game_framework
class item:
    volX = 30
    volY = 30
    collisionImage = None
    def __init__(self):
        self.namefont = font()
        self.itemName = None
        self.itemInfo = None
        self.image = None
        if item.collisionImage == None:
            item.collisionImage = pico2d.load_image('../Resources/common/itemcollisionbox.png')
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
    def draw(self):
        self.image.draw(self.x,self.y, self.imagewidth, self.imageheight)
        self.namefont.draw(self.x + self.pivotItemName,self.y + 120,self.itemName,(255,255,255))
        self.namefont.draw(self.x + self.pivotItemInfo,self.y - 100,self.itemInfo,(255,255,255))
        item.collisionImage.draw(self.x, self.y)
    def get_box(self):
        return self.x - item.collisionImage.w //2, self.y - item.collisionImage.h //2,\
               self.x + item.collisionImage.w //2, self.y + item.collisionImage.h //2

    def active(self, obj):
        pass
    def update(self):
        if self.turnFirst:
            self.x += 25
            if self.x > self.stopX:
                self.turnFirst = False
        if self.used and self.y < 1300:
            self.y += 50
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
        if self.exitturn:
            self.x -= 25
            if self.x < self.startX:
                self.exitturn = False
    def setexitturn(self):
        if not self.used:
            self.exitturn = True
    def first(self):
        self.x = self.startX
        self.used = False
        self.turnFirst = True
        self.y = 540
    def reuse(self):
        self.first()


class baseattack(item):
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
    def active(self, obj):
        self.used = True
        monster_status().addhp(-obj.get_count())
        obj.set_use()
        pass
class ironshield(item):
    def __init__(self):
        super().__init__()
        self.x = -500
        self.itemName = "철 방패"
        self.itemInfo = "□ 만큼 실드를 얻는다."
        self.image = pico2d.load_image('../Resources/common/small_orange.png')
        self.pivotItemName = -45
        self.pivotItemInfo = -140
        self.stopX = 900
        self.startX = -500
        self.imagewidth = self.image.w
        self.imageheight = self.image.h
    def active(self, obj):
        self.used = True
        obj.set_use()
        pass
class reloaddice(item):
    def __init__(self):
        super().__init__()
        self.x = -200
        self.count = 3
        self.itemName = "다시 굴리기"
        self.itemInfo = "주사위를 " + str(self.count) + "회 다시 굴린다."
        self.image = pico2d.load_image('../Resources/common/small_grey.png')
        self.pivotItemName = -75
        self.pivotItemInfo = -160
        self.stopX = 1400
        self.startX = -200
        self.imagewidth = self.image.w
        self.imageheight = self.image.h
    def active(self, obj):
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