from ball import Ball
from paddle import Paddle
import pygame
import random
import math

def main():
    pygame.init()
    pygame.display.set_caption("My Pong")

    #create a surface
    WIDTH = 800
    HEIGHT = 400
    BORDER = 15
    VELOCITY = 5
    FPS = 60


    screen = pygame.display.set_mode((WIDTH, HEIGHT))

    #add solid background r, g, b
    screen.fill((0,0,0))
    #double buffering: stage all changes and update them all at once
    #avoid flickering
    pygame.display.update()

    #Draw walls as rectangles
    # https://www.pygame.org/docs/ref/draw.html#pygame.draw.rect
    # rect(surface, color, rect) -> Rect
    # Rect((left, top), (width)) -> Rect
    wcolor = pygame.Color("white")
    bgcolor = pygame.Color("Black")
    #top wall
    pygame.draw.rect(screen, wcolor, pygame.Rect((0, 0), (WIDTH,BORDER)))
    #left wall
    pygame.draw.rect(screen, wcolor, pygame.Rect((0, 0), (BORDER, HEIGHT)))
    #bottom
    #Homework: needs, Height, Border, Width and some algebra
    pygame.draw.rect(screen, wcolor, pygame.Rect((0, HEIGHT-BORDER), (WIDTH, BORDER)))
    
    #ball init
    x0 = WIDTH - Ball.RADIUS
    y0 = (HEIGHT // 2)
    vx0 = -VELOCITY
    vy0 = random.randrange(-VELOCITY, VELOCITY, 1)
    #TODO: +/- 45 degree/random

    b0 = Ball(x0, y0, vx0, vy0, screen, wcolor, bgcolor, BORDER, HEIGHT - BORDER)
    b0.show(wcolor)

    # define a variable to control the main loop
    running = True
    clock = pygame.time.Clock()
    # main loop
    count = 0
    while running:
        count+= 1
        # event handling, gets all event from the event queue
        for event in pygame.event.get():
            
            # only do something if the event is of type QUIT
            if event.type == pygame.QUIT:
                # change the value to False, to exit the main loop
                running = False

        pygame.display.update() #flip?
        clock.tick(FPS)
        #Ball
        b0.update()

if __name__=="__main__":
    # call the main function
    main()
