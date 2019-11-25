import pico2d

def collisionMouse(mouse, A):
    left, bottom, right, top = A.get_box()
    if mouse[0] > left and mouse[0] < right and mouse[1] > bottom and mouse[1] < top:
        return True
    return False
class button:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.imageWidth = 0
        self.imageHeight = 0


class turnbutton(button):
    image = None
    def __init__(self):
        if turnbutton.image == None:
            turnbutton.image = pico2d.load_image('../Resources/common/nextbutton.png')
        self.imageWidth = turnbutton.image.w
        self.imageHeight = turnbutton.image.h
    def draw(self):
        turnbutton.image.draw(self.x, self.y)
    def get_box(self):
        return self.x - self.imageWidth // 2, self.y - self.imageHeight // 2, \
               self.x + self.imageWidth // 2, self.y + self.imageHeight // 2
    def setPos(self,x,y):
        self.x = x
        self.y = y
