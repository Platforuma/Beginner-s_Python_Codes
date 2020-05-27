import pygame
import time
import random

pygame.init()

display_x = 800
display_y = 600

gameDisplay = pygame.display.set_mode((display_x,display_y))
pygame.display.set_caption('Practise')
clock = pygame.time.Clock()

carImg = pygame.image.load('E:\car.png')
ImgWidth = 98
ImgHeight =  176

def things_dodged(count):
    font = pygame.font.SysFont(None, 25)
    text = font.render("Dodged: "+str(count), True, (25,255,255))
    gameDisplay.blit(text,(0,0))

def car(x,y):
    gameDisplay.blit(carImg,(x,y))

def things(thingx, thingy, thingw, thingh, color):
    pygame.draw.rect(gameDisplay, color, [thingx, thingy, thingw, thingh])

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
    y = display_y * 0.2

    position_x = 0
    position_y = 0

    thing_startx = random.randrange(0,display_x)
    thing_starty = -600
    thing_speed = 3
    thing_width = 100
    thing_height = 100

    dodged = 0

    gameExit = False

    while not gameExit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    position_x = -5
                elif event.key == pygame.K_RIGHT:
                    position_x = 5
                elif event.key == pygame.K_UP:
                    position_y = -5
                elif event.key == pygame.K_DOWN:
                    position_y = 5
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_DOWN or event.key == pygame.K_UP or event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT:
                    position_x = 0
                    position_y = 0

        x += position_x
        y += position_y

        gameDisplay.fill((123,80,30))

        things(thing_startx, thing_starty, thing_width, thing_height, (30,210, 80))
        thing_starty += thing_speed

        car(x,y)

        things_dodged(dodged)

        if x < 0 or x > display_x - ImgWidth:
            crash()

        if thing_starty > display_y:
            thing_starty = 0 - thing_height
            thing_startx = random.randrange(0, display_x - thing_width)
            dodged += 1
            # thing_speed += 1




        if y < thing_starty + thing_height and y + ImgHeight > thing_starty:
            print('y-crossover')
            if x > thing_startx and x < thing_startx+thing_width or thing_startx>x and thing_startx<x+ImgWidth:
                print('x-crossover')
                crash()

        pygame.display.update()
        clock.tick(60)

gameloop()
pygame.quit()
quit()