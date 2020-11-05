from pyglet.gl import *
from Ertengine.Rendering.Window import get_window
from Ertengine.Game.Player import Player
from Ertengine.Game.GameManager import game_manager
from resources import resources

if __name__ == "__main__":
    # print()

    window = get_window()

    player = Player(collision_verteces=[-25, -25, 0, 25, 25, -25], x=400, y=300, batch=window.renderer.batch, img=resources.player_img)

    window.push_handlers(player.keys)
    game_manager.add_game_object(player, updatable=True)
    pyglet.clock.schedule_interval(game_manager.update, 1 / 144.0)

    pyglet.app.run()

