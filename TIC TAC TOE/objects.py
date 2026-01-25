import pygame
from constants import*
from init import*


# The size and location of 9 squares in display
sq1 = pygame.Rect(CORDS[0], CORDS[0], TILE_SIZE, TILE_SIZE)
sq2 = pygame.Rect(CORDS[1], CORDS[0], TILE_SIZE, TILE_SIZE)
sq3 = pygame.Rect(CORDS[2], CORDS[0], TILE_SIZE, TILE_SIZE)

sq4 = pygame.Rect(CORDS[0], CORDS[1], TILE_SIZE, TILE_SIZE)
sq5 = pygame.Rect(CORDS[1], CORDS[1], TILE_SIZE, TILE_SIZE)
sq6 = pygame.Rect(CORDS[2], CORDS[1], TILE_SIZE, TILE_SIZE)

sq7 = pygame.Rect(CORDS[0], CORDS[2], TILE_SIZE, TILE_SIZE)
sq8 = pygame.Rect(CORDS[1], CORDS[2], TILE_SIZE, TILE_SIZE)
sq9 = pygame.Rect(CORDS[2], CORDS[2], TILE_SIZE, TILE_SIZE)

sq_lists = [sq1, sq2, sq3, sq4, sq5, sq6, sq7, sq8, sq9]








