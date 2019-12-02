import stage1

STAGE_FACTORY = {"stage1" : stage1}

cur_stage = None

def enter():
    global cur_stage
    cur_stage = "stage1"
    STAGE_FACTORY[cur_stage].enter()


def exit():
    STAGE_FACTORY[cur_stage].exit()


def handle_events():
    STAGE_FACTORY[cur_stage].handle_events()


def update():
    STAGE_FACTORY[cur_stage].update()


def draw():
    STAGE_FACTORY[cur_stage].draw()

def pause():
    STAGE_FACTORY[cur_stage].pause()


def resume():
    STAGE_FACTORY[cur_stage].resume()
