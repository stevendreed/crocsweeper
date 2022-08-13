# play.py

import pygame as pyg
from gameboard import Gameboard


class Play(Gameboard) :


    def tile_selection(self, tile) :
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

    def draw_num(self, tile) :
        """receives the x and y coordinate of a tile and draws the number
        of adjacent crocs to each tile."""
        # get the center of the tile based on abstract screen size and tile num

        # use pygame to draw the tiles[x][y][0] value

        # return something?
        gap_x = self.screen[0] // len(self.tiles)
        gap_y = self.screen[1] // len(self.tiles[0])

        # use pygame.draw.rect(surface, color, rect, width=0) to cover old numbers

        # todraw = pyg.Surface.blit((gap_x * tile[0], gap_y * tile[1]),
        #                           (gap_x * tile[0] + gap_x, gap_y * tile[1] + tile[1]))

        if (pyg.font.get_init()) :
            txtcolor = (0, 0, 0)
            bgcolor = (255, 255, 255)
            pyg.font.render(self.tiles[tile[0]][tile[1][0]], 1, txtcolor, bgcolor)
        # end if

        # need to blit this onto a new shape


    # end draw_num

# end Play
