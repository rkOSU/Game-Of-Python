import pygame
import time
import random

pygame.init()

# TODO: Ask user for custom display length and height
disp_length = 400
disp_height = 400

disp = pygame.display.set_mode((disp_length, disp_height))
pygame.display.update()
pygame.display.set_caption("Game of Python by Raj")

# Colors
pink = (255, 153, 204)
black = (0, 0, 0)
white = (255, 255, 255)
yello =  (100, 100, 0)


# Font used in game
font = pygame.font.SysFont(None, 20)

clock = pygame.time.Clock()

def message(msg):
    mesg = font.render(msg, True, pink)

    # TODO: Make message output prettier

    disp.blit(mesg, [disp_length/2, disp_height/2])

def generate_food():
    return [round(random.randrange(0, disp_length - 10)/10) * 10, round(random.randrange(0, disp_height - 10)/10) * 10]
def game_loop():

    GAME_ENDING_FINAL = False
    GAME_ENDING_SOFT = False

    # Snake's coordinates on the center of the display
    x1 = disp_height / 2
    y1 = disp_length / 2

    x1_move = 0
    y1_move = 0

    # Generate Coordinates of food block
    food = generate_food()

    # List of coordinates which represent the snake's body
    snake_body = []
    snake_length = 1

    while not GAME_ENDING_FINAL:

        while GAME_ENDING_SOFT:
            disp.fill(white)
            message("Play Again: Y | Quit: N")
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    disp.fill(white)
                    if event.key == pygame.K_n:
                        GAME_ENDING_FINAL = True
                        GAME_ENDING_SOFT = False
                    if event.key == pygame.K_y:
                        game_loop()

        for event in pygame.event.get():
            # Print actions which are taking place on the screen
            #print(event)
            # Close the game when the user clicks on "X" button
            if event.type == pygame.QUIT:
                GAME_ENDING_FINAL = True
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

        # If snake hits the edge of the screen, then the game ends
        if x1 >= disp_length or x1 < 0 or y1 > disp_height or y1 < 0 and GAME_ENDING_FINAL == False:
            message("OH NO, you hit a wall!")
            pygame.display.update()

            time.sleep(2)
            GAME_ENDING_SOFT = True
        x1 += x1_move
        y1 += y1_move

        # Recolor display where the snake previously was
        disp.fill(black)

        # Structure to represent the head of the snake
        snake_front = []
        snake_front.append(x1)
        snake_front.append(y1)
        snake_body.append(snake_front)

        # Maintain snake's length
        if len(snake_body) > snake_length:
            del snake_body[0]

        # Check if snake has crossed itself
        for x in snake_body[:-1]:
            if x == snake_front:
                # End game if snake bit itself
                message("OH NO, you bit yourself!")
                pygame.display.update()

                time.sleep(2)
                GAME_ENDING_SOFT = True

        # Draw snake block by block
        for x in snake_body:
            pygame.draw.rect(disp, pink, [x[0], x[1], 10, 10])

        # Draw food
        pygame.draw.rect(disp, yello, [food[0], food[1], 10, 10])
        pygame.display.update()

        # Increase snake length when it eats food
        if x1 == food[0] and y1 == food[1]:
            food = generate_food()
            snake_length += 1

        clock.tick(10)

    pygame.quit()
    quit()


game_loop()

