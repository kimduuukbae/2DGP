from pico2d import *
import game_framework
from fadescene import *

fadeObj = None

def enter():
    global fadeObj
    fadeObj = fade()
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
    fadeObj.update()

def draw():
    clear_canvas()
    fadeObj.draw()
    update_canvas()
