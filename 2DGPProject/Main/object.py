import pico2d

class object:
    def __init__(self, imageString):
        self.image = pico2d.load_image(imageString)
        self.x = 0
        self.y = 0
        self.w = 0
        self.h = 0
        self.sw = self.image.w
        self.sh = self.image.h
        self.rad = 0
        self.rotateFlag = True
        self.left = 0
        self.bottom = 0
    def update(self):
        pass
    def draw(self):
        self.image.draw(self.x, self.y, self.sw, self.sh)
    def clip_draw(self):
        self.image.clip_draw(self.left,self.bottom,self.w, self.h, self.x, self.y, self.sw, self.sh)
    def rotate_draw(self):
        self.image.rotate_draw(self.rad, self.x, self.y, self.sw, self.sh)
    def setPos(self, x, y):
        self.x = x
        self.y = y
    def setSize(self, w, h):
        self.sw = w
        self.sh = h
    def setClipSize(self, w, h):
        self.w = w
        self.h = h
    def setRotateFlag(self, flag):
        self.rotateFlag = flag
    def changeClipFrame(self, left, bottom):
        self.left = left
        self.bottom = bottom

