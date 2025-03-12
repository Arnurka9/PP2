import pygame

pygame.init()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Red ball")

#color
WHITE = (255, 255, 255)
RED = (255, 0, 0)

#parameters 
ball_x = 800//2
ball_y = 600//2

ball_radius = 25

clock = pygame.time.Clock()

step = 20

running = True

while running:
    screen.fill(WHITE)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
    #moving 
    move = pygame.key.get_pressed()
        
    if move[pygame.K_LEFT] and ball_x - ball_radius - step >= 0:
        ball_x -= step
    elif move[pygame.K_RIGHT] and ball_x + ball_radius + step <= 800:
        ball_x += step
    elif move[pygame.K_UP] and ball_y - ball_radius - step >= 0:
        ball_y -= step
    elif move[pygame.K_DOWN] and ball_y + ball_radius + step <= 600:
        ball_y += step
        
        
    pygame.draw.circle(screen, RED, (ball_x, ball_y), ball_radius)
    pygame.display.flip()
        
        
    clock.tick(60) #60 fps

pygame.quit()