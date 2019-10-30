from object import *
from pico2d import *

class mapTile(object):
    image = None
    def __init__(self, ID,  x, y): # 현재 tile이 만들어질 장소와 ID
        super().__init__(None)
        self.x = x
        self.y = y
        self.id = ID
        self.origin = 0
        self.future = 0
    def getInfo(self):
        return self.x,self.y,self.id
    def overlapTile(self,x,y):
        if self.x - self.imageWidth / 2 < x and self.x + self.imageWidth / 2 > x and \
                self.y - self.imageHeight / 2 < y and self.y + self.imageHeight / 2 > y:
            self.changeClipFrame(self.origin, self.future)
        else:
            self.bottom = self.origin
    def setFrame(self, origin, future):
        self.origin = origin
        self.future = future
    def setImage(self, imageString):
        if mapTile.image is None:
            mapTile.image = load_image(imageString)
    def clip_draw(self):
        mapTile.image.clip_draw(self.left, self.bottom, self.clipWidth, self.clipHeight, self.x, self.y, self.imageWidth,\
                             self.imageHeight)

class mapBridge(object):
    image = None
    def __init__(self):
        super().__init__(None)
        pass
    def setImage(self, imageString):
        if mapBridge.image is None:
            mapBridge.image = load_image(imageString)
        self.imageWidth = mapBridge.image.w
        self.imageHeight = mapBridge.image.h
    def rotate_draw(self):
        mapBridge.image.rotate_draw(self.rad, self.x, self.y, \
                                    self.imageWidth, self.imageHeight)

if __name__ == "__name__":
    print("Module")
    exit(1)