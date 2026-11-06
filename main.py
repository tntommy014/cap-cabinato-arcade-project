
from microbit import *  # pyright: ignore[reportMissingModuleSource]
from st7735 import ST7735

SCREEN_WIDTH = 160
SCREEN_HEIGHT = 128
COLOR="#00FF00"
BACKGROUND_COLOR="#000000"
PLAYER_MOVEMENT_SLEEP = 30

xp = SCREEN_WIDTH // 2
yp = SCREEN_HEIGHT // 2
old_xp = xp
old_yp = yp

def draw_player(x, y, old_x, old_y):
    screen.draw_pixel(x=old_x, y=old_y, color=BACKGROUND_COLOR)
    screen.draw_pixel(x=x, y=y, color=COLOR)
    sleep(PLAYER_MOVEMENT_SLEEP)

def main():
    try:
        global screen, xp, yp, old_xp, old_yp
        screen = ST7735()
        display.off()
        # screen.draw_text(
        #     text="ciao sono Pippo\nche scoreggia a piu\nnon posso per tutta la citta",
        #     x=2,
        #     y=0,
        #     color="#0000FF",
        # )
        screen.draw_pixel(x=xp, y=yp, color=COLOR)
        pin3.set_pull(pin3.PULL_DOWN)
        pin4.set_pull(pin4.PULL_DOWN)
        pin7.set_pull(pin7.PULL_DOWN)
        pin6.set_pull(pin6.PULL_DOWN)
        
        while True:
            jup = pin3.read_digital()
            jdown = pin4.read_digital()
            jleft = pin7.read_digital()
            jright = pin6.read_digital()
            if jup == 1:
                old_yp = yp
                old_xp = xp
                yp -= 1 
                draw_player(xp, yp, old_xp, old_yp)
            if jdown == 1:
                old_yp = yp
                old_xp = xp
                yp += 1
                draw_player(xp, yp, old_xp, old_yp)
            if jleft == 1:
                old_xp = xp
                old_yp = yp
                xp -= 1
                draw_player(xp, yp, old_xp, old_yp)
            if jright == 1:
                old_xp = xp
                old_yp = yp
                xp += 1
                draw_player(xp, yp, old_xp, old_yp)
            # uart.write("jup = " + str(jup) + " jdown = " + str(jdown) + " jleft = " + str(jleft) + " jright = " + str(jright) + "\n")
            # uart.write("xp = " + str(xp) + " yp = " + str(yp) + "\n")

                
    except Exception as e:
                uart.write(repr(e))
            
main()