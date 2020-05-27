import pygame   #calling pycharm module
pygame.init()   #initiating pygame module

gameDisplay = pygame.display.set_mode((800,600))    #setting up the screen
pygame.display.set_caption('example-1')     #title bar name
clock = pygame.time.Clock()     #declaring the time period to run

crashed = False     #declaring condition to stop

while not crashed:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:   #cancel red button
             crashed = True     #if game is closed, change condition

        print(event)    #displaying the status of the program

    pygame.display.update()     #to refresh the background data

    clock.tick(60)      #setting the frame speed

pygame.quit() #quitting pygame
quit() #quitting python
