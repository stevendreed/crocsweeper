# draw gameboard & set up mines

import pygame as pyg
#import sys


class Gameboard() :


    def __init__(
            self, screen, x_tiles, y_tiles, surface) :
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

                # self.tiles[i].append([])
                # self.tiles[i][k] = 0
                self.tiles[i].append([])
                # self.tiles[i][k].append([])

                while (c < 2) :
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

            pyg.draw.line(
                self.surface, line_color, srt, end, 2
                )
            i += 1
        # end while

        i = 0

        srt = [0, 0]
        end = [0, self.screen[1]]

        # draw vertical lines
        while (i < x_tiles - 1) :
            srt[0] += self.screen[0] / x_tiles
            end[0] += self.screen[0] / x_tiles

            pyg.draw.line(
                self.surface, line_color, srt, end, 2
            )
            i += 1
        # end while

        pyg.display.flip() # flush input buffer to screen

        return

    # end draw_gameboard

    # def probe_tile(self, x, y) :
    #     return self.tiles[x][y][1]

    # end probe_tile

    def reveal_tile(self, x, y) :
        self.tiles[x][y][0] = self.tiles[x][y][1]

        return self.tiles[x][y][0]

    # end reveal_tile
    