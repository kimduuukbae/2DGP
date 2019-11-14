from pico2d import *
import game_framework
pixel_per_meter = (10.0 / 0.3)

bird_size = 5.0
size_pixel = bird_size * pixel_per_meter

speed_kmph = 30.0
speed_mpm = speed_kmph * 1000.0 / 60.0
speed_mps = speed_mpm / 60.0
speed_pps = speed_mps * pixel_per_meter

time_per_action = 1.0
action_per_time = 1.0 / time_per_action
frame_per_action = 14

class Bird:
    def __init__(self):
        self.image = load_image('bird_animation.png')
        self.x, self.y = 1600 // 2, 400
        self.frame = 0.0
        self.velocity = speed_pps
        self.mass = 2.0
        self.dir = 1
        self.width = self.image.w // 5
        self.height = self.image.h // 3

    def update(self):
        self.frame = (self.frame + frame_per_action * action_per_time \
                      * game_framework.frame_time) % frame_per_action
        print(int(self.frame % 5), "   ", int(self.frame // 5))
        self.x += self.dir * self.velocity * game_framework.frame_time
        self.x = clamp(size_pixel, self.x, 1600 - size_pixel)
        if self.x == size_pixel or self.x == 1600 - size_pixel:
            self.dir = -self.dir

    def draw(self):
        if self.dir == 1:
            self.image.clip_draw(int(self.frame % 5) * self.width, (2 - int(self.frame // 5)) * self.height, self.width, self.height,self.x, self.y \
                                 ,size_pixel, size_pixel)
        else:
            self.image.clip_composite_draw(int(self.frame % 5) * self.width, (2 - int(self.frame // 5)) * self.height, self.width, self.height,0,'h',
                                           self.x, self.y, size_pixel, size_pixel)


