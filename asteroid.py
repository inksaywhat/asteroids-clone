import random
import pygame
from constants import ASTEROID_MIN_RADIUS

class Asteroid(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        super().__init__()
        self.position = pygame.Vector2(x, y)
        self.radius = radius
        self.velocity = pygame.Vector2(random.uniform(-1, 1), random.uniform(-1, 1))

    def split(self):
        # Kill the current asteroid
        self.kill()

        # If the asteroid is too small, stop here
        if self.radius <= ASTEROID_MIN_RADIUS:
            return

        # Generate a random angle between 20 and 50 degrees
        random_angle = random.uniform(20, 50)

        # Calculate the new radius of the smaller asteroids
        new_radius = self.radius - ASTEROID_MIN_RADIUS

        # Create two new velocity vectors rotated from the original
        velocity_1 = self.velocity.rotate(random_angle) * 1.2
        velocity_2 = self.velocity.rotate(-random_angle) * 1.2

        # Create two new asteroids at the current position with new velocities and radius
        new_asteroid_1 = Asteroid(self.position.x, self.position.y, new_radius)
        new_asteroid_1.velocity = velocity_1

        new_asteroid_2 = Asteroid(self.position.x, self.position.y, new_radius)
        new_asteroid_2.velocity = velocity_2

        # Add the new asteroids to the appropriate groups
        new_asteroid_1.add(self.containers)
        new_asteroid_2.add(self.containers)

