import pygame
from constants import *

def main():
    # Initialize pygame
    pygame.init()

    # Create the game window
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # Start the game loop (infinite loop)
    while True:
        # Event handling for quitting the game
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return  # Exit the game loop if the user closes the window

        # Fill the screen with black color
        screen.fill((0, 0, 0))

        # Refresh the display to show the black screen
        pygame.display.flip()

if __name__ == "__main__":
    main()

