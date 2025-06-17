from constants import *
import pygame
import random
from star import *
class NightSkyManager(pygame.sprite.Sprite):
    def __init__(self, celestial_objects_group):
        pygame.sprite.Sprite.__init__(self, self.containers)
        #define starfield
        self.stars = [
            (random.randint(0, SCREEN_WIDTH - 1), random.randint(0, SCREEN_HEIGHT - 1))
            for _ in range(NIGHTSKY_NUM_STARS)
        ]
        # init starfield
        self.generate_starfield()

        #reference to celestial_objects_group in main.py
        self.celestial_objects_group = celestial_objects_group

        # celestial body velocity
        self.celestial_body_velocity = pygame.Vector2(0,0) 

    def generate_starfield(self):
        for star in self.stars:
            Star(star[0], star[1])
        # print("Starfield generated.")

    def update_parallax(self, dt, player):
        target = player.last_velocity
        self.celestial_body_velocity = self.celestial_body_velocity.lerp(target, NIGHTSKY_PARALLAX_EASE * dt)

        for celestial_object in self.celestial_objects_group:
            if isinstance(celestial_object, CelestialBody):
                celestial_object.update_parallax(dt, self.celestial_body_velocity)

    def update(self, dt):
        pass        