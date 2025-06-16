from circleshape import *
from constants import *
from devsettings import *
class Shot(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, SHOT_RADIUS)
        self.x = x
        self.y = y
        self.radius = SHOT_RADIUS
        self.timer = SHOT_DURATION

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, width=2)
        # print(f"Drawing bullet")

    def update(self, dt):
        # update timer
        self.timer -= dt
        # should the shot be destroyed?
        if ENABLE_SHOT_DURATION:
            if self.timer <= 0:
                self.kill() 
        # bullet screen wrap
        if ENABLE_SHOT_SCREEN_WRAP:
            self.screen_wrap_simple()
        # calculate updated position
        self.position += (self.velocity * dt)
        # print(f"Updating bullet: {self.position}")