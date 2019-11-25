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
    def setPos(self,x, y):
        self.x = x
        self.y = y
    def draw(self):
        self.dice.draw(self.x, self.y)
    def get_box(self):
        return self.x - self.dice.w // 2, self.y - self.dice.h // 2, \
               self.x + self.dice.w // 2, self.y + self.dice.h // 2
    def get_count(self):
        return self.count
class diceManager:
    def __init__(self, num):
        self.dicelist = [dice() for i in range(num)]

    def draw(self):
        for i in self.dicelist:
            i.draw()
            x1, y1, x2, y2 = i.get_box()
            pico2d.draw_rectangle(x1, y1, x2, y2)
    def setalldicepos(self,x ,y, w):
        for i in range(len(self.dicelist)):
            self.dicelist[i].setPos(x + (i*w), y)

    def update(self):
        pass
    def collideToObject(self, A):   # A must item
        for i in range(len(self.dicelist)):
            if collision(A, self.dicelist[i]):
                return True

    def collideToMouse(self, mouse):
        for i in range(len(self.dicelist)):
            if collisionMouse(mouse, self.dicelist[i]):
                return i
        return None
    def getdicetoidx(self,idx):
        return self.dicelist[idx]

