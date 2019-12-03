from fadescene import *
import battle_state_sprite
import winsound
from item import *
from dice import *
from button import *
import hero
import monster_in_battle

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


def change_turn():
    global turn, changeturn, changetime
    if not changeturn:
        if turn:
            heroObject.changeturn()
            monsterObject.reuse()
            herodice.dice_clear()
        else:
            herodice.push_dice(2)
            monsterObject.changeturn()
            heroObject.reuse()
        changetime = 0.0
        changeturn = True


def change_scene():

    global changeturn, changetime, changescene
    if not changescene:
        changeturn = True
        changetime = 0.0
        heroObject.changeturn()
        monsterObject.changeturn()
        herodice.dice_clear()
        changescene = True


def enter():
    global sprites, turn, herodice, turnbtn, heroObject, monsterObject
    sprites = battle_state_sprite.Battle_state_sprite()
    winsound.PlaySound('../Resources/battle/combat1Sound.wav', winsound.SND_FILENAME | winsound.SND_NOWAIT | \
                       winsound.SND_LOOP | winsound.SND_ASYNC)

    heroObject = item_manager("hero")
    monsterObject = item_manager("monster")

    heroObject.push_item_list(hero.Hero_status.equip_item)
    monsterObject.push_item_list(monster_in_battle.Monsterstatus.item_list)

    turn = True # True == character
    herodice = Dice_manager(2)
    herodice.set_all_dice_pos(1000, 150)
    turnbtn = Turnbutton()
    turnbtn.set_position(1700, 200)


def exit():
    global clickflag, clickidx, changeturn, changetime, changescene
    sprites.clear_banner()
    clickflag = False
    clickidx = -1
    changeturn = False
    changetime = 0.0
    changescene = False
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
            if event.key == SDLK_o and turn is False:
                change_turn()
        if turn:
            if event.type == SDL_MOUSEMOTION:
                if clickflag:
                    x = event.x
                    y = 1080 - 1 - event.y
                    herodice.get_dice_to_idx(clickidx).set_position(x, y)
                    pass
            if event.type == SDL_MOUSEBUTTONDOWN:
                x = event.x
                y = 1080 - 1 - event.y
                if collide_to_mouse((x, y), turnbtn):
                    change_turn()
                    break;
                temp = herodice.collide_to_mouse((x, y))
                if temp is not None:
                    clickflag = True
                    clickidx = temp
                    herodice.get_dice_to_idx(clickidx).set_position(x, y)

            if event.type == SDL_MOUSEBUTTONUP:
                clickflag = False


def update():
    global changeturn, changetime, turn, changescene
    sprites.update()
    if turn:
        herodice.update()
        for i in heroObject.getlist():
            i.update()
            if not clickflag:
                herodice.collide_to_object(i)
    else:
        for i in monsterObject.getlist():
            i.update()
    if sprites.getvictory() and not changescene:
        change_scene()
    if changeturn:
        changetime += game_framework.frame_time
        if changetime > 2.0:
            if not changescene:
                turn ^= True
                changeturn = False
            else:
                sprites.setvictory()
                pass

    Fade.update()


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

    Fade.draw()
    update_canvas()
