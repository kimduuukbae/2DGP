import pico2d


class Object:
    def __init__(self, image_name = None):
        self.image = None
        if image_name is not None:
            self.image = pico2d.load_image(image_name)
            self.imageWidth = self.image.w
            self.imageHeight = self.image.h
        self.x = 0
        self.y = 0
        self.clipWidth = 0
        self.clipHeight = 0

        self.pivotX = 0
        self.pivotY = 0

    def update(self):
        pass

    def draw(self):
        self.image.draw(self.x + self.pivotX, self.y + self.pivotY, self.imageWidth, self.imageHeight)

    def set_position(self, x, y):
        self.x = x
        self.y = y

    def set_image_pivot(self, x, y):
        self.pivotX = x
        self.pivotY = y

    def set_image_size(self, w, h):
        self.imageWidth = w
        self.imageHeight = h

    def set_clip_size(self, w, h):
        self.clipWidth = w
        self.clipHeight = h

    def set_image(self, image_name):
        if self.image is not None:
            del self.image
        self.image = pico2d.load_image(image_name)
        self.imageWidth = self.image.w
        self.imageHeight = self.image.h

    def get_position(self):
        return self.x, self.y



