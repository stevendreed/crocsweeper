# window.py

import pygame as pyg
# import sys


class Window():


    def __init__(self, width, height, color = (1, 1, 1)):
        self.screen = [0, 0]
        self.screen[0] = width
        self.screen[1] = height

        # initialize pygame display
        pyg.display.init()

        if (pyg.display.init()) :
        # if init successful, fill screen with white and flush buffer
            pyg.screen.fill(color)
            pyg.display.flip()

        # end if

        return
    # end __init__

    def __del__(self):

        # exit pygame display
        pyg.display.quit()

        return
    # end __del__

# end Window
