# import the pygame module, so you can use it
import pygame
import random
import time
import math
 
# height and width must be devisible by tile_side
#height = 260
#width = 300
time_step = 0.1
tile_side = 20
height = 20*tile_side
width = 30*tile_side
w= width/tile_side
h= height/tile_side
# define a main function
def main():
    direction=1
    correction =0
    snake = [0, 1, 2]
    applepos=random.randint(3,h*w-1)
    # define a variable to control the main loop and stuff
    running = True
    check = True

    # initialize the pygame module
    pygame.init()
    pygame.display.set_caption("snake")
    # create a surface on screen that has the size of what we specify
    screen = pygame.display.set_mode((width,height))
    #loading images
    image = pygame.image.load("basic tile.bmp")
    image_apple = pygame.image.load("apple.bmp")
    image_head = pygame.image.load("blue.bmp")
    r = 60
    g = 60
    b = 60

    # main loop
    while running:
        old_direction=direction
        time.sleep(time_step)
        screen.fill((r,g,b))
        # event handling, gets all event from the event queue
        for event in pygame.event.get():
            # only do something if the event is of type QUIT
            if event.type == pygame.QUIT:
                # change the value to False, to exit the main loop
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT :
                    direction = -1
                elif event.key == pygame.K_RIGHT:
                    direction = 1
                elif event.key == pygame.K_UP:
                    direction = -w
                elif event.key == pygame.K_DOWN:
                    direction = w
                elif event.key == pygame.K_q :
                    running = False
        #this makes it impossible for snake to go back into itself
        if not old_direction+direction:
            direction=old_direction
        #here I want to make the snake go back exactly from the other side
        if (snake[-1]+direction) % w == 0 and direction == 1:
            correction = -w
        if snake[-1] % w == 0 and direction == -1:
            correction = +w
        if direction == -w and math.floor(snake[-1]/w)==0:
            correction = +w*h
        if direction == w and math.floor(snake[-1]/w)==h-1:
            correction = -w*h
        #snake moves here
        snake.append(snake[-1]+direction+correction)
        correction = 0
        #making snake longer when it eats an apple and generating new ones
        if applepos == snake[-1]:
            #we need to guard for apples not to generate in the snake
            while check:
                applepos=random.randint(0,h*w-1)
                check = False
                for x in snake:
                    if x == applepos:
                        check = True
            check = True
        else:
            snake.pop(0)
        #we need a reset when snake eats itself
        reset = 0
        for x in snake:
            if x == snake[-1]:
                reset += 1
        if reset > 1:
            direction=1
            snake = [0, 1, 2]
            applepos=random.randint(3,h*w-1)
            correction = 0
            reset = 0

        #displaying stuff
        for x in snake:
            screen.blit(image, (x%w*tile_side,(math.floor(x/w))*tile_side))
        screen.blit(image_apple, (applepos%w*tile_side,tile_side*math.floor(applepos/w)))
        screen.blit(image_head, (snake[-1]%w*tile_side,tile_side*math.floor(snake[-1]/w)))
        pygame.display.flip()

# run the main function only if this module is executed as the main script
# (if you import this as a module then nothing is executed)
if __name__=="__main__":
    # call the main function
    main()
