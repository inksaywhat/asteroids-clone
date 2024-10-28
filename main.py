import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    # Initialize pygame
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    # Create groups to manage game objects
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    # Set up static containers for Player, Asteroid, and AsteroidField classes
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable,)
    shots.containers = (shots, updatable, drawable)

    # Create game objects
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()

    # Delta time variable
    dt = 0

    # Start the game loop
    while True:
        # Event handling for quitting the game
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        # Update all objects in the updateable group
        for obj in updatable:
            obj.update(dt)

        # Collision detection: check if player collides with any asteroid
        for asteroid in asteroids:
            if player.collides_with(asteroid):
                print("Game over!")
                return  # Exit the game loop if a collision is detected

        # Fill the screen with black color
        screen.fill("black")

        # Draw all objects in the drawable group
        for obj in drawable:
            obj.draw(screen)

        # Refresh the display
        pygame.display.flip()

        # Cap the frame rate at 60 FPS and update delta time
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()
