# -*- coding: utf-8 -*-
"""The apps entrypoint."""
from . import game
from . import player


if __name__ == "__main__":

    player1 = player.Player("p1", "m")
    
    game1 = game.x01()
    game1.set_options()
    game1.register_player(player1)

    game1.start()
    