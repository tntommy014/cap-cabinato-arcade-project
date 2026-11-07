
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
PLAYER_MOVEMENT_SLEEP = 1
xcoin = random.randint(0, 128)
ycoin = random.randint(0, 128)

# PLAYER_SPRITE = [[0, 1, 0],
#                  [1, 1, 1],
#                  [0, 1, 0]]

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

CLEAR_COIN = [[0, 0, 0],
               [0, 0, 0],
               [0, 0, 0]
               ]

PLAYER_WIDTH = len(PLAYER_SPRITE[0])
PLAYER_HEIGHT = len(PLAYER_SPRITE)

def draw_sprite(x, y, old_x, old_y, sprite):
    screen.move_sprite(sprite, old_x, old_y, x, y, COLOR, BACKGROUND_COLOR)
    sleep(PLAYER_MOVEMENT_SLEEP)

def draw_coin(xcoin, ycoin, COIN_SPRITE):
    screen.draw_matrix(COIN_SPRITE, xcoin, ycoin, COLOR_COIN)

def clear_coin(xcoin, ycoin, BLACKGROUND_COLOR):
     screen.draw_matrix(CLEAR_COIN, xcoin, ycoin, BLACKGROUND_COLOR)

def collision(xp, yp):
    global xcoin, ycoin
    player_border_left = xp - 2
    player_border_right = xp + 2
    player_border_top = yp + 2
    player_border_bottom = yp - 2
    coin_border_left = xcoin - 4
    coin_border_right = xcoin + 4
    coin_border_top = ycoin + 4
    coin_border_bottom = ycoin - 4
    if player_border_left >= coin_border_left and player_border_right <= coin_border_right and (player_border_bottom >= coin_border_bottom and player_border_top <= coin_border_top):
        clear_coin(xcoin, ycoin, BACKGROUND_COLOR)
        xcoin = random.randint(0, 128)
        ycoin = random.randint(0, 128)
        draw_coin(xcoin, ycoin, COIN_SPRITE)

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
            collision(xp, yp)
                
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
