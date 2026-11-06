
from microbit import *  # pyright: ignore[reportMissingModuleSource]
from st7735 import ST7735

SCREEN_WIDTH = 160
SCREEN_HEIGHT = 128
COLOR="#00FF00"
BACKGROUND_COLOR="#000000"
PLAYER_MOVEMENT_SLEEP = 1

# PLAYER_SPRITE = [[0, 1, 0],
#                  [1, 1, 1],
#                  [0, 1, 0]]

PLAYER_SPRITE = [[0, 1, 1, 1, 0],
                 [1, 1, 0, 1, 1],
                 [1, 1, 0, 1, 1],
                 [0, 1, 1, 1, 0]]

def draw_sprite(x, y, old_x, old_y, sprite):
    screen.move_sprite(sprite, old_x, old_y, x, y, COLOR, BACKGROUND_COLOR)
    sleep(PLAYER_MOVEMENT_SLEEP)

def main():
    try:
        global screen
        screen = ST7735()
        display.off()
        pin3.set_pull(pin3.PULL_DOWN)
        pin4.set_pull(pin4.PULL_DOWN)
        pin7.set_pull(pin7.PULL_DOWN)
        pin6.set_pull(pin6.PULL_DOWN)
        
        xp = SCREEN_WIDTH // 2 - len(PLAYER_SPRITE[0]) // 2
        yp = SCREEN_HEIGHT // 2 - len(PLAYER_SPRITE) // 2
        
        screen.draw_matrix(PLAYER_SPRITE, xp, yp, COLOR)

        while True:
            jup = pin3.read_digital()
            jdown = pin4.read_digital()
            jleft = pin7.read_digital()
            jright = pin6.read_digital()
            if jup == 1:
                old_yp = yp
                old_xp = xp
                yp -= 1 
                draw_sprite(xp, yp, old_xp, old_yp, PLAYER_SPRITE)
            if jdown == 1:
                old_yp = yp
                old_xp = xp
                yp += 1
                draw_sprite(xp, yp, old_xp, old_yp, PLAYER_SPRITE)
            if jleft == 1:
                old_xp = xp
                old_yp = yp
                xp -= 1
                draw_sprite(xp, yp, old_xp, old_yp, PLAYER_SPRITE)
            if jright == 1:
                old_xp = xp
                old_yp = yp
                xp += 1
                draw_sprite(xp, yp, old_xp, old_yp, PLAYER_SPRITE)
                
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
