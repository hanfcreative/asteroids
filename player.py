from constants import *
from circleshape import *
import pygame
from shot import *

class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.x = x
        self.y = y
        self.radius = PLAYER_RADIUS
        self.rotation = 0
        self.timer = 0
        self.last_velocity = pygame.Vector2(0,0)
        self.moving = False

    # in the player class
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    # overriding the draw method of CircleShape
    def draw(self, screen):
        pygame.draw.polygon(screen, "white", self.triangle(), 2)
    
    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt

    def get_input_velocity(self):
        keys = pygame.key.get_pressed()
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        velocity = pygame.Vector2(0, 0)

        if keys[pygame.K_w] or keys[pygame.K_UP]:
            velocity += forward * PLAYER_SPEED
        if keys[pygame.K_s] or keys[pygame.K_DOWN]:
            velocity -= forward * PLAYER_SPEED

        return velocity

    def update(self, dt):
        # init moving
        self.moving = False
        # manage input
        keys = pygame.key.get_pressed()
        input_velocity = pygame.Vector2(0, 0)
        forward = pygame.Vector2(0, 1).rotate(self.rotation)

        if keys[pygame.K_a] or keys[pygame.K_LEFT]:
            self.rotate(-dt)
        if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            self.rotate(dt)
        if keys[pygame.K_w] or keys[pygame.K_UP]:
            input_velocity += forward * PLAYER_SPEED
            self.move(dt)
        if keys[pygame.K_s] or keys[pygame.K_DOWN]:
            input_velocity -= forward * PLAYER_SPEED
            self.move(-dt)
        if keys[pygame.K_SPACE]:
            self.shoot()

        # Even if not moving, check for forward/backward input to ensure last_velocity is accurate
        if input_velocity.length_squared() > 0:
            self.last_velocity = input_velocity
        
        # delete with the dictionary?
        if not self.moving:
            if not NIGHTSKY_PARALLAX_BEHAVIOR[NIGHTSKY_PARALLAX_MODE]["retain_velocity_on_stop"]:
                self.last_velocity = pygame.Vector2(0,0)

        # update timer
        self.timer -= dt

    def move(self, dt):
        self.moving = True
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        velocity = forward * PLAYER_SPEED
        self.position += velocity * dt
        self.last_velocity = velocity
        self.screen_wrap_simple()

    def shoot(self):
        # player can't shoot if timer is greater thsn 0
        if self.timer <= 0:
            new_shot = Shot(self.position.x, self.position.y)
            new_shot.velocity = pygame.Vector2(0, 1).rotate(self.rotation) * PLAYER_SHOOT_SPEED
            # print(f"Shooting bullet at: {new_shot.velocity}")
            self.timer = PLAYER_SHOOT_COOLDOWN
        # else:
        #    print(f"Shoot Cooldown: {self.timer}")
    