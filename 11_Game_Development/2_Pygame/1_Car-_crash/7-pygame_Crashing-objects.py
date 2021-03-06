import pygame
import time
import random

pygame.init()

display_x = 1000
display_y = 600

gameDisplay = pygame.display.set_mode((display_x,display_y))
pygame.display.set_caption('GameOn')
clock = pygame.time.Clock()

carImg = pygame.image.load('''E:\car.png''')
carWidth = 240

def car(x,y):
    gameDisplay.blit(carImg,(x,y))

def things(thingx, thingy, thingw, thingh, color):
    pygame.draw.rect(gameDisplay, color, [thingx,thingy, thingw, thingh])


def text_object(text, font):
    textSurface = font.render(text, True, (255,0,0))
    return textSurface, textSurface.get_rect()

def message_display(text):
    largeText = pygame.font.Font('freesansbold.ttf',120)
    TextSurf, TextRect = text_object(text, largeText)
    TextRect.center = ((display_x/2),(display_y/2))

    gameDisplay.blit(TextSurf,TextRect)

    pygame.display.update()
    time.sleep(2)
    gameloop()

def crash():
    message_display('!! You crashed !!')

def gameloop():
    x = display_x * 0.5
    y = display_y * 0.1


    x_position = 0
    y_position = 0

    thing_startx = random.randrange(0, display_x)
    thing_starty = -600
    thing_speed = 5
    thing_width = 100
    thing_height = 100

    gameExit = False

    while not gameExit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_position = -5

                elif event.key == pygame.K_RIGHT:
                    x_position = 5

                elif event.key == pygame.K_UP:
                    y_position = -5

                elif event.key == pygame.K_DOWN:
                    y_position = 5

            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT or event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    x_position = 0
                    y_position = 0

        x += x_position
        y += y_position

        gameDisplay.fill((190,200,63))

        #things(thingx, thingy, thingw, thingh, color)
        things(thing_startx,thing_starty, thing_width, thing_height, (30,50,185))
        thing_starty += thing_speed

        car(x,y)

        if x < 0 or x > display_x - carWidth:
            crash()

        if thing_starty > display_y:
            thing_starty = 0 - thing_height
            thing_startx = random.randrange(0, display_x)

        if y < thing_starty + thing_height:
            print('y crosspver')
            if x > thing_startx and x < thing_startx+thing_width or x+carWidth>thing_startx and x+carWidth<thing_startx+thing_width:
                print('x crossover')
                crash()

        pygame.display.update()
        clock.tick(60)



gameloop()
pygame.quit()
quit()