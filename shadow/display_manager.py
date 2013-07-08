import pygame
import os

class DisplayManager:
    def __init__(self, game):
        self.game = game

    def tick(self):
        for x in xrange(0, self.game.size[0]):
            for y in xrange(0, self.game.size[1]):
                for entity in sorted(self.game.em.find((x,y))):
                    self.draw(entity, x, y)
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
