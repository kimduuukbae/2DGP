from pico2d import *
import game_framework
import title_state
import fadescene
import hero
from sound_manager import *
import stage_manager
image1 = None
image2 = None
draw_image = None
dt = 0.0
release_time = 0.0


def enter():
    global image1, image2, draw_image, release_time
    image1 = load_image("../Resources/common/end_1.png")
    image2 = load_image("../Resources/common/end_2.png")
    draw_image = image1
    release_time = 0.0

    SoundManager.stop("Combat")
    SoundManager.change_sound("../Resources/sound/endgame.ogg", "BackGround")
    SoundManager.play_sound("BackGround", True)
    stage_manager.StageManager.set_index(0)
    hero.HeroStatus.hp = 24


def exit():
    global image1, image2
    del image1, image2


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
    draw_image.draw(960,540)
    update_canvas()


def update():
    global dt, image1, image2, draw_image, release_time
    dt += game_framework.frame_time
    release_time += game_framework.frame_time
    if dt > 0.5:
        if draw_image == image1:
            draw_image = image2
        else:
            draw_image = image1
        dt = 0.0

    if release_time > 10.0:
        fadescene.Fade.change_state(title_state)
        release_time = 0.0

    fadescene.Fade.update()
