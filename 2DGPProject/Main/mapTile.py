from object import *
from pico2d import *


class Maptile(Object):
    image = None

    def __init__(self, id, x, y): # 현재 tile이 만들어질 장소와 ID
        super().__init__(None)
        self.x = x
        self.y = y
        self.id = id
        self.originframe = 0
        self.clickframe = 0
        self.connect = []
        self.visit = False
        self.radian = 0.04
        self.frame = 0

    def set_radian(self, rad):
        self.radian = rad

    def get_tileinfo(self):
        return self.x, self.y, self.id

    def click_tile(self, x, y):
        if self.x - self.imageWidth / 2 < x and self.x + self.imageWidth / 2 > x and \
                self.y - self.imageHeight / 2 < y and self.y + self.imageHeight / 2 > y:
            return True
        return False

    def overlap_tile(self, x, y):
        if self.x - self.imageWidth / 2 < x and self.x + self.imageWidth / 2 > x and \
                self.y - self.imageHeight / 2 < y and self.y + self.imageHeight / 2 > y:
            self.frame = self.clickframe
        else:
            self.frame= self.originframe

    def set_connect_map(self, x, y, id):
        self.connect.append((x, y, id))

    def get_connect_map(self):
        return self.connect

    def set_frame(self, origin, future):
        self.originframe = origin
        self.clickframe = future

    def draw(self):
        Maptile.image.clip_draw(0, self.frame, self.clipWidth, self.clipHeight, self.x, self.y, self.imageWidth, \
                                self.imageHeight)

    def get_visited(self):
        return self.visit

    def set_visited(self, flag):
        self.visit = flag

    def set_image(self, image_name):
        if Maptile.image is None:
            Maptile.image = pico2d.load_image(image_name)
            self.imageWidth = Maptile.image.w
            self.imageHeight = Maptile.image.h


class Mapbridge(Object):
    image = None

    def __init__(self):
        super().__init__(None)
        self.radian = 0.0

    def set_image(self, image_name):
        if Mapbridge.image is None:
            Mapbridge.image = load_image(image_name)
        self.imageWidth = Mapbridge.image.w
        self.imageHeight = Mapbridge.image.h

    def set_radian(self, rad):
        self.radian = rad

    def draw(self):
        Mapbridge.image.rotate_draw(self.radian, self.x, self.y, self.imageWidth, self.imageHeight)


def make_map(count):
    map_list = []
    bridge_list = []
    f = open('../Resources/stage/mapText' + str(count) + '.txt', 'r')
    idx = 0
    while True:
        line = f.readline().split(' ')
        if not line[0]:
            break
        x, y, z = map(int, line)
        map_list.append(Maptile(x, y, z))
        map_list[idx].set_image('../Resources/stage/mapTile.png')
        map_list[idx].set_image_size(200, 150)
        map_list[idx].set_clip_size(280, 140)
        map_list[idx].set_frame(0, 140)
        idx += 1
    f.close()
    f = open('../Resources/stage/mapVertex' + str(count) + '.txt', 'r')
    idx = 0
    while True:
        line = f.readline().split(' ')
        if not line[0]:
            break
        start_id, end_id = map(int, line)
        bridge_list.append(Mapbridge())
        bridge_list[idx].set_image('../Resources/stage/mapBridge.png')
        bridge_list[idx].set_image_size(210, 15)
        x1, y1, id1 = map_list[start_id - 1].get_tileinfo()
        x2, y2, id2 = map_list[end_id - 1].get_tileinfo()
        map_list[start_id-1].set_connect_map(x2, y2, id2)
        map_list[end_id-1].set_connect_map(x1, y1, id1)
        rad = math.atan2(y2 - y1, x2 - x1)
        bridge_list[idx].set_radian(rad)
        if x1 == x2:
            y1 += 125

        else:
            if x1 >= x2:
                x1 -= 125
            else:
                x1 += 125
            if y1 >= y2:
                y1 -= 125
            else:
                y1 += 125
        bridge_list[idx].set_position(x1, y1)
        idx += 1
    return map_list, bridge_list


def check_map(nowid, moveid):
    if nowid == moveid:
        return False
    return True


returnlists = []


def insert_map(list, nowid, moveid):  # 리스트들과 현재 캐릭터, 갈 위치 id 를 받음
    if list[nowid-1].get_visited():
        return False
    conn = list[nowid - 1].get_connect_map()
    list[nowid-1].set_visited(True)

    if nowid == moveid:
        returnlists.append(list[nowid - 1].get_tileinfo())
        return True
    for i in conn:
        if insert_map(list, i[2], moveid) is True:
            returnlists.append(list[nowid - 1].get_tileinfo())
            return True


def clear_maplist():
    returnlists.clear()


def get_maplist():
    returnlists.pop()
    returnlists.reverse()
    return returnlists


if __name__ == "__name__":
    print("Module")
    exit(1)
