import pygame
pygame.init()

display_x = 1000
display_y = 800

gameDisplay = pygame.display.set_mode((display_x,display_y))
pygame.display.set_caption('practise')
clock = pygame.time.Clock()

carImg = pygame.image.load('''E:\car.png''')
car_width = 260


def car(x,y):
    gameDisplay.blit(carImg,(x,y))


def game_loop():

    x = display_x * 0.4
    y = display_y * 0.3

    position_x = 0
    position_y = 0

    gameExit = False

    while not gameExit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    position_y = 5

                elif event.key == pygame.K_UP:
                    position_y = -5

                elif event.key == pygame.K_RIGHT:
                    position_x = 5

                elif event.key == pygame.K_LEFT:
                    position_x = -5

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT or event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    position_y = 0
                    position_x = 0

        x += position_x
        y += position_y

        gameDisplay.fill((180,156,96))
        car(x,y)

        if x > display_x - car_width or x < 0:
            gameExit = True

        pygame.display.update()
        clock.tick(60)

game_loop()
pygame.quit()
quit()