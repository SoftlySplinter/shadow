import pygame, os

class Entity(object):
    redraw = True
    cached_image = None

    def tick(self):
        pass

    def do_draw(self):
        self.redraw = False
        return self.draw()

    def invalidate(self):
        self.redraw = True

    def draw(self):
        if self.cached_image == None:
            self.load_image()
        return self.cached_image

    def load_image(self):
        filen = os.path.join("data", self.load_image_name() + ".png")
        self.set_cached_image(pygame.image.load(filen))

    def load_image_name(self):
        return "unknown"

    def set_cached_image(self, image):
        self.cached_image = image

    def order(self):
        return 0

    def needs_redraw(self):
        return self.redraw

    def __cmp__(self, other):
        return self.order() - other.order()

from shadow.entities.tile import *
from shadow.entities.actors import *
