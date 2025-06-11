# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *

# make sure VENV is running - source venv/bin/activate

def main():
    # initialize pygame and vars
    pygame.init()
    game_loop_running = True
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
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

        # 2: Update the game world

        # 3: Draw the game to the screen
        # - fill screen with black
        pygame.Surface.fill(screen, "black")
        # - update entire display
        pygame.display.flip()
        # - tick = 60 FPS, return delta time in seconds
        dt =  game_clock.tick(60) / 1000


# add to end of file
if __name__ == "__main__":
    main()