from Ertengine.Game.GameManager import game_manager
from copy import deepcopy
from Ertengine.Rendering.Window import window
import pyglet

class CollisionShape2D:
    def __init__(self, collision_verteces=[], is_triggered=False, **kwargs):
        super().__init__(**kwargs)

        if collision_verteces==[]:
            collision_verteces=[-self.image.width, -self.image.height,
                                -self.image.width, self.image.height,
                                self.image.width, self.image.height,
                                self.image.width, -self.image.height]
            collision_verteces = [x // 2 for x in collision_verteces]

        self.COLLISION_VERTECES_DEFAULT = deepcopy(collision_verteces)
        self.collision_verteces = collision_verteces

        self.bounding_box_verteces = [0,0] * 4 #(len(self.collision_verteces)//2)
        self.is_triggered = is_triggered

        game_manager.add_collider_object(self)

        self.debug_batch1 = pyglet.graphics.Batch()
        window.renderer.add_batch_to_draw(self.debug_batch1)
        self.bounding_box = self.debug_batch1.add(4, pyglet.gl.GL_LINE_LOOP, None, ("v2f", self.bounding_box_verteces))

        self.debug_batch2 = pyglet.graphics.Batch()
        window.renderer.add_batch_to_draw(self.debug_batch2)
        self.collision_box = self.debug_batch2.add(len(self.collision_verteces)//2, pyglet.gl.GL_LINE_LOOP, None, ("v2f", self.collision_verteces))

        batch = pyglet.graphics.Batch()
        '''batch.add(3, pyglet.gl.GL_TRIANGLES, None,       Test to draw triangle
                  ('v2i', (0, 0, 30, 35, 30, 15)),
                  ('c3B', (0, 0, 255, 0, 255, 0, 0, 255, 0))
                  )'''
        window.renderer.add_batch_to_draw(batch)


    def update(self, dt):
        self.update_bounding_boxes()
        #self.collison_check()
        self.bounding_box.vertices = self.bounding_box_verteces
        self.collision_box.vertices = self.collision_verteces

        super().update(dt)

    def update_bounding_boxes(self):
        x_vertex_array=[]
        y_vertex_array=[]
        for vertex_index in range(len(self.collision_verteces)):
            if vertex_index % 2 == 0:
                x_vertex_array.append(self.collision_verteces[vertex_index])
            else:
                y_vertex_array.append(self.collision_verteces[vertex_index])
        x_max = max(x_vertex_array)
        x_min = min(x_vertex_array)
        y_max = max(y_vertex_array)
        y_min = min(y_vertex_array)
        self.bounding_box_verteces = [x_min, y_min, x_min, y_max, x_max, y_max, x_max, y_min]

    def collison_check(self):
        print("Checking for collision!")

