from shadow.entities import Light

class EntityManager:
    def __init__(self, size):
        self.entities = {}
        for x in xrange(-1,size[0]+1):
            for y in xrange(-1,size[1]+1):
                self.entities[(x,y)] = [Light()]
        

    def add(self, entity):
        self.entities[entity.position].append(entity)

    def remove(self, entity):
        self.entities[entity.position].remove(entity)

    def tick(self):
        for entity in self.entities.values():
            for e in entity:
                e.tick()

    def find(self, loc):
        try:
            return self.entities[loc]
        except KeyError:
            return []

    def find_type(self, loc, of_type):
        return [entity for entity in self.find(loc) if type(entity) == of_type]
