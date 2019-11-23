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
        self.connect = []
        self.visit = False
    def getInfo(self):
        return self.x,self.y,self.id
    def clickTile(self,x,y):
        if self.x - self.imageWidth / 2 < x and self.x + self.imageWidth / 2 > x and \
                self.y - self.imageHeight / 2 < y and self.y + self.imageHeight / 2 > y:
            return True
        return False
    def overlapTile(self,x,y):
        if self.x - self.imageWidth / 2 < x and self.x + self.imageWidth / 2 > x and \
                self.y - self.imageHeight / 2 < y and self.y + self.imageHeight / 2 > y:
            self.changeClipFrame(self.origin, self.future)
        else:
            self.bottom = self.origin
    def setConnect(self, x, y, id):
        self.connect.append((x,y,id))
    def getConnect(self):
        return self.connect
    def setFrame(self, origin, future):
        self.origin = origin
        self.future = future
    def setImage(self, imageString):
        if mapTile.image is None:
            mapTile.image = load_image(imageString)
    def clip_draw(self):
        mapTile.image.clip_draw(self.left, self.bottom, self.clipWidth, self.clipHeight, self.x, self.y, self.imageWidth,\
                             self.imageHeight)
    def getVisit(self):
        return self.visit
    def setVisit(self, flag):
        self.visit = flag
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


def makeMap():
    mapList =[]
    bridgeList =[]
    f = open('../Resources/stage/mapText.txt', 'r')
    idx = 0
    while True:
        line = f.readline().split(' ')
        if not line[0]: break
        x, y, z = map(int, line)
        mapList.append(mapTile(x, y, z))
        mapList[idx].setImage('../Resources/stage/mapTile.png')
        mapList[idx].setSize(200, 150)
        mapList[idx].setClipSize(280, 140)
        mapList[idx].setFrame(0, 140)
        idx += 1
    f.close()
    f = open('../Resources/stage/mapVertex.txt', 'r')
    idx = 0
    while True:
        line = f.readline().split(' ')
        if not line[0]: break
        startID, endID = map(int, line)
        bridgeList.append(mapBridge())
        bridgeList[idx].setImage('../Resources/stage/mapBridge.png')
        bridgeList[idx].setSize(210, 15)
        x1, y1, id1 = mapList[startID - 1].getInfo()
        x2, y2, id2 = mapList[endID - 1].getInfo()
        mapList[startID-1].setConnect(x2,y2,id2)
        mapList[endID-1].setConnect(x1,y1,id1)
        rad = math.atan2(y2 - y1, x2 - x1)
        bridgeList[idx].setRad(rad)
        if x1 >= x2:
            x1 -= 125
        else:
            x1 += 125
        if y1 >= y2:
            y1 -= 125
        else:
            y1 += 125
        bridgeList[idx].setPos(x1, y1)
        idx += 1
    return mapList, bridgeList
def checkMap(nowid, moveid):
    if nowid == moveid:
        return False
    return True
returnlists = []
def insertMap(list, nowid, moveid):  # 리스트들과 현재 캐릭터, 갈 위치 id 를 받음
    if list[nowid-1].getVisit():
        return False
    conn = list[nowid - 1].getConnect()


    list[nowid-1].setVisit(True)
    if nowid == moveid:
        returnlists.append(list[nowid - 1].getInfo())
        return True
    for i in conn:
        if insertMap(list, i[2], moveid) is True:
            returnlists.append(list[nowid - 1].getInfo())
            return True


def cleanMapList():
    returnlists.clear()
def getMapList():
    returnlists.pop()
    returnlists.reverse()
    return returnlists

if __name__ == "__name__":
    print("Module")
    exit(1)