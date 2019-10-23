from pico2d import *
import game_framework
import random


class Boy:
    def __init__(self):
        self.x = random.randint(300,600)
        self.y = 140
        self.speed = random.randint(1,5)
        self.image = load_image('animation_sheet.png')
        self.frame = 0
        self.height = 0
    def draw(self):
        self.image.clip_draw(self.frame * 100, self.height, 100, 100, self.x, self.y)
    def update(self):
        self.frame = (self.frame + 1) % 8
        self.x += self.speed
        if self.x > 800 or self.x < 0:
            self.speed = -self.speed
        if self.speed > 0:
            self.height = 100
        else:
            self.height = 0

class Grass:
    def __init__(self):
        self.x = 400
        self.y = 90
        self.image = load_image('grass.png')
    def draw(self):
        self.image.draw(400, 90)


def enter():
    global boy, grass, mypause, bPause, opacity
    boy = Boy()
    grass = Grass()
    mypause = load_image('pause.png')
    bPause = False
    opacity = 200

def exit():
    global boy, grass
    del(boy)
    del(grass)

def handle_events():
    global bPause
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        else:
            if (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
                game_framework.quit()
            if (event.type, event.key) == (SDL_KEYDOWN, SDLK_p):
                bPause ^= 1

def update():
    global boy, grass, opacity
    if not bPause:
        boy.update()
    if bPause:
        opacity -= 1
        if opacity <= 0.0:
            opacity = 200
        mypause.opacify(opacity)


def draw():
    global boy, grass
    clear_canvas()
    grass.draw()
    boy.draw()
    if bPause and opacity > 100:
        mypause.draw(400,300,50,50)
    update_canvas()

