import pygame as gm
from pygame.locals import *
import time
import random

gm.init()

# assigning values to color
red = (255,0,0)
blue = (51,153,255)
grey = (192,192,192)
green = (51,102,0)
yellow = (0,255,255)

# window dimension
win_height = 400
win_width = 600
window = gm.display.set_mode((win_width,win_height))

# Title of the game
gm.display.set_caption("Snake Game")
# time.sleep(2)


snake = 10 
snake_speed = 10

clock = gm.time.Clock()

font_style = gm.font.SysFont('corbel',26)
score_font = gm.font.SysFont('comicsansms',30)

def user_score(score):
    number = score_font.render('Score: ', score, True, red)
    window.blit(number, [0,0])

def game_snake(snake, snake_length_list):
    for x in snake_length_list:
        gm.draw.rect(window,green,[x[0],x[1],snake,snake])

def message(msg):
    msg = font_style.render(msg, True, red)
    window.blit(msg, [win_width/6, win_height/3])    
    
def game_loop():
    gameOver = False
    gameClose = False
    
    x1 = win_width/2
    y1 = win_height/2
    
    x1_change = 0
    y1_change = 0
    
    snake_length_list = []
    snake_length = 1
    
    foodx = round(random.randrange(0, win_width-snake)/10.0)*10.0
    foody = round(random.randrange(0, win_height-snake)/10.0)*10.0

    while not gameOver:
        
        while gameClose == True:
            window.fill(grey)
            message('You lost!! press P to Play again and Q to Quit the game')
            user_score(snake_length-1)
            gm.display.update()
            
            for event in gm.event.get():
                if event.type == gm.KEYDOWN:
                    if event.key == gm.K_q:
                        gameOver = True
                        gameClose = True
                    if event.key == gm.K_p:
                        game_loop()
        
        for event in gm.event.get():
            if event.type == gm.KEYDOWN:
                if event.key == K_LEFT:
                    x1_change = -snake
                    y1_change = 0
                elif event.key == K_RIGHT:
                    x1_change = snake
                    y1_change = 0
                elif event.key == K_UP:
                    x1_change = 0
                    y1_change = -snake
                elif event.key == K_DOWN:
                    x1_change = 0
                    y1_change = snake
        
        if x1 > win_width or x1 < 0 or y1 > win_height or y1 < 0:
            gameClose = True
            
        x1 += x1_change
        y1 += y1_change
        window.fill(grey)
        gm.draw.rect(window, yellow, [foodx, foody,snake,snake])
        snake_size = []
        snake_size.append(x1)
        snake_size.append(y1)
        snake_length_list.append(snake_size)
        if len(snake_length_list)>snake_length:
            del snake_length_list[0]
            
        game_snake(snake, snake_length_list)
        user_score(snake_length - 1)
        
        gm.display.update()
        
        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, win_width-snake)/10.0)*10.0
            foody = round(random.randrange(0, win_height-snake)/10.0)*10.0
            snake_length += 1
        clock.tick(snake_speed)
                    
    gm.quit()
    quit()
    
game_loop()