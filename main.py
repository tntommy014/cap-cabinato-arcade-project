
from microbit import * # pyright: ignore[reportWildcardImportFromLibrary]
from st7735 import ST7735

SCREEN_WIDTH = 128
SCREEN_HEIGHT = 160
COLOR="#00FF00"
BACKGROUND_COLOR="#000000"
screen = None
draw_pixel = None

def draw_black(x, y):
    global screen
    screen.draw_pixel(x=x, y=y, color=COLOR)

def main():
    global screen
    global x
    global y
    xp = SCREEN_WIDTH // 2
    yp = SCREEN_HEIGHT // 2
    xjoy = 0
    yjoy = 0
    screen = ST7735()
    screen.draw_text(
        text="ciao sono Pippo\nche scoreggia a piu\nnon posso per tutta la citta",
        x=2,
        y=0,
        color="#0000FF",
    )
    screen.draw_pixel(x=x, y=y, color=COLOR)
    
    while True:
        if pin3.read_digital() == 1:
            x -= 1
            screen.draw_pixel(x=old_x, y=old_y, color="#000000")
            screen.draw_pixel(x=x, y=y, color="#00FF00")
            old_x = x
            old_y = y
main()