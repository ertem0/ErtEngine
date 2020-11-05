import pyglet

class Renderer:
    def __init__(self):
        self.batch = pyglet.graphics.Batch()
        self.batches_to_draw = []

        self.add_batch_to_draw(self.batch)

    def add_batch_to_draw(self, batch):
        if batch not in self.batches_to_draw:
            self.batches_to_draw.append(batch)





