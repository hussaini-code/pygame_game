import pygame
from constants import*


pygame.init()

# making display
game_display = pygame.display.set_mode(DISPLAY_SIZE)

# Defining name to our display
pygame.display.set_caption(DISPLAY_NAME)

# for importing my photo on the caption 
a = pygame.image.load('m.jpeg')
pygame.display.set_icon(a)
