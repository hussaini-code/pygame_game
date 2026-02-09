import pygame
import sys
from constant import*
from init import*
from functions import*



clock = pygame.time.Clock() # For making how many time our loop do in a minute
direction = "Down"
food = generate_food(snake)
alive = True
while True:     # Making game loop
    game_display.fill((99, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYUP:# arrange keys in keyboard for determining snake direction
            if event.key == pygame.K_UP and direction != "Down":
                direction = "Up"

            elif event.key == pygame.K_DOWN and direction != "Up":
                direction = "Down" 
            
            elif event.key == pygame.K_RIGHT and direction != "Left" :
                direction = "Right" 
            
            elif event.key == pygame.K_LEFT and direction != "Right":
                direction = "Left"
    
    game_display.blit(SCREEN_BACKROUND, (0, 0))
    snake, food, alive, SPEED = update(snake, direction, food, alive, SPEED)
    
    if not alive : # delay for restarting 
        direction = ""
        if DELAY == 0:
            DELAY = 10
            snake, food, direction, alive, SPEED = restart()   
        DELAY -= 1
            
    show(game_display , snake, food)        
    pygame.display.update()
    clock.tick(SPEED)
             