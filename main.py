
from random import randint, random
import random

from microbit import *  # pyright: ignore[reportMissingModuleSource]
from st7735 import ST7735

SCREEN_WIDTH = 160
SCREEN_HEIGHT = 128
BORDER_WIDTH = 8
MAX_X = SCREEN_WIDTH - BORDER_WIDTH
MAX_Y = SCREEN_HEIGHT - BORDER_WIDTH
COLOR="#00FF00"
BACKGROUND_COLOR="#000000"
COLOR_COIN = "#FFFF00"
PLAYER_MOVEMENT_SLEEP = 3

PLAYER_SPRITE = [[0, 1, 1, 1, 0],
                 [0, 1, 0, 1, 0],
                 [1, 1, 1, 1, 1],
                 [0, 1, 1, 1, 0],
                 [0, 1, 0, 1, 0]
                 ]

COIN_SPRITE = [[1, 1, 1],
               [1, 0, 1],
               [1, 1, 1]
               ]

CLEAR_COIN = [[1, 1, 1],
              [1, 1, 1],
              [1, 1, 1]
               ]

PLAYER_WIDTH = len(PLAYER_SPRITE[0])
PLAYER_HEIGHT = len(PLAYER_SPRITE)


def are_colliding(sprite1, sprite2):
    matrix1, x1, y1 = sprite1
    matrix2, x2, y2 = sprite2

    width1, height1 = len(matrix1[0]), len(matrix1)
    width2, height2 = len(matrix2[0]), len(matrix2)

    return (
        x1 < x2 + width2
        and x2 < x1 + width1
        and y1 < y2 + height2
        and y2 < y1 + height1
    )


def draw_sprite(x, y, old_x, old_y, sprite):
    screen.move_sprite(sprite, old_x, old_y, x, y, COLOR, BACKGROUND_COLOR)
    sleep(PLAYER_MOVEMENT_SLEEP)

def draw_coin(xcoin, ycoin, COIN_SPRITE):
    screen.draw_matrix(COIN_SPRITE, xcoin, ycoin, COLOR_COIN)

def clear_coin(xcoin, ycoin):
     screen.draw_matrix(CLEAR_COIN, xcoin, ycoin, BACKGROUND_COLOR)

def main():
    try:
        global screen
        screen = ST7735()
        display.off()
        pin3.set_pull(pin3.PULL_DOWN)
        pin4.set_pull(pin4.PULL_DOWN)
        pin7.set_pull(pin7.PULL_DOWN)
        pin6.set_pull(pin6.PULL_DOWN)
        
        xp = SCREEN_WIDTH // 2 - PLAYER_WIDTH // 2
        yp = SCREEN_HEIGHT // 2 - PLAYER_HEIGHT // 2
        xcoin = random.randint(0, 128)
        ycoin = random.randint(0, 128)

        screen.draw_matrix(PLAYER_SPRITE, xp, yp, COLOR)
        draw_coin(xcoin, ycoin, COIN_SPRITE)

        while True:
            jup = pin3.read_digital()
            jdown = pin4.read_digital()
            jleft = pin7.read_digital()
            jright = pin6.read_digital()
            if jup == 1:
                old_yp = yp
                old_xp = xp
                yp -=1
                yp = max(yp, BORDER_WIDTH)
                draw_sprite(xp, yp, old_xp, old_yp, PLAYER_SPRITE)
            if jdown == 1:
                old_yp = yp
                old_xp = xp
                yp += 1
                yp = min(yp, MAX_Y)
                draw_sprite(xp, yp, old_xp, old_yp, PLAYER_SPRITE)
            if jleft == 1:
                old_xp = xp
                old_yp = yp
                xp -= 1
                xp = max(xp, BORDER_WIDTH)
                draw_sprite(xp, yp, old_xp, old_yp, PLAYER_SPRITE)
            if jright == 1:
                old_xp = xp
                old_yp = yp
                xp += 1
                xp = min(xp, MAX_X)
                draw_sprite(xp, yp, old_xp, old_yp, PLAYER_SPRITE)
            if are_colliding((PLAYER_SPRITE, xp, yp), (COIN_SPRITE, xcoin, ycoin)):
                clear_coin(xcoin, ycoin)
                xcoin = random.randint(0, 128)
                ycoin = random.randint(0, 128)
                draw_coin(xcoin, ycoin, COIN_SPRITE)
                
    except Exception as e:
                uart.write(repr(e))
            
main()

# come disegnare un testo
# screen.draw_text(
#     text="ciao sono Pippo\nche scoreggia a piu\nnon posso per tutta la citta",
#     x=2,
#     y=0,
#     color="#0000FF",
# )

# come scrivere sulla seriale
# uart.write("xp = " + str(xp) + " yp = " + str(yp) + "\n")
