from shadow.entities import Entity
import pygame,os

class TileType():
    @classmethod
    def load(cls):
        # TODO Load from file.
        return [TileType("test", "base_tile", True), TileType("edge","edge", False)]

    def __init__(self, name, img, passable):
        self.name = name
        filen = os.path.join("data/img/", img + ".png")
        self.surface = pygame.image.load(filen)
        self.passable = passable

class Tile(Entity):
    def __init__(self, position, tile_type):
        self.position = position
        self.tile_type = tile_type

    def passable(self):
        return self.tile_type.passable

    def tick(self):
        pass

    def load_image(self):
        return self.tile_type.surface

    def order(self):
        return 0
