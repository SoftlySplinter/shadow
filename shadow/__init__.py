import sys, random
import pygame
from pygame.locals import *
from shadow.entities import Tile, TileType, Player
from shadow.entity_manager import EntityManager
from shadow.display_manager import DisplayManager


def run():
    Game().start()
    print "Shadow copyright Alexander Brown, 2013"

class Game:
    size = (25,25)

    def __init__(self):
        self.running = False
        self.types = TileType.load()
        self.em = EntityManager(self.size)
        self.dm = DisplayManager(self)
        self.player = Player((0,0), self.em)
        self.em.add(self.player)
        self.clock = pygame.time.Clock()
        self.window = None

    def start(self):
        self.running = True
        pygame.init()
        info = pygame.display.Info()
        self.window = pygame.display.set_mode((info.current_w, info.current_h))
        pygame.display.toggle_fullscreen()
        self.window.convert_alpha()

        for i in xrange(0, self.size[0]):
            for j in xrange(0, self.size[1]):
                if (i,j) == (0,0):
                    self.em.add(Tile((i,j), self.types[0]))
                else:
                    self.em.add(Tile((i,j), self.types[random.randint(0,len(self.types)-1)]))

        for i in xrange(-1,self.size[0]):
                self.em.add(Tile((i, -1), self.types[1]))
                self.em.add(Tile((i, self.size[1]), self.types[1]))

        for j in xrange(-1, self.size[1]):
                self.em.add(Tile((-1, j), self.types[1]))
                self.em.add(Tile((self.size[0], j), self.types[1]))


        while(self.running):
            self.tick()

    def tick(self):
        self.input(pygame.event.get())
        self.em.tick()
        self.dm.tick()
        self.clock.tick(60)

    def input(self, events):
        for event in events:
            if event.type == QUIT:
                self.running = False
            if event.type == KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.running = False
                self.player.set_move(Player.direction(event.key))
            if event.type == KEYUP:
                self.player.unset_move(Player.direction(event.key))
