import pygame
import time

pygame.init()


screen = pygame.display.set_mode((500, 500))
pygame.display.set_caption("Clock")

clock = pygame.time.Clock()

#color
WHITE = (255, 255, 255)

#image
mikki = pygame.image.load("img//mickeyclock.jpg")
mikki = pygame.transform.scale(mikki, (450, 450))
mikki_x = (500 - mikki.get_width())/2
mikki_y = (500 - mikki.get_width())/2

minuts_arm = pygame.image.load("img//minuts.png")
minuts_arm = pygame.transform.scale(minuts_arm, (250, 250))

seconds_arm = pygame.image.load("img//seconds.png")
seconds_arm = pygame.transform.scale(seconds_arm, (300, 300))


#rect for img
rect_seconds = seconds_arm.get_rect(center = (250, 250))
rect_minuts = minuts_arm.get_rect(center = (250, 250))



running = True

while running:
    screen.fill(WHITE)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    now = time.localtime()
    seconds = now.tm_sec
    minuts = now.tm_min
    
    sec_ang = -seconds * 360/60
    min_ang = -minuts * 360/60
    
    seconds_rot = pygame.transform.rotate(seconds_arm, sec_ang) 
    minuts_rot = pygame.transform.rotate(minuts_arm, min_ang)
    
    new_rect_seconds = seconds_rot.get_rect(center = (250, 250))
    new_rect_minuts = minuts_rot.get_rect(center = (250, 250))

    screen.blit(mikki, (mikki_x, mikki_y))
    screen.blit(minuts_rot, (new_rect_minuts.topleft))
    screen.blit(seconds_rot, (new_rect_seconds.topleft))

    pygame.display.flip()
    clock.tick(60)
    
pygame.quit()