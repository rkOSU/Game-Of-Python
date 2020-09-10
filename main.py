import pygame
pygame.init()
disp = pygame.display.set_mode((400, 400))
pygame.display.update()
pygame.display.set_caption("Game of Python by Raj")
END_GAME = False

# Colors
pink = (255, 153, 204)
black = (0, 0, 0)
# Snake's coordinates on the display
x1 = 300
y1 = 300

x1_move = 0
y1_move = 0
clock = pygame.time.Clock()

while not END_GAME:
    for event in pygame.event.get():
        # Print actions which are taking place on the screen
        print(event)
        # Close the game when the user clicks on "X" button
        if event.type == pygame.QUIT:
            END_GAME = True
        # Handle key inputs
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                # Move snake left
                x1_move = -10
                y1_move = 0
            elif event.key == pygame.K_DOWN:
                # Move snake down
                x1_move = 0
                y1_move = 10
            elif event.key == pygame.K_RIGHT:
                # Move snake right
                x1_move = 10
                y1_move = 0
            elif event.key == pygame.K_UP:
                # Move snake up
                x1_move = 0
                y1_move = -10

    x1 += x1_move
    y1 += y1_move

    # Recolor display where the snake previously was
    disp.fill(black)
    # Draw the python using a colored rectangle
    pygame.draw.rect(disp, pink, [x1, y1, 10, 10])
    pygame.display.update()

    clock.tick(3)

pygame.quit()
quit()

