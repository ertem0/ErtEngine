from pyglet.gl import *
from pyglet.window import Window
from Ertengine.Rendering.Renderer import Renderer
from resources import resources

class Window(Window):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.renderer = Renderer()
        glClearColor(255, 0, 0, 255)

    def on_draw(self):
        self.clear()
        for batch in self.renderer.batches_to_draw:
            batch.draw()
        #resources.player_img.blit(0,0)

    #def on_resize(self, width, height):
        #gl.glViewport(0, 0, width, height)
        #glScissor(0, 0, width, height)
        #return

def get_window():
    if window != None:
        return window

window = Window(800, 600, "Ertengine")