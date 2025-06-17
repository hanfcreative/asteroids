from constants import *
from celestialbody import *
import random

class Star(CelestialBody):
    def __init__(self, x, y):
        super().__init__(x, y)

        self.parallax_factor = random.uniform(STAR_PARALLAX_MIN, STAR_PARALLAX_MAX)

    def update(self, dt):
         pass

    # deprecated - delete
    #def apply_parallax(self, dt, player_velocity):
        #self.position -= player_velocity * self.parallax_factor * dt
        #self.screen_wrap_simple()

    def draw(self, screen):
        screen.set_at((int(self.position.x), int(self.position.y)), STAR_COLOR)
        # print(f"drawing star at: {self.position}")