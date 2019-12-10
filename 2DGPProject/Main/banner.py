from pico2d import *
import game_framework
import battle_state
import fadescene

class Banner:
    image = None
    background = None

    def __init__(self):
        if Banner.image is None:
            Banner.image = load_image("../Resources/stage/banner.png")
        if Banner.background is None:
            Banner.background = load_image("../Resources/stage/winbannerbackground.png")
        self.x = 950
        self.y = 2000

        self.pivotX = 0
        self.pivotY = 0

        self.changeTime = 0.0
        self.changeState = None

    def draw(self):
        Banner.background.draw(960, 540)
        Banner.image.draw(self.x, self.y, Banner.image.w, Banner.image.h)
        self.text.draw(self.x, self.y, self.text.w, self.text.h)
        self.sport.clip_draw(0, self.frame * self.clipSportY, self.clipSportX,
                                self.clipSportY, self.x + self.pivotX, self.y + self.pivotY, self.imageWidth, self.imageHeight)

    def update(self):
        self.time += game_framework.frame_time
        if self.time > 0.1:
            self.time = 0.0
            self.frame = (self.frame+1)%2
        if self.y > 600:
            self.y -= 10
        else:
            self.changeTime += game_framework.frame_time
            if self.changeTime > 2.0:
                self.change_scene()
                self.changeTime = 0.0

    def change_scene(self):
        pass

    def init(self):
        self.time = 0
        self.y = 2000
        self.changeTime = 0


class WinBanner(Banner):

    def __init__(self):
        super().__init__()

        self.text = load_image("../Resources/stage/winText.png")
        self.sport = load_image("../Resources/stage/winSport.png")
        self.frame = 0

        self.imageWidth = self.sport.w
        self.imageHeight = self.sport.h // 2

        self.clipSportX = self.sport.w
        self.clipSportY = self.sport.h // 2

        self.time = 0.0
        self.pivotX = 10

    def change_scene(self):
        fadescene.Fade.pop_state()


class BattleBanner(Banner):
    def __init__(self):
        super().__init__()
        self.text = load_image("../Resources/stage/battleText.png")
        self.sport = load_image("../Resources/stage/battleSport.png")
        self.frame = 0

        self.imageWidth = self.sport.w
        self.imageHeight = self.sport.h // 2

        self.clipSportX = self.sport.w
        self.clipSportY = self.sport.h // 2
        self.pivotX  = 10
        self.pivotY = 0
        self.time = 0.0

    def change_scene(self):
        fadescene.Fade.push_state(battle_state)
