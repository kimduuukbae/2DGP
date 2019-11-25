from object import *
import pico2d

class hero(object):
    def __init__(self, imageString = None):
        super().__init__(imageString)
        self.id = 1
        self.moveFlag = False
        self.name = "전사"

        self.toX = 0
        self.toY = 0

        self.distanceX = 0
        self.distanceY = 0

        self.count = 0

        self.battle = False
        self.battleEffectFlag = False
        self.battleEffectSize = -1
    def update(self):
        if self.battle:
            if not self.battleEffectFlag:
                self.x -= 3
                self.battleEffectSize -= 2
                if self.battleEffectSize < -100:
                    self.battleEffectSize = -1
                    self.battleEffectFlag = True
            else:
                self.x += 2
                self.battleEffectSize -= 2
                if self.battleEffectSize < -20:
                    self.battleEffectFlag = False
                    self.battle = False
        if self.moveFlag:
            self.x += self.distanceX
            self.y += self.distanceY
            self.count += 1
            if self.count == 100:
                self.count = 0
                self.id = self.moveLists[0][2]
                self.moveFlag = False
                self.moveLists.pop(0)
                if len(self.moveLists):
                    self.moveTo(self.moveLists)

    def getHeroId(self):
        return self.id
    def moveTo(self,list):
        if not self.moveFlag:
            self.moveLists = list
            self.toX = self.moveLists[0][0]
            self.toY = self.moveLists[0][1]
            self.distanceX = (self.toX - self.x) / 100
            self.distanceY = (self.toY - self.y) / 100
            self.moveFlag = True

    def getMoving(self):
        return self.moveFlag
    def getBattle(self):
        return self.battle
    def setBattle(self, flag):
        self.battle = flag
    def addX(self, value):
        self.x += value

class hero_status:
    hp = 24
    maxhp = 24  # 24 = 6 28 = 5.5 32 = 5
    pivot = 6
    backimg = None
    img = None
    enemytype = None
    def __init__(self):
        if hero_status.backimg == None and hero_status.img == None:
            hero_status.backimg = pico2d.load_image("../Resources/common/hpbarback.png")
            hero_status.img = pico2d.load_image("../Resources/common/hpbar.png")
    def gethp(self):
        return hero_status.hp
    def sethp(self, hp):
        hero_status.hp = hp
    def setmaxhp(self, hp):
        hero_status.maxhp = hp
        hero_status.pivot -= 0.5
    def getmaxhp(self):
        return hero_status.maxhp
    def draw(self,x,y):
        hero_status.backimg.draw(x, y)
        hero_status.img.draw(x - int((hero_status.maxhp - hero_status.hp) * hero_status.pivot), y,\
                                  hero_status.img.w - (int((hero_status.img.w / hero_status.maxhp) * (hero_status.maxhp - hero_status.hp)) ),\
                                  hero_status.img.h)
    def addhp(self, value):
        hero_status.hp += value
    def setEnemyType(self, type):
        hero_status.enemytype = type