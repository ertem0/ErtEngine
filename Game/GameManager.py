import warnings


class GameManager():
    def __init__(self):
        self.game_objects = []
        self.game_colliders = []
        self.objects_to_update = []

    def update(self, dt):
        for obj in self.objects_to_update:
            obj.update(dt)

    def add_game_object(self, game_object, updatable=False):
        self.game_objects.append(game_object)
        if updatable:
            self.objects_to_update.append(game_object)

    def remove_game_object(self, game_object):
        if game_object in self.game_objects:
            self.game_objects.remove(game_object)
            if game_object in self.objects_to_update:
                self.objects_to_update.remove(game_object)
        else:
            warnings.warn("Game object isn't in the game object array!")

    def add_collider_object(self, collider_object):
        self.game_colliders.append(collider_object)

game_manager = GameManager()