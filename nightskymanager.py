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
        # set parallex behavior for modes
        if NIGHTSKY_PARALLAX_MODE == "arcade":
            velocity_target = player.last_velocity
            self.celestial_body_velocity = velocity_target

        elif NIGHTSKY_PARALLAX_MODE == "realistic":
            velocity_target = player.get_input_velocity()
            if player.moving:
                self.celestial_body_velocity = velocity_target
            else:
                self.celestial_body_velocity = pygame.Vector2(0, 0)

        elif NIGHTSKY_PARALLAX_MODE == "smooth":
            velocity_target = player.get_input_velocity()
            self.celestial_body_velocity = self.celestial_body_velocity.lerp(velocity_target, NIGHTSKY_PARALLAX_EASE * dt)

        elif NIGHTSKY_PARALLAX_MODE == "hybrid":
            velocity_target = player.last_velocity
            # velocity mult while moving
            if player.moving:
                adjusted_velocity = velocity_target * NIGHTSKY_PARALLAX_MOVE_MULTIPLIER
            else:
                adjusted_velocity = velocity_target
            
            ambient_drift = pygame.Vector2(10, 0).rotate(pygame.time.get_ticks() * 0.01)
            blended = adjusted_velocity + ambient_drift * (1 - velocity_target.length() / PLAYER_SPEED)
            self.celestial_body_velocity = self.celestial_body_velocity.lerp(blended, NIGHTSKY_PARALLAX_EASE * dt)

        # apply desired parallax to all celestial objects
        for celestial_object in self.celestial_objects_group:
            if isinstance(celestial_object, CelestialBody):
                celestial_object.update_parallax(dt, self.celestial_body_velocity)

    def update(self, dt):
        pass        