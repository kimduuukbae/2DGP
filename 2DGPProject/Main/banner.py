from pico2d import *
import game_framework
class banner:
    image = None

    def __init__(self):
        if banner.image is None:
            banner.image = load_image("../Resources/stage/banner.png")
        self.x = 950
        self.y = 1400

        self.pivotX = 0
        self.pivotY = 0
    def draw(self):
        banner.image.draw(self.x, self.y, banner.image.w, banner.image.h)
        self.text.draw(self.x, self.y, self.text.w, self.text.h)
        self.sport.clip_draw(0, self.frame * self.clipSportY, self.clipSportX,
                                self.clipSportY, self.x + self.pivotX, self.y + self.pivotY, self.imageWidth, self.imageHeight)
    def update(self):
        self.time += game_framework.frame_time
        if self.time > 0.09:
            self.time = 0.0
            self.frame = (self.frame+1)%2
        if self.y > 600:
            self.y -= 10

class WinBanner(banner):
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



class BattleBanner(banner):
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