from pico2d import *
import game_framework
from fadescene import *
import battle_state_sprite
from monster_in_battle import *
import winsound
from item import *
fadeObj = None
sprites = None
monster = None
collisionObject = None
def enter():
    global fadeObj, sprites,monster, collisionObject
    fadeObj = fade()
    sprites = battle_state_sprite.battle_state_spritelist()
    monster = slime()
    winsound.PlaySound('../Resources/battle/combat1Sound.wav', winsound.SND_FILENAME | winsound.SND_NOWAIT | \
                       winsound.SND_LOOP | winsound.SND_ASYNC)
    collisionObject = ironshield()
    pass
def exit():
    global monster
    del monster
    pass

def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        else:
            if (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
                game_framework.quit()
            if (event.type, event.key) == (SDL_KEYDOWN, SDLK_SPACE):
                fadeObj.pop_state()


def update():
    monster.update()
    fadeObj.update()

def draw():
    clear_canvas()
    sprites.draw()
    monster.draw()
    collisionObject.draw()
    fadeObj.draw()
    update_canvas()
