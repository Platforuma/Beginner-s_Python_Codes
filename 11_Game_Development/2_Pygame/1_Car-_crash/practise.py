import pygame
import time
import random

pygame.init()

display_x = 800
display_y = 600

gameDisplay = pygame.display.set_mode((display_x,display_y))
pygame.display.set_caption("Game")
clock = pygame.time.Clock()

carImg = pygame.image.load("E:\car.png")
ImgWidth = 98
ImgHeight = 176

def car(x,y):
    gameDisplay.blit(carImg,(x,y))

def gameloop():

    position_x = 0
    position_y = 0

    x = display_x * 0.5
    y = display_y * 0.6

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
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT or event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    position_x = 0
                    position_y = 0


            x += position_x
            y += position_y

            gameDisplay.fill((10,60,120))
            car(x,y)

            pygame.display.update()
            clock.tick(60)



gameloop()
pygame.quit()
quit()

