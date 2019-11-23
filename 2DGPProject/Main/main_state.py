from pico2d import *
import game_framework
import object as o
from mapTile import *
from Monster import *

spriteList = []
mapList = None
bridgeList = None
character = None
collisionObjectList = []
def enter():
    global character, mapList, bridgeList
    character = o.hero('../Resources/stage/character.png')
    spriteList.append(o.object('../Resources/stage/stageArea.png'))
    spriteList.append(o.object('../Resources/stage/uiShader.png'))
    spriteList.append(o.object('../Resources/stage/character_Icon.png'))
    spriteList[0].setPos(960,540)
    spriteList[1].setPos(960,100)
    spriteList[2].setPos(100,100)
    collisionObjectList.append(fireman())
    collisionObjectList[0].setPos(550,850)
    mapList, bridgeList = makeMap()
    character.setPos(300,600)
    character.setPivot(20,50)
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
                x = event.x
                y = 1080 - 1 - event.y
                for i in mapList:
                    if i.clickTile(x,y):
                        cleanMapList()
                        tileX, tileY, tileId = i.getInfo()
                        if tileId == character.getHeroId():
                            break
                        for j in mapList:
                            j.setVisit(False)
                        if checkMap(character.getHeroId(), tileId):
                            insertMap(mapList, character.getHeroId(), tileId)
                            character.moveTo(getMapList())
                        break
            if event.type == SDL_MOUSEMOTION:
                x = event.x
                y = 1080 - 1 - event.y
                for i in mapList:
                    i.overlapTile(x, y)


def update():
    character.update()
    for i in collisionObjectList:
        i.update()


def draw():
    clear_canvas()
    for i in range(len(spriteList)):
        spriteList[i].draw()
    for i in bridgeList:
        i.rotate_draw()
    for i in mapList:
        i.clip_draw()
    for i in collisionObjectList:
        i.draw()

    character.draw()
    update_canvas()
