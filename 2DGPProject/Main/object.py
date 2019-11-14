import pico2d

class object:
    def __init__(self, imageString = None):
        self.image = None
        if imageString is not None:
            self.image = pico2d.load_image(imageString)
            self.imageWidth = self.image.w
            self.imageHeight = self.image.h
        self.x = 0
        self.y = 0
        self.clipWidth = 0
        self.clipHeight = 0

        self.rad = 0
        self.rotateFlag = True
        self.left = 0
        self.bottom = 0
    def update(self):
        pass
    def draw(self):
        self.image.draw(self.x, self.y, self.imageWidth, self.imageHeight)
    def clip_draw(self):
        self.image.clip_draw(self.left,self.bottom,self.clipWidth, self.clipHeight, self.x, self.y, self.imageWidth, self.imageHeight)
    def rotate_draw(self):
        self.image.rotate_draw(self.rad, self.x, self.y, self.imageWidth, self.imageHeight)
    def setPos(self, x, y):
        self.x = x
        self.y = y
    def setSize(self, w, h):
        self.imageWidth = w
        self.imageHeight = h
    def setClipSize(self, w, h):
        self.clipWidth = w
        self.clipHeight = h
    def setRotateFlag(self, flag):
        self.rotateFlag = flag
    def changeClipFrame(self, left, bottom):
        self.left = left
        self.bottom = bottom
    def setImage(self, imageString):
        if self.image is not None:
            del self.image
        self.image = pico2d.load_image(imageString)
        self.imageWidth = self.image.w
        self.imageHeight = self.image.h
    def setRad(self, rad):
        self.rad = rad
    def getPos(self):
        return self.x, self.y

class hero(object):
    def __init__(self):
        super().__init__(None)
        self.id = 0
    def update(self):
        pass


