from circleshape import *
import pygame

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        #print(f"Asteroid initialized: {self}")

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, width=2)
        # print(f"Drawing asteroid")

    def update(self, dt):
        self.position += (self.velocity * dt)
        # print(f"Updating asteroid: {self.position}")