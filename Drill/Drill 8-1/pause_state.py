from pico2d import *
import game_framework
import main_state
name = "PauseState"
image = None
logo_time = 0.0

def enter():
    global image
    image = pico2d.load_image('pause.png')

def exit():
    global image
    del(image)

def update():
    pass


def draw():
    global image
    clear_canvas()
    image.draw(400,300)
    update_canvas()

def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        else:
            if (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
                game_framework.quit()
            if (event.type, event.key) == (SDL_KEYDOWN, SDLK_p):
                game_framework.pop_state()

def resume():
    pass