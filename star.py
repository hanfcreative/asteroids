from constants import STAR_COLOR
from celestialbody import *

class Star(CelestialBody):
    def __init__(self, x, y):
        super().__init__(x, y)

    def update(self, dt):
        pass

    def draw(self, screen):
        screen.set_at((int(self.position.x), int(self.position.y)), STAR_COLOR)
        # print(f"drawing star at: {self.position}")