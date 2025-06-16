from constants import *
import pygame
import random
from star import *
class NightSkyManager(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.stars = [
            (random.randint(0, SCREEN_WIDTH - 1), random.randint(0, SCREEN_HEIGHT - 1))
            for _ in range(NIGHTSKY_NUM_STARS)
        ]

        self.generate_starfield()


    def generate_starfield(self):
        for star in self.stars:
            Star(star[0], star[1])
        # print("Starfield generated.")

    def update(self, dt):
        pass        