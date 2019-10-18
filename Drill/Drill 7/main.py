from pico2d import *
import random

KPU_WIDTH, KPU_HEIGHT = 800  , 600
open_canvas(KPU_WIDTH,KPU_HEIGHT)
class ball:
    def __init__(self):
        self.x = random.randint(0,KPU_WIDTH)
        self.y = 599
        self.speed = random.randint(3, 5)
        if random.randint(0,2) == 0:
            self.image = load_image('ball21x21.png')
            self.imageSize = 21
        else:
            self.image = load_image('ball41x41.png')
            self.imageSize = 41
    def draw(self):
        self.image.draw(self.x, self.y, self.imageSize, self.imageSize)
    def update(self):
        if self.y - self.speed > 120:
            self.y -= self.speed
        else:
            self.y = 120

class boy:
    def __init__(self):
        self.x = random.randint(300,600)
        self.y = 140
        self.speed = random.randint(1,5)
        self.image = load_image('run_animation.png')
        self.frame = 0
    def draw(self):
        self.image.clip_draw(self.frame * 100, 0, 100, 100, self.x, self.y)
    def update(self):
        self.frame = (self.frame + 1) % 8
        self.x += self.speed

class grass:
    def __init__(self):
        self.x = 400
        self.y = 90
        self.image = load_image('grass.png')
    def draw(self,x,y):
        self.image.draw(x, y)

def handle_events():
    global running
    events=get_events()
    for event in events:
        if event.type==SDL_QUIT:
            running=False
        elif event.type ==SDL_KEYDOWN and event.key==SDLK_ESCAPE:
            running=False

running = True

ballList = [ball() for i in range(20)]
boyList = [boy() for i in range(10)]
mygrass = grass()
while (running):
    handle_events()
    mygrass.draw(400,90)
    for i in range(0,20):
        ballList[i].draw()
        ballList[i].update()
    for i in range(0,10):
        boyList[i].draw()
        boyList[i].update()
    update_canvas()
    clear_canvas()
    delay(0.03)

close_canvas()