import pygame
from constant import*

pygame.init()

# For making game display and identifying width and height
game_display = pygame.display.set_mode(DISPLAY_SIZE)

# Name of our game
pygame.display.set_caption(GAME_NAME)

# For adding photo as SCREEN_BACKROUND
SCREEN_BACKROUND = pygame.image.load('screen.jpg').convert_alpha()
SCREEN_BACKROUND = pygame.transform.scale( SCREEN_BACKROUND , (DISPLAY_SIZE[0], DISPLAY_SIZE[1]))