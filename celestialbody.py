import pygame
from constants import *

class CelestialBody(pygame.sprite.Sprite):
    def __init__(self, x, y):
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)

        # default, override in child
        self.parallax_factor = 1.0

    def draw(self, screen):
        # sub-classes must override
        pass

    def update(self, dt):
        # sub-classes must override
        pass

    def screen_wrap_simple(self):
        # old screen wrap
        # self.position.x %= SCREEN_WIDTH
        # self.position.y %= SCREEN_HEIGHT

        while self.position.x < 0:
            self.position.x += SCREEN_WIDTH
        while self.position.x >= SCREEN_WIDTH:
            self.position.x -= SCREEN_WIDTH

        while self.position.y < 0:
            self.position.y += SCREEN_HEIGHT
        while self.position.y >= SCREEN_HEIGHT:
            self.position.y -= SCREEN_HEIGHT

    def update_parallax(self, dt, velocity):
        self.position -= velocity * self.parallax_factor * dt
        self.screen_wrap_simple()
