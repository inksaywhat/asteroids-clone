import random
import pygame
from constants import ASTEROID_MIN_RADIUS

class Asteroid(pygame.sprite.Sprite):
    # Your existing Asteroid class code here

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

        # Create two new asteroids at the current position with new velocities
        new_asteroid_1 = Asteroid(self.position.x, self.position.y, new_radius)
        new_asteroid_1.velocity = velocity_1

        new_asteroid_2 = Asteroid(self.position.x, self.position.y, new_radius)
        new_asteroid_2.velocity = velocity_2
