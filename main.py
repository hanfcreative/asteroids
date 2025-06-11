# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from player import *

# create groups
updatable_group = pygame.sprite.Group()
drawable_group = pygame.sprite.Group()

# add class var to player for containers
Player.containers = (updatable_group, drawable_group)

# make sure VENV is running - source venv/bin/activate

def main():
    # initialize pygame and vars
    # - initialize pygame
    pygame.init()
    # - init game loop as active
    game_loop_running = True
    # - init display settings
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    # - instantiate player
    spawn_x = SCREEN_WIDTH / 2
    spawn_y = SCREEN_HEIGHT / 2
    p1 = Player(spawn_x, spawn_y)

    # boot message
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    # create game clock
    game_clock = pygame.time.Clock()
    dt = 0

    # create player

    # game loop
    while game_loop_running:
        # 1: Check for player inputs
        # - check for player quitting
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        # - update all updatables in group
        updatable_group.update(dt)

        # 2: Update the game world

        # 3: Draw the game to the screen
        # - fill screen with black
        pygame.Surface.fill(screen, "black")

        # update drawables in group
        for drawable in drawable_group:
            drawable.draw(screen)
        # - update entire display
        pygame.display.flip()
        # - tick = 60 FPS, return delta time in seconds
        dt =  game_clock.tick(60) / 1000


# add to end of file
if __name__ == "__main__":
    main()