
from random import randint, random
import random

from microbit import *
import microbit  # pyright: ignore[reportMissingModuleSource]
from st7735 import ST7735

SCREEN_WIDTH = 160
SCREEN_HEIGHT = 128
BORDER_WIDTH = 8
MAX_X = SCREEN_WIDTH - BORDER_WIDTH
MAX_Y = SCREEN_HEIGHT - BORDER_WIDTH
COLOR="#00FF00"
BACKGROUND_COLOR="#000000"
COLOR_COIN = "#FFFF00"
TEXT_COLOR = "#FF0000"
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

PLAYER_WIDTH = len(PLAYER_SPRITE[0])
PLAYER_HEIGHT = len(PLAYER_SPRITE)



def init():
    global screen
    screen = ST7735()
    display.off()
    pin3.set_pull(pin3.PULL_DOWN)
    pin4.set_pull(pin4.PULL_DOWN)
    pin7.set_pull(pin7.PULL_DOWN)
    pin6.set_pull(pin6.PULL_DOWN)
    pin8.set_pull(pin8.PULL_DOWN)
    
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

def draw_player(x, y):
    screen.draw_sprite(PLAYER_SPRITE, x, y, COLOR)

def move_player(x, y, old_x, old_y):
    screen.move_sprite(PLAYER_SPRITE, old_x, old_y, x, y, COLOR, BACKGROUND_COLOR)
    sleep(PLAYER_MOVEMENT_SLEEP)

def draw_coin(x, y):
    screen.draw_sprite(COIN_SPRITE, x, y, COLOR_COIN)

def clear_coin(x, y):
    screen.clear_sprite(COIN_SPRITE, x, y)

def draw_timer(time):
    screen.draw_text(
        text= str(time),
        x=100,
        y=0,
        color=TEXT_COLOR
        )
    
def update_timer(timer, timer_last_update):
    now = running_time() # ignoralo
    # qui entra ogni 1000 millisecondi, quindi ogni secondo
    if now - timer_last_update >= 1000:
        timer += 1 # incremento il timer di 1 secondo, cambia questo se vuoi farlo decrementare
        timer_last_update = now # ignoralo
        draw_timer(timer) # disegno il timer
    return timer, timer_last_update # serve per avere i valori aggiornati nel while True

def update_score(score):
    screen.draw_text(
        text=str(score),
        x=61,
        y=0,
        color=TEXT_COLOR
        )

def read_joystick():
    jup = pin3.read_digital()
    jdown = pin4.read_digital()
    jleft = pin7.read_digital()
    jright = pin6.read_digital()
    return jup, jdown, jleft, jright

def reset_pressed():
    return pin8.read_digital() == 1

def update_player(xp, yp):
    jup, jdown, jleft, jright = read_joystick()
    if jup == 1:
        old_xp, old_yp = xp, yp
        yp = max(yp - 1, BORDER_WIDTH)
        move_player(xp, yp, old_xp, old_yp)
    if jdown == 1:
        old_xp, old_yp = xp, yp
        yp = min(yp + 1, MAX_Y)
        move_player(xp, yp, old_xp, old_yp)
    if jleft == 1:
        old_xp, old_yp = xp, yp
        xp = max(xp - 1, BORDER_WIDTH)
        move_player(xp, yp, old_xp, old_yp)
    if jright == 1:
        old_xp, old_yp = xp, yp
        xp = min(xp + 1, MAX_X)
        move_player(xp, yp, old_xp, old_yp)
    return xp, yp # serve per avere i valori aggiornati nel while True

def main():
    try:
        global screen
        # ho spostato qui dentro tutti i ciaffi di preparazione
        init()
        
        xp = SCREEN_WIDTH // 2 - PLAYER_WIDTH // 2
        yp = SCREEN_HEIGHT // 2 - PLAYER_HEIGHT // 2
        xcoin = random.randint(BORDER_WIDTH, MAX_X)
        ycoin = random.randint(BORDER_WIDTH, MAX_Y)
        punteggio = 0
        
        draw_player(xp, yp)
        draw_coin(xcoin, ycoin)

        screen.draw_text(
            text="PUNTEGGIO:" + str(punteggio),
            x=2,
            y=0,
            color=TEXT_COLOR
            )
        
        # un esempio di timer
        timer = 0 # cambia questo se vuoi farlo partire da un certo numero di secondi
        timer_last_update = running_time() # questo te lo spiego poi bene
        draw_timer(timer)
        
        while True:
            # anche questa te la spiego poi bene ma guarda dentro update_timer
            timer, timer_last_update = update_timer(timer, timer_last_update)
            
            # ho messo qui dentro tutta la parte del joystick per il player
            xp, yp = update_player(xp, yp)
            
            if are_colliding((PLAYER_SPRITE, xp, yp), (COIN_SPRITE, xcoin, ycoin)):
                clear_coin(xcoin, ycoin)
                xcoin = random.randint(BORDER_WIDTH, MAX_X)
                ycoin = random.randint(BORDER_WIDTH, MAX_Y)
                punteggio += 10
                update_score(punteggio)
                draw_coin(xcoin, ycoin)
            
            # ho spostato qui dentro il controllo sul pin8    
            if reset_pressed():
                microbit.reset()
                
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
