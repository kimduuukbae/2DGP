from font import *
import pico2d

class item:
    volX = 30
    volY = 30
    def __init__(self):
        self.namefont = font()
        self.itemName = None
        self.itemInfo = None
        self.image = None
        self.x = 960
        self.y = 400
        self.pivotX = 0
        self.pivotY = 0
    def draw(self):
        self.image.draw(self.x,self.y)
        self.namefont.draw(self.x - 30,self.y + 150,self.itemName,(255,255,255))
        self.namefont.draw(self.x,self.y - 100,self.itemInfo,(255,255,255))
    def active(self):
        pass
    def collision(self):
        pass

class ironshield(item):
    def __init__(self):
        super().__init__()
        self.itemName = "철 방패"
        self.itemInfo = "□ 실드를 추가한다."
        self.image = pico2d.load_image('../Resources/battle/small_orange.png')

class reloaddice(item):
    def __init__(self):
        super().__init__()
        self.count = 3
        self.itemName = "다시 굴리기"
        self.itemInfo = "주사위를" + str(self.count) + "회 다시 굴립니다."
    def active(self):
        self.count = self.count - 1