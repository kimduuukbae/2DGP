from pico2d import *
import game_framework
class Grass:
    def __init__(self):
        self.image = load_image('grass.png')

    def update(self):
        pass

    def draw(self):
        self.image.draw(400, 30)
        self.image.draw(1200, 30)
        draw_rectangle(*self.get_bb())


    # fill here
    def get_bb(self):
        return 0, 0, 1600-1, 50

class Brick:
    def __init__(self):
        self.image = load_image('brick180x40.png')
        self.x, self.y = 1000, 200
        self.speed = 50
        self.dir = 1
        self.count = 0
    def update(self):
        self.x = self.x + self.dir * self.speed * game_framework.frame_time
        self.count += 1
        if self.count > 500:
            self.count = 0
            self.dir = -self.dir

    def draw(self):
        self.image.draw(self.x, self.y)
        draw_rectangle(*self.get_bb())

    def get_bb(self):
        return self.x - 90, self.y - 20, self.x + 90, self.y + 20

    def getMoveForce(self):
        return self.dir * self.speed * game_framework.frame_time
