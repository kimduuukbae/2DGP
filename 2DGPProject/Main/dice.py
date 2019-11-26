import pico2d
import random

def collision(A, B):
    left_a, bottom_a, right_a, top_a = A.get_box()
    left_b, bottom_b, right_b, top_b = B.get_box()
    if left_a > right_b: return False
    if right_a < left_b: return False
    if top_a < bottom_b: return False
    if bottom_a > top_b: return False
    return True
def collisionMouse(mouse, A):
    left, bottom, right, top = A.get_box()
    if mouse[0] > left and mouse[0] < right and mouse[1] > bottom and mouse[1] < top:
        return True
    return False

class diceimage:
    dicelist = None
    def __init__(self):
        if diceimage.dicelist == None:
            diceimage.dicelist = []
            diceimage.dicelist.append(pico2d.load_image('../Resources/common/dice_1.png'))
            diceimage.dicelist.append(pico2d.load_image('../Resources/common/dice_2.png'))
            diceimage.dicelist.append(pico2d.load_image('../Resources/common/dice_3.png'))
            diceimage.dicelist.append(pico2d.load_image('../Resources/common/dice_4.png'))
            diceimage.dicelist.append(pico2d.load_image('../Resources/common/dice_5.png'))
            diceimage.dicelist.append(pico2d.load_image('../Resources/common/dice_6.png'))
    def getdice(self):
        temp = random.randint(0,5)
        return diceimage.dicelist[temp], temp+1

class dice():
    def __init__(self):
        self.dice, self.count = diceimage().getdice()
        self.x, self.y = 0,0
        self.used = False
        self.first = True
        self.index = 0
    def setPos(self,x, y):
        self.x = x
        self.y = y
    def draw(self):
        if not self.used:
            self.dice.draw(self.x, self.y)
    def get_box(self):
        return self.x - self.dice.w // 2, self.y - self.dice.h // 2, \
               self.x + self.dice.w // 2, self.y + self.dice.h // 2
    def get_count(self):
        return self.count
    def set_use(self):
        self.used = True
    def get_use(self):
        return self.used
    def redice(self):
        del self.dice
        self.dice, self.count = diceimage().getdice()
        self.setPos(1000 + (150 * self.index),-500)
        self.used = False
        self.first = True
        pass
    def update(self):
        if self.first:
            self.y += 10
            if self.y > 100:
                self.first = False
    def setindex(self, idx):
        self.index = idx
class diceManager:
    def __init__(self, num):
        self.dicelist = []
        for i in range(num):
            self.dicelist.append(dice())
            self.dicelist[i].setindex(i)

    def draw(self):
        for i in self.dicelist:
            i.draw()
    def setalldicepos(self,x , w):
        for i in range(len(self.dicelist)):
            self.dicelist[i].setPos(x + (i*w), -500)

    def update(self):
        for i in self.dicelist:
            i.update()
    def collideToObject(self, A):   # A must item
        for i in range(len(self.dicelist)):
            if not self.dicelist[i].get_use() and collision(A, self.dicelist[i]):
                A.active(self.dicelist[i])
                return True

    def collideToMouse(self, mouse):
        for i in range(len(self.dicelist)):
            if not self.dicelist[i].get_use() and collisionMouse(mouse, self.dicelist[i]):
                return i
        return None

    def getdicetoidx(self,idx):
        return self.dicelist[idx]
    def pushdice(self, num = 1 ,x = 1000, w = 150):
        leng = len(self.dicelist)
        for i in range(leng, leng+num):
            self.dicelist.append(dice())
            self.dicelist[i].setindex(i)
            self.dicelist[i].setPos(x + (i*w), -500)
    def clear(self):
        self.dicelist.clear()

