from pico2d import *
import game_framework
class banner:
    image = None

    def __init__(self):
        if banner.image is None:
            banner.image = load_image("../Resources/stage/banner.png")
        self.x = 800
        self.y = 300

class WinBanner(banner):
    def __init__(self):
        super().__init__()
        self.wintext = load_image("../Resources/stage/winText.png")
        self.winSport = load_image("../Resources/stage/winSport.png")
        self.frame = 0

        self.imageWidth = self.winSport.w
        self.imageHeight = self.winSport.h // 2

        self.clipSportX = self.winSport.w
        self.clipSportY = self.winSport.h // 2

        self.time = 0.0

    def draw(self):
        banner.image.draw(self.x, self.y, banner.image.w, banner.image.h)
        self.wintext.draw(self.x, self.y, self.wintext.w, self.wintext.h)
        self.winSport.clip_draw(0, self.frame * self.clipSportY, self.clipSportX,
                                self.clipSportY, self.x + 10, self.y, self.imageWidth, self.imageHeight)
    def update(self):
        self.time += game_framework.frame_time
        if self.time > 0.1:
            self.time = 0.0
            self.frame = (self.frame+1)%2