import object as o

class main_state_spritelist:
    def __init__(self):
        self.spriteList = []
        self.spriteList.append(o.object('../Resources/stage/stageArea.png'))
        self.spriteList.append(o.object('../Resources/stage/uiShader.png'))
        self.spriteList.append(o.object('../Resources/stage/character_Icon.png'))

        self.spriteList[0].setPos(960, 540)
        self.spriteList[1].setPos(960, 100)
        self.spriteList[2].setPos(100, 100)

    def clear(self):
        self.spriteList.clear()

    def update(self):
        pass

    def draw(self):
        for i in self.spriteList:
            i.draw()