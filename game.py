#Basic setup from https://www.pygame.org/docs/

# Example file showing a basic pygame "game loop"
import pygame
from pygame.locals import*

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
pygame.display.set_caption('TicTacToe')
running = True

#From https://www.youtube.com/watch?v=KBpfB1qQx8w
screen_width = 300
screen_height = 300

# Create board grid
def create_grid():
    bg_color = (209, 197, 192)
    grid_color = (50, 50, 50)
    screen.fill(bg_color)
    for x in range(1,3):
        pygame.draw.line(screen, grid_color, (x * 100, 0), (x * 100, screen_height))
        pygame.draw.line(screen, grid_color, (0, x * 100), (screen_width, x * 100))




while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("")

    create_grid()

    # RENDER YOUR GAME HERE

    # flip() the display to put your work on screen
    pygame.display.flip()

     # limits FPS to 60
