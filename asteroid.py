from circleshape import *
import pygame
from constants import *
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        #print(f"Asteroid initialized: {self}")

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, width=2)
        # print(f"Drawing asteroid")

    def update(self, dt):
        self.screen_wrap_simple()
        self.position += (self.velocity * dt)
        # print(f"Updating asteroid: {self.position}")

    def split(self):
        # destroy original asteroid
        self.kill()
        # print("Asteroid hit")
        # if asteroid is smallest size do not replace
        if self.radius <= ASTEROID_MIN_RADIUS:
            # print("Asteroid is too small. No asteroids to spawn.")
            return
        # otherwise replace asteroid with two smaller asteroids
        else:
             random_angle_offset = random.uniform(20, 50)
             vector1 = self.velocity.rotate(random_angle_offset)
             vector2 = self.velocity.rotate(-random_angle_offset)
             self.radius -= ASTEROID_MIN_RADIUS
             new_asteroid_1 = Asteroid(self.position.x, self.position.y, self.radius)
             new_asteroid_2 = Asteroid(self.position.x, self.position.y, self.radius)
             # print(f"Spawning new asteroids: {new_asteroid_1}, {new_asteroid_2}")
             new_asteroid_1.velocity = vector1 * ASTEROID_VELOCITY_MULT
             new_asteroid_2.velocity = vector2 * ASTEROID_VELOCITY_MULT