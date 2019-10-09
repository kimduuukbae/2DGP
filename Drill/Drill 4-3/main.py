import pico2d as p
from enum import Enum
MONITORX = 1280
MONITORY = 1024
p.open_canvas(MONITORX,MONITORY)
frame = 0
cx = 600
cy = 200
mx = 0
my = 0
targetX = 0
targetY = 0
movelist = []
moveFlag = False
class Direct(Enum):
    e_right = 1,
    e_left = -1,
class State(Enum):
    e_idle = 0,
    e_running = 1
def handle_event():
    global cx,cy
    global mx,my
    global idx
    global targetX,targetY
    global moveFlag
    global direct, state
    event = p.get_events()
    for e in event:
        if e.type == p.SDL_MOUSEBUTTONDOWN:
            currentX = cx
            currentY = cy
            targetX = e.x
            targetY = MONITORY - 1 - e.y
            movelist.clear()
            idx = 0
            if targetX >= cx:
                direct = Direct.e_right
            else:
                direct = Direct.e_left
            state =State.e_running
            for i in range(0, 100+1, 2):
                t = i / 100
                movelist.append(((1-t)*currentX + t*targetX, (1-t)*currentY + t*targetY))
            moveFlag = True
        if e.type == p.SDL_MOUSEMOTION:
            mx = e.x
            my = MONITORY - 1 - e.y

grass = p.load_image('KPU_GROUND.png')
char = p.load_image('animation_sheet.png')
mouse = p.load_image('hand_arrow.png')
direct = Direct.e_right
state = State.e_idle
p.hide_cursor()
idx = 0
while(True):
    p.clear_canvas()
    grass.draw(MONITORX / 2, MONITORY / 2)
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
    if moveFlag:
        cx = movelist[idx][0]
        cy = movelist[idx][1]
        idx += 1
        if idx >= 50:
            idx = 0
            moveFlag = False
            state = State.e_idle

    handle_event()
    mouse.draw_now(mx + 25,my -26)
    p.update_canvas()
    frame = (frame+1) % 8

p.close_canvas()