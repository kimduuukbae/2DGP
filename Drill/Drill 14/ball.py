import random
from pico2d import *
import game_world
import game_framework

class Ball:
    image = None

    def __init__(self):
        if Ball.image == None:
            Ball.image = load_image('ball21x21.png')
        self.x, self.y, self.fall_speed = random.randint(0, 1600-1), 60, 0

    def get_bb(self):
        # fill here
        return self.x -10, self.y - 10, self.x + 10, self.y - 10

    def draw(self):
        self.image.draw(self.x, self.y)
        draw_rectangle(*self.get_bb())

    def update(self):
        pass

    def stop(self):
        self.fall_speed = 0


class BigBall(Ball):
    MIN_FALL_SPEED = 50
    MAX_FALL_SPEED = 200
    image = None
    background = None

    def __init__(self):
        if BigBall.image == None:
           BigBall.image = load_image('ball41x41.png')
        self.x, self.y = random.randint(0,1600-1), random.randint(240, 900-1)
        self.fall_speed = random.randint(BigBall.MIN_FALL_SPEED,
                                          BigBall.MAX_FALL_SPEED)
        self.cx = 0
        self.cy = 0

    def get_bb(self):
        return self.cx - 20, self.cy - 20, self.cx + 20, self.cy + 20

    def setX(self, force):
        self.x = self.x + force

    def draw(self):

        self.image.draw(self.cx, self.cy)
        draw_rectangle(*self.get_bb())

    def update(self):
        cx, cy = self.x - BigBall.background.window_left, self.y - BigBall.background.window_bottom
        self.cx, self.cy = cx, cy
        pass


    @staticmethod
    def set_background(background):
        BigBall.background = background
