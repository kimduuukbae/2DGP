from pico2d import *
import game_framework
import object as o
from mapTile import *
spriteList = []
mapList = []
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
    character.setPos(470,550)
    character.setSize(260,150)

def exit():
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
    for i in spriteList:
        i.draw()
    for i in mapList:
        i.clip_draw()
    character.draw()
    update_canvas()
