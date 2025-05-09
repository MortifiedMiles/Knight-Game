# 1 - Import packages
import pygame
from pygame.locals import *
import sys
from Knight import knight
from Arrow import arrow
from simpleText import simpleText
from background import background
import math

# 2 - Define constants
BLACK = (0, 0, 0)
WINDOW_WIDTH = 640
WINDOW_HEIGHT = 640
FRAMES_PER_SECOND = 30

# 3 - Initialize the world
pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
#image = pygame.transform.scale(pygame.image.load(os.path.join(BASE_PATH, image)).convert(), (WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()
 
# 4 - Load assets: image(s), sound(s),  etc.
arrows = []
player = knight(window, 'Images/Knight3.png')

# 5 - Initialize variables
second = 0
dt = 0
minute = 0
# 6 - Loop forever
running = True
while True:
    if running:

        # 7 - Check for and handle events
        for event in pygame.event.get():
            # Clicked the close button? Quit pygame and end the program 
            if event.type == QUIT:           
                pygame.quit()  
                sys.exit()
                

        # 8  Do any "per frame" actions
        player.manual_move()
        if second/60 >= 1:
            minute = math.floor(minute/60)
        for objArrow in arrows:
            objArrow.continuous_move()
            if player.collide(value = objArrow):
                running = False
        
        if dt%7 == 0:
            for rep in range(1):
                arrows.append(arrow(window))

        # 9 - Clear the window
        window.fill(BLACK)

        # 10 - Draw all window elements
        upScroller = dt/30
        tower = background(window, 'Images/Tower-1.png.png', 0, upScroller)
        tower.draw()
        player.draw(dt)
        [rep.draw() for rep in arrows]
        timer = simpleText(window, f"{minute}:{math.floor((second/3)%60)}")
        timer.draw()
        
        # 11 - Update the window
        pygame.display.update()

        # 12 - Slow things down a bit
        clock.tick(FRAMES_PER_SECOND) # make pygame wait
        second += 0.1
        dt = round(second, 1)
    
    else:
        # 7 - Check for and handle events
        for event in pygame.event.get():
            # Clicked the close button? Quit pygame and end the program 
            if event.type == QUIT:           
                pygame.quit()  
                sys.exit()
            
            if event.type == KEYUP and event.key == K_SPACE:
                arrows = []
                dt = 0
                running = True
        
        # 8  Do any "per frame" actions

        # 9 - Clear the window
        window.fill(BLACK)

        # 10 - Draw all window elements
        gameOver = simpleText(window, "Game Over", 0, 0, 'Comic Sans MS', 25)
        gameOver.draw()
        pressContinue = simpleText(window, "Press Space Bar To Continue", 0, 55, 'Comic Sans MS', 25)
        pressContinue.draw()

        # 11 - Update the window
        pygame.display.update()

        # 12 - Slow things down a bit
        clock.tick(FRAMES_PER_SECOND)
