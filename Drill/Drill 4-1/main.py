import pico2d as p
from enum import Enum

p.open_canvas(1280,1024)
frame = 0
cx = 600
cy = 200
myInput = [False,False,False,False] #right left down up


class Direct(Enum):
    e_right = 1,
    e_left = -1,
class State(Enum):
    e_idle = 0,
    e_running = 1
def handle_events():
    global direct
    global state
    events = p.get_events()
    for event in events:
        if event.key == p.SDLK_RIGHT:
            myInput[0] ^= True
            direct = Direct.e_right
        if event.key == p.SDLK_LEFT:
            myInput[1] ^= True
            direct = Direct.e_left
        if event.key == p.SDLK_DOWN:
            myInput[2] ^= True
        if event.key == p.SDLK_UP:
            myInput[3] ^= True

        if event.key == p.SDLK_LEFT or event.key == p.SDLK_RIGHT or event.key == p.SDLK_UP or event.key == p.SDLK_DOWN:
            if event.type == p.SDL_KEYDOWN:
                state = State.e_running
            else:
                state = State.e_idle



direct = Direct.e_right
state = State.e_idle

grass = p.load_image('KPU_GROUND.png')
char = p.load_image('animation_sheet.png')
LEFT = 1073741904
RIGHT = 1073741903
UP = 1073741906
DOWN = 1073741905
while(True):
    p.clear_canvas()
    grass.draw(640, 512)
    if direct == Direct.e_right:
        if state == State.e_idle:
            char.clip_draw(frame * 100, 300, 100, 100, cx, cy)
        else:
            char.clip_draw(frame * 100, 100, 100, 100, cx, cy)
    else:
        if state == State.e_idle:
            char.clip_draw(frame * 100, 200, 100, 100, cx, cy)
        else:
            char.clip_draw(frame * 100, 0, 100, 100, cx, cy)
    p.update_canvas()
    frame = (frame+1) % 8
    handle_events()
    if myInput[0] == True and cx < 1280:
        cx += 1
    if myInput[1] == True and cx > 0:
        cx -= 1
    if myInput[2] == True and cy > 0:
        cy -= 1
    if myInput[3] == True and cy < 1024:
        cy += 1
p.close_canvas()