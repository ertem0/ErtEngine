from .PhysicalObject import PhysicalObject
from Ertengine.Game.CollisionShape2D import CollisionShape2D
from resources import resources
from pyglet.window import key
import math


class Player(CollisionShape2D, PhysicalObject):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.keys = key.KeyStateHandler()

        self.rotate_speed = 200.0
        self.velocity = 300.0
        self.slowdown_velocity = 3.0

    def update(self, dt):
        super(Player, self).update(dt)

        self.update_collision_verteces(dt)
        self.movement(dt)
        self.check_bounds()


        resources.set_linear()

    def movement(self, dt):
        pressing = False
        if self.keys[key.W]:
            angle_radians = -math.radians(self.rotation)
            self.velocity_x += self.velocity * dt * math.cos(angle_radians + (math.pi / 2))
            self.velocity_y += self.velocity * dt * math.sin(angle_radians + (math.pi / 2))
            pressing = True
        if self.keys[key.A]:
            self.rotation -= self.rotate_speed * dt
        if self.keys[key.D]:
            self.rotation += self.rotate_speed * dt
        if not pressing:
            self.velocity_x -= self.velocity_x * self.slowdown_velocity * dt
            self.velocity_y -= self.velocity_y * self.slowdown_velocity * dt

    def update_collision_verteces(self, dt):
        for vertex_index in range(len(self.collision_verteces)):
            if vertex_index % 2 == 0:

                angle_radians = -math.radians(self.rotation)

                vertex_xpos = self.x + self.velocity_x * dt
                vertex_ypos = self.y + self.velocity_y * dt

                self.collision_verteces[vertex_index] = vertex_xpos + (self.COLLISION_VERTECES_DEFAULT[vertex_index] * math.cos(angle_radians) - self.COLLISION_VERTECES_DEFAULT[vertex_index + 1] * math.sin(angle_radians ))
                self.collision_verteces[vertex_index + 1] = vertex_ypos + (self.COLLISION_VERTECES_DEFAULT[vertex_index] * math.sin(angle_radians) + self.COLLISION_VERTECES_DEFAULT[vertex_index + 1] * math.cos(angle_radians))

        if self.keys[key.K]:
            print(self.collision_verteces)


