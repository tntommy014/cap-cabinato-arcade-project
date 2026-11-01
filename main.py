
from microbit import *  # pyright: ignore[reportMissingModuleSource]
from st7735 import ST7735

SCREEN_WIDTH = 128
SCREEN_HEIGHT = 160
COLOR="#00FF00"
BACKGROUND_COLOR="#000000"
PLAYER_MOVEMENT_SLEEP = 30

def main():
    try:
        global screen
        global x
        global y
        yp = SCREEN_WIDTH // 2
        xp = SCREEN_HEIGHT // 2
        old_xp = xp
        old_yp = yp
        screen = ST7735()
        display.off()
        uart.init(baudrate=115200)
        uart.write('hello world')
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
                xp -= 1
                screen.draw_pixel(x=old_xp, y=old_yp, color="#000000")
                screen.draw_pixel(x=xp, y=yp, color="#00FF00")
                old_xp = xp
                old_yp = yp
                sleep(PLAYER_MOVEMENT_SLEEP)
            if jdown == 1:
                xp += 1
                screen.draw_pixel(x=old_xp, y=old_yp, color="#000000")
                screen.draw_pixel(x=xp, y=yp, color="#00FF00")
                old_xp = xp
                old_yp = yp
                sleep(PLAYER_MOVEMENT_SLEEP)
            if jleft == 1:
                yp += 1
                screen.draw_pixel(x=old_xp, y=old_yp, color="#000000")
                screen.draw_pixel(x=xp, y=yp, color="#00FF00")
                old_xp = xp
                old_yp = yp
                sleep(PLAYER_MOVEMENT_SLEEP)
            if jright == 1:
                yp -= 1
                screen.draw_pixel(x=old_xp, y=old_yp, color="#000000")
                screen.draw_pixel(x=xp, y=yp, color="#00FF00")
                old_xp = xp
                old_yp = yp
                sleep(PLAYER_MOVEMENT_SLEEP)

            
            
            # uart.write("jup = " + str(jup) + " jdown = " + str(jdown) + " jleft = " + str(jleft) + " jright = " + str(jright) + "\n")
                
    except Exception as e:
                uart.write(repr(e))
            
main()