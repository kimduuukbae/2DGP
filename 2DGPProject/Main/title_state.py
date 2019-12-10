from pico2d import *
import object as o
import random as r
import game_framework
import main_state
import battle_state_sprite
import fadescene
from sound_manager import *



name = "TitleState"
background = None
char = None
title = None
oList = []
font = None


class Titledice(o.Object):
    image = None

    def __init__(self, image_name, rotation):
        o.Object.__init__(self, image_name)
        self.dir = r.randint(0,1)
        if self.dir == 0:
            self.dir = -0.04
        else:
            self.dir = 0.04
        self.max = 0
        self.plane = r.randint(20,40)
        self.radian = 0.0
        self.rotate_flag = rotation

    def update(self):
        self.y += self.dir
        self.max += self.dir
        if self.max > self.plane or self.max < -self.plane:
            self.max = 0
            self.dir = -self.dir
        if self.rotate_flag is True:
            self.radian -= 0.0001

    def draw(self):
        if self.rotate_flag:
            self.image.rotate_draw(self.radian, self.x + self.pivotX, self.y + self.pivotY, self.imageWidth, self.imageHeight)
        else:
            super().draw()


class Button(o.Object):
    def __init__(self, image_name, origin, future):
        o.Object.__init__(self, image_name)
        self.originframe = origin
        self.clickframe = future
        self.frame = origin

    def overlap_button(self, x, y):
        if self.x - int(self.imageWidth / 2) < x and self.x + int(self.imageWidth /2) > x and \
            self.y - int(self.imageHeight / 2) < y and self.y + int(self.imageHeight /2) > y:
            self.frame = self.clickframe
        else:
            self.frame = self.originframe

    def click_button(self, x, y):
        if self.x - self.imageWidth / 2 < x and self.x + self.imageWidth / 2 > x and \
                self.y - self.imageHeight / 2 < y and self.y + self.imageHeight / 2 > y:
            return True
        return False

    def draw(self):
        self.image.clip_draw(0, self.frame, 608, 150, self.x ,self.y, self.imageWidth, self.imageHeight)


def enter():
    global background, char, title, font
    fadescene.Fade()
    background = o.Object('../Resources/intro/background.png')
    title = o.Object('../Resources/intro/introLogo.png')
    char = o.Object('../Resources/intro/char.png')
    oList.append(Titledice('../Resources/intro/dice1.png', False))
    oList.append(Titledice( '../Resources/intro/dice2.png', False))
    oList.append(Titledice( '../Resources/intro/dice3.png', False))
    oList.append(Titledice( '../Resources/intro/dice4.png', False))
    oList.append(Titledice('../Resources/intro/dice_char.png', True))
    oList.append(Button('../Resources/intro/buttonAtlas.png', 450, 150))
    oList.append(Button('../Resources/intro/buttonAtlas.png', 300, 0))
    background.set_position(960, 540)
    title.set_position(300, 850)
    char.set_position(1300, 658)
    oList[0].set_position(600, 512)
    oList[1].set_position(1100, 600)
    oList[2].set_position(1150, 450)
    oList[3].set_position(900, 400)
    oList[4].set_position(350, 230)

    oList[5].set_position(1600, 250)
    oList[5].set_image_size(400, 100)
    oList[5].set_clip_size(608, 150)

    oList[6].set_position(1600, 100)
    oList[6].set_image_size(400, 100)
    oList[6].set_clip_size(608, 150)

    SoundManager.add_sound("../Resources/sound/title.ogg", "BackGround")
    SoundManager.add_effect_sound("../Resources/sound/effect/herowinsound.wav", "win")
    SoundManager.add_effect_sound("../Resources/sound/effect/herobattlesound.wav", "battle")
    SoundManager.play_sound("BackGround", True)
    battle_state_sprite.Battle_state_sprite.set_init()


def exit():
    global background, char, title
    del background
    del char
    del title
    oList.clear()


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        else:
            if (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
                game_framework.quit()
            if event.type == SDL_MOUSEMOTION:
                x = event.x
                y = 1080 - 1 - event.y
                oList[5].overlap_button(x,y)
                oList[6].overlap_button(x, y)
            if event.type == SDL_MOUSEBUTTONDOWN:
                x = event.x
                y = 1080 - 1 - event.y
                if oList[5].click_button(x, y) is True:
                    fadescene.Fade.change_state(main_state)
                    break
                if oList[6].click_button(x, y) is True:
                    game_framework.quit()


def draw():
    clear_canvas()
    background.draw()
    title.draw()
    char.draw()
    for i in oList:
        i.draw()
    fadescene.Fade.draw()
    update_canvas()


def update():
    for i in oList:
        i.update()
    fadescene.Fade.update()
