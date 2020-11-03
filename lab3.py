import pygame
from paddle import Paddle
from ball import Ball
from collections import namedtuple
import random

def main():
    pygame.init()
    pygame.display.set_caption('my pong')

    WIDTH = 800
    HEIGHT = 400
    BORDER = 15
    VELOCITY = 5
    FPS = 30

    MyConstants = namedtuple("MyConstants", ['WIDTH', 'HEIGHT', 'BORDER', 'VELOCITY', 'FPS'])
    CONSTS = MyConstants(WIDTH, HEIGHT, BORDER, VELOCITY, FPS)

    #surface
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    screen.fill((0,0,0))
    #double buffering: stage updates together; update them at once
    #avoids flickering
    pygame.display.update()

    #walls
    # Rect(surface, color, rect) -> Rect
    # Rect((left, top), (width, height)) -> Rect
    wcolor = pygame.Color('blue')
    bgcolor = pygame.Color('black')
    
    #top wall
    pygame.draw.rect(screen, wcolor, pygame.Rect((0, 0), (WIDTH, BORDER)))
    #left wall
    pygame.draw.rect(screen, wcolor, pygame.Rect((0, 0), (BORDER, HEIGHT)))
    #bottom wall
    pygame.draw.rect(screen, wcolor, pygame.Rect((0, HEIGHT-BORDER), (WIDTH, BORDER)))

    #Ball init
    x0 = WIDTH - Ball.RADIUS
    y0 = HEIGHT // 2
    vx0 = -VELOCITY
    plusminus = [-1,1]
    vy0 = VELOCITY * random.choice(plusminus)
    #TODO: pick +/- init velocity of 45deg 

    b0 = Ball(x0,y0, vx0,vy0, screen, wcolor, bgcolor, CONSTS)
    b0.show(wcolor)


    pygame.display.update()
    # define a variable to control the main loop
    running = True
    clock = pygame.time.Clock()    
    # main loop
    while running:
        # event handling, gets all event from the event queue
        for event in pygame.event.get():
            # only do something if the event is of type QUIT
            if event.type == pygame.QUIT:
                # change the value to False, to exit the main loop
                running = False
            pygame.display.update()
            clock.tick(FPS)
            #Ball
            b0.update()
    #done
if __name__=='__main__':
    main()