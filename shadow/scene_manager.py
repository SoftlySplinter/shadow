import pickle

class SceneManager(object):
    def __init__(self, entity_manager, scenes):
        self.entity_manager = entity_manager
        self.scenes = scenes

class SceneEditor(object):

class Scene(object):
    def __init__(self, name, data):
        self.name = name
        self.data = data

    def save(to_file):
        with open(to_file) as file:
            pickle.dump(self, file)

    @classmethod
    def load(from_file):
        with open(from_file) as file:
            return pickle.load(file)
