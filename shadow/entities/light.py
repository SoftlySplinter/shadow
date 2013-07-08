from shadow.entities import Entity
from pygame import Surface

class Light(Entity):
    def __init__(self):
        self.light = 0
        self.prev_light = 0

    def order(self):
        return 0xf

    def tick(self):
        if(self.light != self.prev_light):
            self.invalidate()

    def draw(self):
        surface = Surface((10,10))
        surface.fill((0,0,10))
        surface.set_alpha((255 / 15 * (15 - self.light)) - 4)
        self.prev_light = self.light
        self.light = 0
        return surface
