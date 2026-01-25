import pygame
import sys
from init import*
from objects import*
from functions import*


turn = False
show()
# loop of our game
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
            pygame.quit()
        
        # it show the cooinination of place we click on it
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            for sq in range(len(sq_lists)):
                if sq_lists[sq].collidepoint(pos):# we can click in each square one time
                    row, col = sq // 3 , sq % 3
                    if GAME_BOARD [row] [col] == 0:
                        if turn :
                            cross(sq)
                            turn = not turn
                            GAME_BOARD [row] [col] = int(turn) + 1
                        else:
                            circle(sq)
                            turn = not turn
                            GAME_BOARD [row] [col] = int(turn) + 1
            # we call to check state of game
            state = check_state(GAME_BOARD) 
            if state != 'continue':
                if state != "Tie":
                    
                    print(f' player {state} won')
                    GAME_BOARD = restart()
                    show()
                    
                else:
                    print("Tie")
                    GAME_BOARD = restart()
                    show()              
                                
    pygame.display.update()        