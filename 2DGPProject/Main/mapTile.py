from object import *

class mapTile(object):
    def __init__(self, ID,  x, y): # 현재 tile이 만들어질 장소와 ID
        super().__init__(None)
        self.x = x
        self.y = y
        self.id = ID
        self.Rule = []
        self.origin = 0
        self.future = 0
    def setRule(self, *args): # 자신과 연결 된 타일들의 정보
        for i in args:
            self.Rule.append((i.getInfo()))
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



if __name__ == "__name__":
    print("Module")
    exit(1)