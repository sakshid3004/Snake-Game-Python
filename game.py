import pygame
import random
import time

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 700

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Initialize the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

# Game variables
snake_pos = [100, 50]
snake_body = [[100, 50], [90, 50], [80, 50]]
food_pos = [random.randrange(1, (WIDTH//10)) * 10, random.randrange(1, (HEIGHT//10)) * 10]
food_spawn = True
direction = 'RIGHT'
change_to = direction
score = 0

# Game loop
clock = pygame.time.Clock()
font = pygame.font.SysFont('Arial', 30)
game_over_font = pygame.font.SysFont('Arial', 60)
game_over_flag = False

while True:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
        #Update direction based on key press
             if event.key == pygame.K_UP and direction != 'DOWN':
                change_to = 'UP'
             elif event.key == pygame.K_DOWN and direction != 'UP':
                change_to = 'DOWN'
             elif event.key == pygame.K_LEFT and direction != 'RIGHT':
                change_to = 'LEFT'
             elif event.key == pygame.K_RIGHT and direction != 'LEFT':
                change_to = 'RIGHT'    
   #Update direction based on key press
    if change_to == 'UP':
        direction = 'UP'
    elif change_to == 'DOWN':  
        direction = 'DOWN'
    elif change_to == 'LEFT':
        direction = 'LEFT'
    elif change_to == 'RIGHT':
        direction = 'RIGHT'
        
    # Update snake position
    if direction == 'UP':
        snake_pos[1] -= 10
    elif direction == 'DOWN':
        snake_pos[1] += 10
    elif direction == 'LEFT':
        snake_pos[0] -= 10
    elif direction == 'RIGHT':
        snake_pos[0] += 10
        
    # Snake body growth logic
    snake_body.insert(0, list(snake_pos)) 
    if snake_pos == food_pos:
        score += 1
        food_spawn = False
    else:
        snake_body.pop() 
        
    if not food_spawn:
        food_pos = [random.randrange(1, (WIDTH//10)) * 10, random.randrange(1, (HEIGHT//10)) * 10]      
    food_spawn = True
    
    # game over conditions
    if snake_pos[0] < 0 or snake_pos[0] > WIDTH-10:
        game_over_flag = True
    if snake_pos[1] < 0 or snake_pos[1] > HEIGHT-10:
        game_over_flag = True
    for block in snake_body[1:]:   
        if snake_pos == block:
            game_over_flag = True
            
# update screen
    screen.fill(BLACK)
    for pos in snake_body:
        pygame.draw.rect(screen, GREEN, pygame.Rect(pos[0], pos[1], 10, 10))  
    pygame.draw.rect(screen, RED, pygame.Rect(food_pos[0], food_pos[1], 10, 10))
    
    # Display score
    score_text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(score_text, (10, 10))
    
    # Display game over message
    if game_over_flag:
        game_over_text = game_over_font.render("GAME OVER", True, RED)
        text_rect = game_over_text.get_rect(center=(WIDTH//2, HEIGHT//2 - 50))
        screen.blit(game_over_text, text_rect)
        
        final_score_text = font.render(f"Final Score: {score}", True, WHITE)
        score_rect = final_score_text.get_rect(center=(WIDTH//2, HEIGHT//2 + 50))
        screen.blit(final_score_text, score_rect)
    
    # update the display
    pygame.display.update()

    # control the speed
    clock.tick(15)
    
    # Exit when game over and a key is pressed
    if game_over_flag:
        waiting = True
        while waiting:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    waiting = False
                    pygame.quit()
                    exit()
                if event.type == pygame.KEYDOWN:
                    waiting = False
                    break                  