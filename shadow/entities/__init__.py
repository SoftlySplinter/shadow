import pygame, os, random

class Entity(object):
    redraw = True
    cached_image = None
    light = 0

    def tick(self):
        pass

    def do_draw(self):
        self.redraw = False
        return self.draw()

    def invalidate(self):
        self.redraw = True

    def passable(self):
        return True

    def draw(self):
        if self.cached_image == None:
            self.cached_image = self.load_image()
        return self.cached_image

    def load_image(self):
        filen = os.path.join("data/img/", self.load_image_name() + ".png")
        return pygame.image.load(filen)

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

from shadow.entities.light import *
from shadow.entities.tile import *
from shadow.entities.actors import *
