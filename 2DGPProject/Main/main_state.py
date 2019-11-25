from mapTile import *
from monster_in_menu import *
from banner import *
import fadescene
from main_state_spritelist import *
import winsound
from hero import *

mapList = None
bridgeList = None
character = None
collisionObjectList = []
bannerList = []
fadeObj = None
spriteList = None
def collisionHeroVsObject(heroObj, colObj):
    if heroObj.getHeroId() == colObj.getId() and \
    not heroObj.getBattle() and not colObj.getBattle():
        colObj.setBattle(True)
        heroObj.setBattle(True)

def enter():
    global character, mapList, bridgeList, fadeObj, spriteList
    character = hero('../Resources/stage/character.png')
    spriteList = main_state_spritelist()
    collisionObjectList.append(slime())
    collisionObjectList[0].setPos(550,850)
    mapList, bridgeList = makeMap()
    character.setPos(300,600)
    character.setPivot(20,50)
    character.setSize(260,150)
    fadeObj = fadescene.fade()
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
            if (event.type, event.key) == (SDL_KEYDOWN, SDLK_o):
                hero_status().addhp(-1)
            if (event.type, event.button) == (SDL_MOUSEBUTTONDOWN, SDL_BUTTON_LEFT):
                x = event.x
                y = 1080 - 1 - event.y
                if character.getMoving() or character.getBattle():
                    pass
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
        collisionHeroVsObject(character, i)
    for i in bannerList:
        i.update()
    fadeObj.update()
def draw():
    clear_canvas()
    spriteList.draw()
    for i in bridgeList:
        i.rotate_draw()
    for i in mapList:
        i.clip_draw()
    for i in collisionObjectList:
        i.draw()
    character.draw()
    for i in bannerList:
        i.draw()
    fadeObj.draw()
    update_canvas()

def pause():
    for i in range(len(collisionObjectList)):
        if collisionObjectList[i].getBattle():
            collisionObjectList.pop(i)
    pass

def resume():
    character.addX(131)
    fadeObj.setFirst()
    bannerList.pop()
    winsound.PlaySound('../Resources/intro/introSound.wav', winsound.SND_FILENAME | winsound.SND_NOWAIT | \
                       winsound.SND_LOOP | winsound.SND_ASYNC)
    pass
