import pygame
import os

from pygame.font import Font
from pygame.color import Color

class DisplayManager:
    def __init__(self, game):
        self.game = game
        pygame.font.init()
        self.font = Font(None, 15)

    def tick(self):
        for x in xrange(0, self.game.size[0]):
            for y in xrange(0, self.game.size[1]):
                for entity in sorted(self.game.em.find((x,y))):
                    self.draw(entity, x, y)
        fps = self.font.render("{} FPS".format(int(self.game.clock.get_fps())), True, Color("black"), Color("white"))
        self.game.window.blit(fps, (self.game.window.get_width() - fps.get_width(),0))
        pygame.display.flip()

    def draw(self, entity, x, y):
        if not entity.needs_redraw():
            return
        surface = entity.do_draw()

        width = self.game.window.get_width()
        height = self.game.window.get_height()

        x_step = width / self.game.size[0]
        y_step = height / self.game.size[1]

        surface = pygame.transform.scale(surface, (x_step, y_step))
        self.game.window.blit(surface, (x * x_step, y * y_step))
