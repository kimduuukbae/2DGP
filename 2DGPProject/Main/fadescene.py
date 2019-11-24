import game_framework
import pico2d

class fade:
    image = None
    def __init__(self):
        self.state = None
        self.x = 960
        self.y = 540
        self.stateFlag = False
        self.startChange = False
        self.first = True
        if fade.image == None:
            fade.image = pico2d.load_image("../Resources/fade.png")
    def update(self):
        if self.startChange:
            self.x += 20
            if self.x > 960:
                if self.stateFlag:
                    game_framework.push_state(self.state)
                else:
                    game_framework.change_state(self.state)
                self.startChange = False
        elif self.first:
            self.x += 20
            if self.x > 2880:
                self.first = False
                self.x = -960

    def draw(self):
        if self.startChange or self.first:
            fade.image.draw(self.x, self.y, fade.image.w, fade.image.h)
    def changeScene(self, state):
        self.stateFlag = False
        self.state = state
        self.startChange = True

    def push_state(self, state):
        self.state = state
        self.stateFlag = True
        self.startChange = True