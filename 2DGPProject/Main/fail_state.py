from pico2d import *
import game_framework

import title_state
import fadescene
from sound_manager import *
import stage_manager

import hero
image = None
dt = 0.0


def enter():
    global image
    image = load_image("../Resources/common/fail.png")
    SoundManager.stop("BackGround")
    SoundManager.stop("Combat")
    stage_manager.StageManager.set_index(0)
    hero.HeroStatus.hp = 24

def exit():
    global image
    del image


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        else:
            if (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
                game_framework.quit()


def draw():
    clear_canvas()
    image.draw(960, 540)
    update_canvas()


def update():
    global image, dt
    dt += game_framework.frame_time
    if dt > 3.0:
        fadescene.Fade.change_state(title_state)
        dt = 0.0

    fadescene.Fade.update()
