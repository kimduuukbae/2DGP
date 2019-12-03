import game_framework
import pico2d
import stage_manager


class Idle:
    @staticmethod
    def enter(fadeobj):
        pass

    @staticmethod
    def do(fadeobj):
        pass

class FadeIn:
    @staticmethod
    def enter(fadeobj):
        fadeobj.x = -960.0
        pass

    @staticmethod
    def do(fadeobj):
        fadeobj.x += 5760 * game_framework.frame_time
        if fadeobj.x > 960:
            fadeobj.push_event(FadeOut)
            if fadeobj.change_type is False:
                game_framework.change_state(fadeobj.next_state)
            else:
                game_framework.push_state(fadeobj.next_state)

class FadeInPop:
    @staticmethod
    def enter(fadeobj):
        fadeobj.x = -960.0
        pass

    @staticmethod
    def do(fadeobj):
        fadeobj.x += 5760 * game_framework.frame_time
        if fadeobj.x > 960.0:
            fadeobj.push_event(FadeOut)
            game_framework.pop_state()

class FadeInStage:
    @staticmethod
    def enter(fadeobj):
        fadeobj.x = -960.0

    @staticmethod
    def do(fadeobj):
        fadeobj.x += 5760 * game_framework.frame_time
        if fadeobj.x > 960.0:
            fadeobj.push_event(FadeOut)
            stage_manager.StageManager.next_stage()

class FadeOut:
    @staticmethod
    def enter(fadeobj):
        fadeobj.x = 960.0
        pass

    @staticmethod
    def do(fadeobj):
        fadeobj.x += 5760 * game_framework.frame_time
        if fadeobj.x > 2880.0:
            fadeobj.push_event(Idle)
        pass




class Fade:
    image = None
    cur_state = None
    next_state = None
    change_type = False
    event_que = []
    x = -960.0
    y = 540.0

    def __init__(self):
        if Fade.cur_state is None:
            Fade.cur_state = Idle
            Fade.next_state = Idle
            Fade.change_type = False
            Fade.image = pico2d.load_image("../Resources/fade.png")

    @staticmethod
    def update():
        Fade.cur_state.do(Fade)
        if len(Fade.event_que) > 0:
            event = Fade.event_que.pop()
            Fade.cur_state = event
            Fade.cur_state.enter(Fade)

    @staticmethod
    def push_event(state):
        Fade.event_que.append(state)

    @staticmethod
    def draw():
        Fade.image.draw(Fade.x, Fade.y, Fade.image.w, Fade.image.h)

    @staticmethod
    def change_state(state):
        Fade.change_type = False
        Fade.next_state = state
        Fade.push_event(FadeIn)

    @staticmethod
    def push_state(state):
        Fade.change_type = True
        Fade.next_state = state
        Fade.push_event(FadeIn)

    @staticmethod
    def pop_state():
        Fade.push_event(FadeInPop)
