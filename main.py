# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    game_loop_running = True

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
        # - update entire display, call last
        pygame.display.flip()


# add to end of file
if __name__ == "__main__":
    main()