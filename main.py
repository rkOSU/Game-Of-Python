import pygame
pygame.init()
disp = pygame.display.set_mode((400,300))
pygame.display.update()
pygame.display.set_caption("Game of Python by Raj")
END_GAME = False

#Colors

pink = (255, 153, 204)

while not END_GAME:
    for event in pygame.event.get():
        #Print actions which are taking place on the screen
        print(event)
        #Close the game when the user clicks on "X" button
        if event.type == pygame.QUIT:
            END_GAME = True
        #Handle Key Inputs
    #Draw the python using a colored rectangle
    pygame.draw.rect(disp, pink, [200, 150, 10, 10])
    pygame.display.update()

pygame.quit()
quit()

