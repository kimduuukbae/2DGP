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
heroObject = None
monsterObject = None
turn = None
herodice = None
clickflag = False
clickidx = -1
turnbtn = None
changeturn = False
changetime = 0.0
changescene = False
tempenemytime = 0.0
def exchangeturn():
    global turn, changeturn, changetime, tempenemytime
    if not changeturn:
        if turn:
            heroObject.changeturn()
            monsterObject.reuse()
            herodice.clear()
        else:
            herodice.pushdice(2)
            monsterObject.changeturn()
            heroObject.reuse()
        tempenemytime = 0.0
        changetime = 0.0
        changeturn = True
def exchangescene():

    global changeturn, changetime, changescene
    if not changescene:
        changeturn = True
        changetime = 0.0
        heroObject.changeturn()
        monsterObject.changeturn()
        herodice.clear()
        changescene = True

def enter():
    global fadeObj, sprites, turn, herodice, turnbtn, heroObject, monsterObject
    fadeObj = fade()
    sprites = battle_state_sprite.battle_state_spritelist()
    winsound.PlaySound('../Resources/battle/combat1Sound.wav', winsound.SND_FILENAME | winsound.SND_NOWAIT | \
                       winsound.SND_LOOP | winsound.SND_ASYNC)

    heroObject = item_manager("hero")
    monsterObject = item_manager("monster")

    heroObject.push_item("baseattack")
    heroObject.push_item("ironshield")
    heroObject.push_item("reloaddice")

    monsterObject.push_item("poison")
    monsterObject.push_item("poison")
    monsterObject.push_item("poison")

    turn = True # True == character
    herodice = diceManager(2)
    herodice.setalldicepos(1000,150)
    turnbtn = turnbutton()
    turnbtn.setPos(1700,200)
    pass
def exit():
    pass

def handle_events():
    global clickflag, clickidx, turn, tempenemytime
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
                tempenemytime = 0.0
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
    global changeturn, changetime, turn, changescene, tempenemytime
    sprites.update()
    if turn:
        herodice.update()
        for i in heroObject.getlist():
            i.update()
            if not clickflag:
                herodice.collideToObject(i)
    else:
        tempenemytime += game_framework.frame_time
        if tempenemytime > 1.0:
            exchangeturn()
        for i in monsterObject.getlist():
            i.update()
    if sprites.getvictory() and not changescene:
        exchangescene()
    if changeturn:
        changetime += game_framework.frame_time
        if changetime > 1.0:
            if not changescene:
                turn ^= True
                changeturn = False
            else:
                sprites.setvictory()
                pass


    fadeObj.update()

def draw():
    global turn, changescene
    clear_canvas()
    sprites.draw()
    if turn:
        if not changescene:
            turnbtn.draw()
        heroObject.draw()
    else:
        monsterObject.draw()
    if herodice:
        herodice.draw()


    fadeObj.draw()
    update_canvas()
