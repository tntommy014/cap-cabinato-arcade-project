from microbit import button_a, button_b, uart  # type: ignore[reportMissingModuleSource]
from st7735 import ST7735

SCREEN_WIDTH = 128
SCREEN_HEIGHT = 160
COLOR="#00FF00"
BACKGROUND_COLOR="#000000"

def main():
    x = SCREEN_WIDTH // 2
    y = SCREEN_HEIGHT // 2
    old_x = x
    old_y = y
    screen = ST7735()
    screen.draw_pixel(x=x, y=y, color=COLOR)
    
    while True:
        if button_a.is_pressed():
            x += 1
            screen.draw_pixel(x=old_x, y=old_y, color=BACKGROUND_COLOR)
            screen.draw_pixel(x=x, y=y, color=COLOR)
            old_x = x
        if button_b.is_pressed():
            x -= 1
            screen.draw_pixel(x=old_x, y=old_y, color=BACKGROUND_COLOR)
            screen.draw_pixel(x=x, y=y, color=COLOR)
            old_x = x
        
        

main()