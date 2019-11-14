from pico2d import *
import game_framework
import object as o
from mapTile import *
spriteList = []
mapList = None
bridgeList = None
character = None
def enter():
    global character, mapList, bridgeList
    character = o.hero('../Resources/stage/character.png')
    spriteList.append(o.object('../Resources/stage/stageArea.png'))
    spriteList.append(o.object('../Resources/stage/uiShader.png'))
    spriteList.append(o.object('../Resources/stage/character_Icon.png'))
    spriteList[0].setPos(960,540)
    spriteList[1].setPos(960,100)
    spriteList[2].setPos(100,100)

    mapList, bridgeList = makeMap()
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
            if (event.type, event.button) == (SDL_MOUSEBUTTONDOWN, SDL_BUTTON_LEFT):
                x,y,id = moveMap(mapList, 1, 2)[0]
                character.moveTo(x,y,id)
            if event.type == SDL_MOUSEMOTION:
                x = event.x
                y = 1080 - 1 - event.y
                for i in mapList:
                    i.overlapTile(x, y)


def update():
    character.update()

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
