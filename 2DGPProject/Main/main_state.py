from pico2d import *
import game_framework
import object as o
from mapTile import *
import math
spriteList = []
mapList = []
bridgeList = []
character = None
def enter():
    global character
    character = o.object('../Resources/stage/character.png')
    spriteList.append(o.object('../Resources/stage/stageArea.png'))
    spriteList.append(o.object('../Resources/stage/uiShader.png'))
    spriteList.append(o.object('../Resources/stage/character_Icon.png'))
    spriteList[0].setPos(960,540)
    spriteList[1].setPos(960,100)
    spriteList[2].setPos(100,100)

    f = open('../Resources/stage/mapText.txt', 'r')
    idx = 0
    while True:
        line = f.readline().split(' ')
        if not line[0]: break
        x,y,z = map(int,line)
        mapList.append(mapTile(x,y,z))
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
        bridgeList[idx].setSize(210,15)
        x1,y1,id1 = mapList[startID-1].getInfo()
        x2,y2,id2 = mapList[endID-1].getInfo()
        rad = math.atan2(y2-y1,x2-x1)
        bridgeList[idx].setRad(rad)
        if x1 >= x2:
            x1 -= 125
        else:
            x1 += 125
        if y1 >= y2:
            y1 -= 125
        else:
            y1 += 125
        bridgeList[idx].setPos(x1,y1)
        idx += 1
    character.setPos(320,650)
    character.setSize(260,150)
def exit():
    global character
    del character
    spriteList.clear()
    mapList.clear()

def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        else:
            if (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
                game_framework.quit()
            if event.type == SDL_MOUSEMOTION:
                x = event.x
                y = 1080 - 1 - event.y
                for i in mapList:
                    i.overlapTile(x, y)

def update():
    pass

def draw():
    clear_canvas()
    for i in range(len(spriteList)):
        spriteList[i].draw()
    for i in bridgeList:
        i.rotate_draw()
    for i in mapList:
        i.clip_draw()

    character.draw()
    update_canvas()
