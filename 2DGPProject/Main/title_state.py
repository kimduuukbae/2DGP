from pico2d import *
import object as o
import random as r
import game_framework
import main_state
import winsound
import fadescene

name = "TitleState"
background = None
char = None
title = None
fadeObj = None
oList = []
font = None

class Dice(o.object):
    image = None
    def __init__(self, imageString):
        o.object.__init__(self, imageString)
        self.dir = r.randint(0,1)
        if self.dir == 0:
            self.dir = -0.04
        else:
            self.dir = 0.04
        self.max = 0
        self.plane = r.randint(20,40)

    def update(self):
        self.y += self.dir
        self.max += self.dir
        if self.max > self.plane or self.max < -self.plane:
            self.max = 0
            self.dir = -self.dir
        if self.rotateFlag is True:
            self.rad -= 0.0001

class button(o.object):
    def __init__(self, imageString, origin, future):
        o.object.__init__(self,imageString)
        self.origin = origin
        self.future = future
    def overlapButton(self, x, y):
        if self.x - self.imageWidth / 2 < x and self.x + self.imageWidth /2 > x and \
            self.y - self.imageHeight / 2 < y and self.y + self.imageHeight /2 > y:
            self.changeClipFrame(0, self.future)
        else:
            self.bottom = self.origin
    def clickButton(self,x,y):
        if self.x - self.imageWidth / 2 < x and self.x + self.imageWidth / 2 > x and \
                self.y - self.imageHeight / 2 < y and self.y + self.imageHeight / 2 > y:
            return True
        else:
            return False

def enter():
    global background,char,title, fadeObj, font
    background = o.object('../Resources/intro/background.png')
    title = o.object('../Resources/intro/introLogo.png')
    char = o.object('../Resources/intro/char.png')
    oList.append(Dice('../Resources/intro/dice1.png'))
    oList.append(Dice( '../Resources/intro/dice2.png'))
    oList.append(Dice( '../Resources/intro/dice3.png'))
    oList.append(Dice( '../Resources/intro/dice4.png'))
    oList.append(Dice('../Resources/intro/dice_char.png'))
    oList.append(button('../Resources/intro/buttonAtlas.png', 450, 150))
    oList.append(button('../Resources/intro/buttonAtlas.png', 300, 0))
    background.setPos(960,540)
    title.setPos(300,850)
    char.setPos(1300,658)
    oList[0].setPos(600, 512)
    oList[1].setPos(1100, 600)
    oList[2].setPos(1150, 450)
    oList[3].setPos(900, 400)
    oList[4].setPos(350, 230)
    oList[4].setRotateFlag(False)
    oList[5].setPos(1600, 250)
    oList[5].setSize(400,100)
    oList[5].setClipSize(608,150)
    oList[6].setPos(1600, 100)
    oList[6].setSize(400, 100)
    oList[6].setClipSize(608, 150)
    winsound.PlaySound('../Resources/intro/introSound.wav', winsound.SND_FILENAME | winsound.SND_NOWAIT | \
                       winsound.SND_LOOP | winsound.SND_ASYNC)

    fadeObj = fadescene.fade()
def exit():
    global background,char
    del background
    del char
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
                oList[5].overlapButton(x,y)
                oList[6].overlapButton(x, y)
            if event.type == SDL_MOUSEBUTTONDOWN:
                x = event.x
                y = 1080 - 1 - event.y
                if oList[5].clickButton(x, y) is True:
                    fadeObj.changeScene(main_state)
                    break
                if oList[6].clickButton(x, y) is True:
                    game_framework.quit()

def draw():
    clear_canvas()
    background.draw()
    title.draw()
    char.draw()
    for i in range(len(oList)-2):
        oList[i].rotate_draw()
        oList[i].update()
    oList[5].clip_draw()
    oList[6].clip_draw()
    fadeObj.draw()
    update_canvas()

def update():

    fadeObj.update()
