# play.py

import pygame as pyg
from gameboard import Gameboard


class Play(Gameboard) :


    def tile_selection(
            self, tile) :
        """Pass in a list of len = 2. Updates values with the x,y of the tile
        that the mouse is currently over
        """
        x_len = self.screen[0] // len(self.tiles)
        y_len = self.screen[1] // len(self.tiles[0])
        mouse_pos = pyg.mouse.get_pos()

        print("Mouse position:", mouse_pos) # testing purposes

        tile[0] = mouse_pos[0] // x_len
        tile[1] = mouse_pos[1] // y_len

        return

    # end tile_selection
