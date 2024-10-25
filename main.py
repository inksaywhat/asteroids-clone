import pygame
from constants import *
from player import Player 

def main():
    # Initialize pygame
    pygame.init()

    # Create the game window
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # Create a clock object to manage the game's FPS
    clock = pygame.time.Clock()

    # Delta time variable to keep track of time between frames
    dt = 0

    # Create a Player object and set initial position to the center of the screen
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    # Start the game loop (infinite loop)
    while True:
        # Event handling for quitting the game
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return  # Exit the game loop if the user closes the window

        # Fill the screen with black color
        screen.fill((0, 0, 0))

        # Draw the player on the screen
        player.draw(screen)

        # Refresh the display to show the black screen
        pygame.display.flip()

        # Cap the frame rate at 60 FPS and update delta time
        dt = clock.tick(60) / 1000  # Limits FPS to 60 and converts milliseconds to seconds

if __name__ == "__main__":
    main()
