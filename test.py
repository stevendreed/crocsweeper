# test.py

import pygame as pyg
from window import Window
from gameboard import Gameboard
from play import Play

if (__name__ == "__main__") :

    pyg.init()
    pyg.time.Clock()

    size = [1200, 800]

    screen = pyg.display.set_mode(size)

    instance = Window(size[0], size[1])

    print("Testing doc has begun:")

    # minesweeper = Gameboard(size, 12, 8, screen)
    # print(minesweeper.tiles)

    # minesweeper.draw_gameboard()

    # pyg.time.wait(2000)

    crocs = Play(size, 12, 8, screen)

    crocs.draw_gameboard()

    # i = 0

    LEFT = 1
    RIGHT = 3
    running = True

    a = [0, 0]
    while (running) :
        event = pyg.event.poll()    

        if (event.type == pyg.QUIT):
            running = False
        # end if

        elif (event.type == pyg.MOUSEBUTTONDOWN and event.button == LEFT) :
            # while (event.type != pyg.MOUSEBUTTONUP and event.button == LEFT) :
            #     # while the mouse hasn't been released
            #     pyg.time.wait(100)
            # # end while

            crocs.tile_selection(a)

            print("Tile location is:", a)
        # end elif

    # end while

    # while (i > 10) :

    #     click = (False, False, False)
    #     click = pyg.mouse.get_pressed(3)

    #     if (click[0]):
    #         crocs.tile_selection(a)
    #         print("Value registered:", a)

    #     # i = pyg.time.get_ticks()
        
    pyg.quit()
    
# end if
