# test.py

import pygame as pyg
from window import Window
from gameboard import Gameboard
from play import Play

# defined main function to avoid default global scope behavior (from py)
def main() :
    pyg.init()
    pyg.time.Clock()

    size = [800, 800]

    screen = pyg.display.set_mode(size)

    instance = Window(size[0], size[1])

    print("Testing doc has begun:")

    # minesweeper = Gameboard(size, 12, 8, screen)
    # print(minesweeper.tiles)

    # minesweeper.draw_gameboard()

    # pyg.time.wait(2000)

    crocs = Play(size, 10, 10, screen)

    crocs.draw_gameboard()
    crocs.set_crocs(25)


    # i = 0

    # mouse buttons for pygame:
    LEFT = 1
    RIGHT = 3

    running = True

    print(crocs.tiles)

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
            print("The number of nearby crocs is:", crocs.tiles[a[0]][a[1]][0])

            if (crocs.tiles[a[0]][a[1]][1] > 0) :
                print("And there is a croc on this tile!")
            # end if

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
    



if (__name__ == "__main__") :
# execution guard-rails which ensure this only runs if run as main
    main()

# end if
