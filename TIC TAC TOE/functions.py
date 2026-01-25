import pygame
import numpy as np
from init import*
from objects import*
from constants import GAME_BOARD as gb


def show ():
    """ Making square in display """
    for sq in sq_lists:
        pygame.draw.rect(game_display, (255, 255, 255), sq)


def circle(i):
    """ For drawing of circle in the squares """
    row, col = i // 3 , i % 3
    pygame.draw.circle(game_display, (255, 0, 0), (CORDS[col] + HALF_TILE, CORDS[row] + HALF_TILE), 50, 7)


def cross(i):
    """ For drawing of cross in the squares """
    row, col = i // 3 , i % 3

    pygame.draw.line(game_display, (0, 255, 0), (CORDS[col] + 15, CORDS[row] + 15), (CORDS[col] + 130 - 15 , CORDS[row] + 130 - 15), 7 )
    pygame.draw.line(game_display, (0, 255, 0), (CORDS[col] + 15, CORDS[row] + 130 - 15  ), (CORDS[col] + 130 - 15, CORDS[row] + 15 )  , 7 )


def check_state(gb):
    """ it checks which plsyer is the winner or the game is finidhed equal"""
    for i in range(3):
        row = np.unique(gb[:,i])
        col = np.unique(gb[i, :])
        # check row and col who is winner
        if len(row) == 1 and row != 0:
            return row
        if len(col) == 1 and col != 0:
            return col
        
    # check who is winner not be row or col
    if gb[0][0] == gb [1][1] and gb [1][1] == gb[2][2] and gb[0][0] != 0 :
        return gb [1] [1]
    elif gb[2][0] == gb [1][1] and gb [1][1] == gb[0][2] and gb[2][0] != 0:
        return gb[1][1]

    # if no one is winner
    if 0 not in np.unique(gb):
        return "Tie"    
    return "continue"

def restart():
    return np.array([[0, 0, 0], [0, 0, 0], [0, 0, 0]])    



