from pico2d import *
import game_framework
import object as o
spriteList = []

def enter():
    global spriteList
    spriteList.append(o.object('../Resources/stage/stageArea.png'))
    spriteList.append(o.object('../Resources/stage/uiShader.png'))
    spriteList.append(o.object('../Resources/stage/character_Icon.png'))
    spriteList.append(o.object('../Resources/stage/character.png'))
    spriteList[0].setPos(960,540)
    spriteList[1].setPos(960,100)
    spriteList[2].setPos(100,100)
    spriteList[3].setPos(450, 600)
    spriteList[3].setSize(260,150)
    pass

def exit():
    pass

def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        else:
            if (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
                game_framework.quit()

def update():
    pass

def draw():
    clear_canvas()
    for i in spriteList:
        i.draw()
    update_canvas()
