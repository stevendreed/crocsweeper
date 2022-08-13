# draw gameboard & set up mines

import pygame as pyg
#import sys


class Gameboard() :


    def __init__(self, screen, x_tiles, y_tiles, surface) :
        self.screen = [0, 0]
        self.screen[0] = screen[0]
        self.screen[1] = screen[1]
        self.tiles = []
        self.surface = surface

        i = 0

        while (i < x_tiles) :
            k = 0

            self.tiles.append([])

            while (k < y_tiles) :
                c = 0

                self.tiles[i].append([])

                while (c < 2) : # TODO: need to add another z element for visited flag
                    self.tiles[i][k].append(0)
                    c += 1

                # end while

                k += 1
            # end while

            i += 1
        # end while

        return

    # end __init__

    def draw_gameboard(self, line_color = (50, 205, 50)) :
        print("invoked draw_gameboard")

        i = 0

        srt = [0, 0]
        end = [self.screen[0], 0]

        x_tiles = len(self.tiles)
        y_tiles = len(self.tiles[0])

        # draw horizontal lines
        while (i < y_tiles - 1) :
            srt[1] += self.screen[1] / y_tiles
            end[1] += self.screen[1] / y_tiles

            pyg.draw.line(self.surface, line_color, srt, end, 2)
            i += 1
        # end while

        i = 0

        srt = [0, 0]
        end = [0, self.screen[1]]

        # draw vertical lines
        while (i < x_tiles - 1) :
            srt[0] += self.screen[0] / x_tiles
            end[0] += self.screen[0] / x_tiles

            pyg.draw.line(self.surface, line_color, srt, end, 2)
            i += 1
        # end while

        pyg.display.flip() # flush input buffer to screen
        return

    # end draw_gameboard

    def probe_tile(self, x, y) :
        if (x == len(self.tiles) or y == len(self.tiles[0])) :
            return 0                    # out of bounds
        # end if

        if (x < 0 or y < 0) :
            return 0                    # out of bounds
        # end if

        return self.tiles[x][y][1]

    # end probe_tile

    def set_crocs(self, croc_num) :

        # TODO: if tile already has a croc, add to new tile instead

        
        xlen = len(self.tiles)
        ylen = len(self.tiles[0])

        # if the board is not a valid size, do not add crocs
        if (xlen <= 0 or ylen <= 0) :
            return -1                   # an error has occurred
        # end if


        i = 0

        while (i < croc_num) :
            from random import randint

            # TODO: reassign croc to a new tile if one already present
            x_pos = randint(0, xlen - 1)
            y_pos = randint(0, ylen - 1)
            self.tiles[x_pos][y_pos][1] = 1 # 1 means croc!

            i += 1
        # end while

        x = 0

        # apply the number of neighboring crocs to each tile
        while (x < xlen) :

            y = 0
            
            while (y < ylen) :

                # add upper right
                self.tiles[x][y][0] += self.probe_tile(x + 1, y + 1)

                # add right
                self.tiles[x][y][0] += self.probe_tile(x + 1 , y)

                # add lower right
                self.tiles[x][y][0] += self.probe_tile(x + 1, y - 1)

                # add below
                self.tiles[x][y][0] += self.probe_tile(x, y - 1)

                # add lower left
                self.tiles[x][y][0] += self.probe_tile(x - 1, y - 1)

                # add left
                self.tiles[x][y][0] += self.probe_tile(x - 1, y)

                # add upper left
                self.tiles[x][y][0] += self.probe_tile(x - 1, y + 1)

                # add above
                self.tiles[x][y][0] += self.probe_tile(x, y + 1)

                y += 1

            # end while
            x += 1

        # end while

    # end set_crocs

    def reveal_tile(self, x, y) :
        # self.tiles[x][y][0] = self.tiles[x][y][1]
        return self.tiles[x][y][0]

    # end reveal_tile
    