import pico2d
from object import *
import game_framework
import main_state
import banner
import winsound
from monster_type import monster_TYPE
class Monster_In_Menu(object):
    def __init__(self, name):
        super().__init__(None)
        self.type = monster_TYPE[name]
        self.frame = 0
        self.frameTime = 0.0
        self.battle = False
        self.battleOnce = False
        self.battleEffectFlag = False
        self.battleEffectSize = -1
        pass
    def getMonsterType(self):
        return self.type
    def draw(self):
        self.image.clip_draw(self.clipWidth*self.frame, 0, self.clipWidth, self.clipHeight,
                             self.x + self.pivotX, self.y + self.pivotY, self.imageWidth, self.imageHeight)
    def update(self):
        if self.battle:
            if not self.battleEffectFlag:
                self.x += 3
                self.battleEffectSize -= 2
                if self.battleEffectSize < -100:
                    self.battleEffectSize = -1
                    self.battleEffectFlag = True
            else:
                self.x -= 3
                self.battleEffectSize -= 2
                if self.battleEffectSize < -20:
                    self.battleEffectFlag = False
                    self.battle = False
                    main_state.bannerList.append(banner.BattleBanner())
                    winsound.PlaySound('../Resources/stage/fightfxSound.wav', winsound.SND_FILENAME | winsound.SND_NOWAIT | \
                       winsound.SND_ASYNC)
        self.frameTime += game_framework.frame_time
        if self.frameTime > 1.0:
            self.frame = (self.frame + 1)%2
            self.frameTime = 0.0

    def getBattle(self):
        return self.battleOnce
    def setBattle(self, flag):
        self.battleOnce = flag
        self.battle = flag

class fireman(Monster_In_Menu):
    def __init__(self):
        super().__init__("FIREMAN")
        self.image = pico2d.load_image("../Resources/stage/firemanStage.png")
        self.imageWidth = self.image.w
        self.imageHeight = self.image.h
        self.clipWidth = self.imageWidth // 2
        self.clipHeight = self.imageHeight
        self.id = 8
        self.pivotX = 0
        self.pivotY = 70
    def getId(self):
        return self.id


