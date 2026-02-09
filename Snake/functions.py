import pygame
from random import randint as ran
from constant import*


def show (Surface, snake, food):
    """ Showing snake in display """
    for sq in snake:
        pygame.draw.rect(Surface, (0, 0, 255),
         (sq[0] * TILE_SIZE, sq[1] * TILE_SIZE, TILE_SIZE, TILE_SIZE ) )
    pygame.draw.rect(Surface, (255, 0, 0), (food[0] * TILE_SIZE, food[1] * TILE_SIZE, TILE_SIZE, TILE_SIZE))     

def update(snake, direction, food, alive, speed):
    """ For making the directions that snake moves """    
    if direction == "Right" :
        if snake[-1][0] + 1 > 19:
            snake.append([0 , snake[-1][1]])
        else:
            snake.append([snake[-1][0] + 1, snake[-1][1]])

    elif direction == "Left" :
        if snake[-1][0] - 1 < 0 :
            snake.append( [19, snake[-1][1]])
        else:
            snake.append([snake[-1][0] - 1, snake[-1][1]])        
    
    elif direction == "Up" :
        if snake [-1][1] -1 < 0 :
            snake.append([snake[-1][0] , 19]) 
        else:
            snake.append([snake[-1][0] , snake[-1][1] - 1])  

    elif direction == "Down" :
        if snake[-1][1] + 1 > 19:
            snake.append([snake[-1][0] , 0])
        else:
            snake.append([snake[-1][0] , snake[-1][1] + 1]) 
    
    if food not in snake and alive: # for eating food
        snake.pop(0)
    else :
        if alive:
            food = generate_food(snake)
            speed += 1  

    if snake[-1] in snake[:-1]: # losing: if snake accidint with it self
        alive = False

    return snake, food, alive, speed      


def generate_food(snake):
    """for making foo that our snake grow up """
    food = [ran(0, (DISPLAY_SIZE[0] // TILE_SIZE) - 1 ), ran(0, (DISPLAY_SIZE[0] // TILE_SIZE) - 1)] 
    while food in snake :
        food = [ran(0, (DISPLAY_SIZE[0] // TILE_SIZE) - 1 ), ran(0, (DISPLAY_SIZE[0] // TILE_SIZE) - 1)]
    return food    

def restart():
    """ For restarting our game after we lose """
    snake = [[0,(DISPLAY_SIZE[1] // TILE_SIZE) // 2 ],
        [1, (DISPLAY_SIZE[1] // TILE_SIZE) // 2 ],
        [2, (DISPLAY_SIZE[1] // TILE_SIZE) // 2 ]]
    food = generate_food(snake)
    direction = "Right"
    alive = True
    SPEED = 5
    return snake, food, direction, alive, SPEED    
