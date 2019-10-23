from pico2d import *
import game_framework
import pause_state
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
    global boy, grass
    boy = Boy()
    grass = Grass()

def exit():
    global boy, grass
    del(boy)
    del(grass)

def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        else:
            if (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
                game_framework.quit()
            if (event.type, event.key) == (SDL_KEYDOWN, SDLK_p):
                game_framework.push_state(pause_state)

def update():
    global boy, grass
    if running:
        boy.update()

running = True
def draw():
    global boy, grass
    clear_canvas()
    grass.draw()
    boy.draw()
    update_canvas()
def pause():
    global running
    running = False
def resume():
    global running
    running = True
