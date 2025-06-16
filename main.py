# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from player import *
from asteroid import *
from asteroidfield import *
import sys
from shot import *
from star import *
from nightskymanager import *

# create groups
updatable_group = pygame.sprite.Group()
drawable_back_group = pygame.sprite.Group()
drawable_mid_group = pygame.sprite.Group()
drawable_front_group = pygame.sprite.Group()
asteroids_group = pygame.sprite.Group()
shots_group = pygame.sprite.Group()
celestial_objects_group = pygame.sprite.Group()

# add class var for containers
Player.containers = (updatable_group, drawable_mid_group)
Asteroid.containers = (asteroids_group, updatable_group, drawable_mid_group)
AsteroidField.containers = (updatable_group)
Shot.containers = (shots_group, updatable_group, drawable_mid_group)
Star.containers = (celestial_objects_group, updatable_group, drawable_back_group)
NightSkyManager.containers = (updatable_group)

# make sure VENV is running - source venv/bin/activate

def main():
    # initialize pygame and vars
    # - initialize pygame
    pygame.init()
    # - init game loop as active
    game_loop_running = True
    # - init display settings
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    # - instantiate asteroid field
    asteroid_field = AsteroidField()
    # - instantiate player
    spawn_x = SCREEN_WIDTH / 2
    spawn_y = SCREEN_HEIGHT / 2
    p1 = Player(spawn_x, spawn_y)

    #init night sky and starfield
    nightsky = NightSkyManager()
    # print(f"{len(drawable_back_group)} stars in drawable_back_group")


    # boot message
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    # create game clock
    game_clock = pygame.time.Clock()
    dt = 0

    # game loop
    while game_loop_running:
        # 1: Check for player inputs
        # - check for player quitting
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        # - update all update(dt) in group
        updatable_group.update(dt)
        # - apply parallax
        for star in celestial_objects_group:
            star.apply_parallax(dt, p1.last_velocity)

        # 2: Update the game world
        # - check for collisions between player and asteroids
        # - It's okay for asteroids to simply pass through each other.
        for asteroid in asteroids_group:
            ship_collision = p1.check_collision(asteroid)
            # - if ship collides then Game Over
            if ship_collision == True:
                sys.exit("Game over!")
        # - check for collisions between bullets and asteroids
        for asteroid in asteroids_group:
            for bullet in shots_group:
                asteroid_collision = asteroid.check_collision(bullet)
                if asteroid_collision == True:
                    bullet.kill()
                    asteroid.split()

        # 3: Draw the game to the screen
        # - fill screen with black
        pygame.Surface.fill(screen, "black")

        # update drawables in all drawable groups, background to foreground
        for drawable in drawable_back_group:
            drawable.draw(screen)
        for drawable in drawable_mid_group:
            drawable.draw(screen)
        for drawable in drawable_front_group:
            drawable.draw(screen)
        # - update entire display
        pygame.display.flip()
        # - tick = 60 FPS, return delta time in seconds
        dt =  game_clock.tick(60) / 1000


# add to end of file
if __name__ == "__main__":
    main()