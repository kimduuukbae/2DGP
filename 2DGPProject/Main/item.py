from font import *
import pico2d

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
        self.pivotItemName = 0
        self.pivotItemInfo = 0
        self.turnFirst = True
        self.stopX = 0
    def draw(self):
        self.image.draw(self.x,self.y)
        self.namefont.draw(self.x + self.pivotItemName,self.y + 120,self.itemName,(255,255,255))
        self.namefont.draw(self.x + self.pivotItemInfo,self.y - 100,self.itemInfo,(255,255,255))
        item.collisionImage.draw(self.x, self.y)
    def get_box(self):
        return self.x - item.collisionImage.w //2, self.y - item.collisionImage.h //2,\
               self.x + item.collisionImage.w //2, self.y + item.collisionImage.h //2

    def active(self):
        pass
    def update(self):
        if self.turnFirst:
            self.x += 25
            if self.x > self.stopX:
                self.turnFirst = False


class baseattack(item):
    def __init__(self):
        super().__init__()
        self.x = -700
        self.itemName = "기본 공격"
        self.itemInfo = "□ 만큼 데미지를 입힌다."
        self.image = pico2d.load_image('../Resources/common/small_blue.png')
        self.pivotItemName = -60
        self.pivotItemInfo = -145
        self.stopX = 400
class ironshield(item):
    def __init__(self):
        super().__init__()
        self.x = -400
        self.itemName = "철 방패"
        self.itemInfo = "□ 실드를 추가한다."
        self.image = pico2d.load_image('../Resources/common/small_orange.png')
        self.pivotItemName = -45
        self.pivotItemInfo = -120
        self.stopX = 900
    def active(self):
        pass
class reloaddice(item):
    def __init__(self):
        super().__init__()
        self.x = -100
        self.count = 3
        self.itemName = "다시 굴리기"
        self.itemInfo = "주사위를 " + str(self.count) + "회 다시 굴린다."
        self.image = pico2d.load_image('../Resources/common/small_grey.png')
        self.pivotItemName = -75
        self.pivotItemInfo = -160
        self.stopX = 1400
    def active(self):
        self.count = self.count - 1