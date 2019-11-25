from fadescene import *
import battle_state_sprite
from monster_in_battle import *
import winsound
from item import *
from monster_in_battle import monster_status
from dice import *
from button import *
fadeObj = None
sprites = None
collisionObject = []
turn = None
herodice = None
clickflag = False
clickidx = -1
turnbtn = None

def exchangeturn():
    global turn
    if turn:
        for i in collisionObject:
            i.setexitturn()
        herodice.clear()
    else:
        herodice.pushdice(2)
        for i in collisionObject:
            i.reuse()
    turn ^= True

def enter():
    global fadeObj, sprites, collisionObject, turn, herodice, turnbtn
    fadeObj = fade()
    sprites = battle_state_sprite.battle_state_spritelist()
    winsound.PlaySound('../Resources/battle/combat1Sound.wav', winsound.SND_FILENAME | winsound.SND_NOWAIT | \
                       winsound.SND_LOOP | winsound.SND_ASYNC)
    collisionObject.append(ironshield())
    collisionObject.append(reloaddice())
    collisionObject.append(baseattack())

    turn = True # True == character
    herodice = diceManager(2)
    herodice.setalldicepos(1000,150)
    turnbtn = turnbutton()
    turnbtn.setPos(1700,200)
    pass
def exit():
    pass

def handle_events():
    global clickflag, clickidx, turn
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        if event.type == SDL_KEYDOWN:
            if event.key == SDLK_ESCAPE:
                game_framework.quit()
            if event.key == SDLK_SPACE:
                fadeObj.pop_state()
            if event.key ==  SDLK_o and turn == False:
                exchangeturn()
        if turn:
            if event.type == SDL_MOUSEMOTION:
                if clickflag:
                    x = event.x
                    y = 1080 - 1 - event.y
                    herodice.getdicetoidx(clickidx).setPos(x,y)
                    pass
            if event.type == SDL_MOUSEBUTTONDOWN:
                x = event.x
                y = 1080 - 1 - event.y
                if collisionMouse((x, y), turnbtn):
                    exchangeturn()
                    break;
                temp = herodice.collideToMouse((x,y))

                if temp != None:
                    clickflag = True
                    clickidx = temp
                    herodice.getdicetoidx(clickidx).setPos(x,y)

            if event.type == SDL_MOUSEBUTTONUP:
                clickflag = False

def update():
    sprites.update()
    if herodice:
        herodice.update()
    for i in collisionObject:
        i.update()
        if not clickflag:
            herodice.collideToObject(i)
    fadeObj.update()

def draw():
    global turn
    clear_canvas()
    sprites.draw()
    for i in collisionObject:
        i.draw()
    if herodice:
        herodice.draw()
    if turn:
        turnbtn.draw()
    fadeObj.draw()
    update_canvas()
