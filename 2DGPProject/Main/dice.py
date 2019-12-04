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


def collide_item_and_mouse(mouse, A):
    left, bottom, right, top = A.get_box()
    if mouse[0] > left and mouse[0] < right and mouse[1] > bottom and mouse[1] < top:
        return True
    return False


class Dice_image:
    dicelist = None

    def __init__(self):
        if Dice_image.dicelist is None:
            Dice_image.dicelist = []
            Dice_image.dicelist.append(pico2d.load_image('../Resources/common/dice_1.png'))
            Dice_image.dicelist.append(pico2d.load_image('../Resources/common/dice_2.png'))
            Dice_image.dicelist.append(pico2d.load_image('../Resources/common/dice_3.png'))
            Dice_image.dicelist.append(pico2d.load_image('../Resources/common/dice_4.png'))
            Dice_image.dicelist.append(pico2d.load_image('../Resources/common/dice_5.png'))
            Dice_image.dicelist.append(pico2d.load_image('../Resources/common/dice_6.png'))

    @staticmethod
    def get_dice():
        temp = random.randint(1, 5)
        return Dice_image.dicelist[temp], temp + 1


class Dice:
    def __init__(self):
        self.dice, self.count = Dice_image().get_dice()
        self.x, self.y = 0,0
        self.used = False
        self.first = True
        self.index = 0

    def set_position(self, x, y):
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
        self.dice, self.count = Dice_image().get_dice()
        self.set_position(1000 + (150 * self.index), -500)
        self.used = False
        self.first = True

    def update(self):
        if self.first:
            if self.y > 500:
                self.y -= 10
                if self.y < 1000:
                    self.first = False
            else:
                self.y += 10
                if self.y > 100:
                    self.first = False



    def set_index(self, idx):
        self.index = idx

class Dice_manager:
    def __init__(self, num):
        self.dicelist = []
        for i in range(num):
            self.dicelist.append(Dice())
            self.dicelist[i].set_index(i)

    def draw(self):
        for i in self.dicelist:
            i.draw()

    def set_all_dice_pos(self, x, w):
        for i in range(len(self.dicelist)):
            self.dicelist[i].set_position(x + (i * w), -500)

    def update(self):
        for i in self.dicelist:
            i.update()

    def collide_to_object(self, A):   # A must item
        for i in range(len(self.dicelist)):
            if not self.dicelist[i].get_use() and collision(A, self.dicelist[i]):
                A.active(self.dicelist[i])
                return True

    def collide_to_mouse(self, mouse):
        for i in range(len(self.dicelist)):
            if not self.dicelist[i].get_use() and collide_item_and_mouse(mouse, self.dicelist[i]):
                return i
        return None

    def get_dice_to_idx(self, idx):
        return self.dicelist[idx]

    def push_dice(self, num = 1, x = 1000, w = 150):
        leng = len(self.dicelist)
        for i in range(leng, leng+num):
            self.dicelist.append(Dice())
            self.dicelist[i].set_index(i)
            self.dicelist[i].set_position(x + (i * w), -500)

    def push_dice_monster(self, num = 1, x = 1000, w = 150):
        leng = len(self.dicelist)
        for i in range(leng, leng + num):
            self.dicelist.append(Dice())
            self.dicelist[i].set_index(i)
            self.dicelist[i].set_position(x + (i * w), 1500)

    def dice_clear(self):
        self.dicelist.clear()

