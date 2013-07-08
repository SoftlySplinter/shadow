from pygame.locals import K_UP, K_DOWN, K_RIGHT, K_LEFT, K_w, K_a, K_s, K_d
from shadow.entities import Entity

NORTH = 0b0001
EAST  = 0b0010
SOUTH = 0b0100
WEST  = 0b1000

class Actor(Entity):

    def __init__(self, position, img, em):
        self.position = position
        self.img = img
        self.em = em

    def passable(self):
        False

    def tick(self):
        pass

    def move(self, direction):
        if direction == 0b0000:
            return
        (x, y) = self.position
        if (direction & NORTH) == NORTH:
            new_pos = (x, y-1)
        if (direction & EAST) == EAST:
            new_pos = (x+1, y)
        if (direction & SOUTH) == SOUTH:
            new_pos = (x, y+1)
        if (direction & WEST) == WEST:
            new_pos = (x-1, y)

        for entity in self.em.find(new_pos):
            if not(entity.passable()) and not(entity == self):
                return

        if new_pos != self.position:
            self.invalidate()
            for entity in self.em.find(self.position):
                entity.invalidate()
            
            self.em.remove(self)

            self.position = new_pos
            self.em.add(self)

    def load_image_name(self):
        return self.img

    def order(self):
        return 0xffffff

class Player(Actor):
    @classmethod
    def direction(cls, key):
        if key == K_UP or key == K_w:
            return NORTH
        if key == K_RIGHT or key == K_d:
            return EAST
        if key == K_DOWN or key == K_s:
            return SOUTH
        if key == K_LEFT or key == K_a:
            return WEST
        return 0b0000

    def __init__(self, position, em):
        super(Player, self).__init__(position, "player", em)
        self.direction = 0b0000

    def set_move(self, direction):
        self.direction |= direction

    def unset_move(self, direction):
        pass#self.direction &= ~direction

    def tick(self):
        super(Player, self).tick()
        self.move(self.direction)
        self.direction = 0b0000
