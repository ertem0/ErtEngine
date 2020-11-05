import pyglet
import inspect
from resources import resources


class PhysicalObject(pyglet.sprite.Sprite):
    def __init__(self, **kwargs):

        _kwargs = {}
        for arg in inspect.getfullargspec(pyglet.sprite.Sprite.__init__)[0]:
            for key in kwargs.keys():
                if key != arg:
                    continue
                _kwargs[key] = kwargs[key]

        super().__init__(**_kwargs)
        self.velocity_x = 0.0
        self.velocity_y = 0.0


    def update(self, dt):
        self.x = self.x + self.velocity_x * dt
        self.y = self.y + self.velocity_y * dt

    def check_bounds(self):
        min_x = -self.image.width // 2
        min_y = -self.image.height // 2
        max_x = 800 + self.image.width // 2
        max_y = 600 + self.image.height // 2

        if self.x < min_x:
            self.x = max_x
        elif self.x > max_x:
            self.x = min_x
        if self.y < min_y:
            self.y = max_y
        elif self.y > max_y:
            self.y = min_y