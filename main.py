
from microbit import *  # pyright: ignore[reportMissingModuleSource]
from st7735 import ST7735

SCREEN_WIDTH = 128
SCREEN_HEIGHT = 160
COLOR="#00FF00"
BACKGROUND_COLOR="#000000"

def draw_black(x, y):
    global screen
    screen.draw_pixel(x=x, y=y, color=COLOR)

def main():
    try:
        global screen
        global x
        global y
        xp = SCREEN_WIDTH // 2
        yp = SCREEN_HEIGHT // 2
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
        
        while True:
            if pin3.read_digital() == 1:
                yp -= 1
                screen.draw_pixel(x=old_xp, y=old_yp, color="#000000")
                screen.draw_pixel(x=xp, y=yp, color="#00FF00")
                old_xp = xp
                old_yp = yp
                
    except Exception as e:
                uart.write(repr(e))
            
main()