import pygame
from constants import SCREEN_HEIGHT
from constants import SCREEN_WIDTH

# Base class for game objects
class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        # we will be using this later
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    def check_collision(self, other_circleshape):
        is_colliding = None
        distance = None
        max_collision_distance = self.radius + other_circleshape.radius
        distance = pygame.math.Vector2.distance_to(self.position, other_circleshape.position)
        if distance <= max_collision_distance:
            is_colliding = True
        else:
            is_colliding = False
        return is_colliding

    def draw(self, screen):
        # sub-classes must override
        pass

    def update(self, dt):
        # sub-classes must override
        pass

    def screen_wrap_simple(self):
        self.position.x %= SCREEN_WIDTH
        self.position.y %= SCREEN_HEIGHT