import pygame
import random
from Config import Config
from Game import Game


def main():
    # Set the game window
    display = pygame.display.set_mode(
        (Config["game"]["width"], Config["game"]["height"])
    )
    surface = pygame.Surface(
        (Config["game"]["width"], Config["game"]["height"]), pygame.SRCALPHA
    )

    # Add game window title
    pygame.display.set_caption(Config["game"]["caption"])

    # Create game instance
    game = Game(display, surface)
    # Run the main game loop
    game.loop()


if __name__ == "__main__":
    main()
