import pygame
from pygame.locals import *
import random, time

pygame.init()

FPS = 60
FramePerSec = pygame.time.Clock()

# Colors
BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255,255,255)

# Screen
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
SPEED = 5
SCORE = 0
COINS = 0

#Setting up Fonts
font = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 20)
game_over = font.render("Game Over", True, BLACK)


#Setting of display
DISPLAYSURF = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
DISPLAYSURF.fill(WHITE)
pygame.display.set_caption("Racer")

background = pygame.image.load("source\\racer\\AnimatedStreet.png")

#Create an Enemy
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("source\\racer\\Enemy.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)

    def move(self): #set up moves for enemy
        global SCORE
        self.rect.move_ip(0, SPEED)
        if (self.rect.top > 600):
            SCORE += 1
            self.rect.top = 0
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 48), 0)


#Create a player
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("source\\racer\\Player.png")
        self.rect = self.image.get_rect()
        self.rect.center = (SCREEN_WIDTH // 2, 520)

    def move(self): #set up moves for player
        pressed_keys = pygame.key.get_pressed()
        if self.rect.left > 0 and pressed_keys[K_LEFT]:
            self.rect.move_ip(-5, 0)
        if self.rect.right < SCREEN_WIDTH and pressed_keys[K_RIGHT]:
            self.rect.move_ip(5, 0)


#Create coins
class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("source\\racer\\coin.png")
        self.image = pygame.transform.scale(self.image, (48, 48))
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)
    
    def move(self):
        self.rect.move_ip(0, 5)
        if (self.rect.top > 600):
            self.rect.top = 0
            self.rect.center = (random.randint(40, 360), 0)

# Sprites
Pl = Player()
Em = Enemy()
Con = Coin()

# Groups
enemies = pygame.sprite.Group()
enemies.add(Em)
all_sprites = pygame.sprite.Group()
all_sprites.add(Pl, Em, Con)

# Speed event
INC_SPEED = pygame.USEREVENT + 1

# Collid event for coin
COLLID_EVENT = pygame.USEREVENT + 2

#Run code
running = True
while running:
    for event in pygame.event.get(): #increase speed
        if event.type == INC_SPEED and SPEED < 20:
            SPEED += 1
        if event.type == QUIT: #quit the game
            running = False
        if event.type == COLLID_EVENT:
            COINS += random.randint(1,3) #each coin has a different weight

    DISPLAYSURF.blit(background, (0,0)) 
    coins_score = font_small.render(f"Coins: {COINS}", True, BLACK)
    scores = font_small.render(f"Score: {SCORE}", True, BLACK)
    DISPLAYSURF.blit(scores, (10,10))
    DISPLAYSURF.blit(coins_score, (10, 35))

    if pygame.sprite.spritecollideany(Pl, pygame.sprite.Group(Con)): 
        pygame.event.post(pygame.event.Event(COLLID_EVENT))
        Con.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)
        
        if COINS%4 == 0: #INC_SPEED is called when we collect n number of coins
            pygame.event.post(pygame.event.Event(INC_SPEED))

    # Move and draw sprites
    for entity in all_sprites:
        entity.move()
        DISPLAYSURF.blit(entity.image, entity.rect)

    # Collision check
    if pygame.sprite.spritecollideany(Pl, enemies): #add crash sound
        pygame.mixer.Sound('source\\racer\\crash.wav').play()
        time.sleep(0.5)
        
        DISPLAYSURF.fill(RED)
        DISPLAYSURF.blit(game_over, (30,250))
        
        pygame.display.update()
        time.sleep(2)
        running = False

    pygame.display.update()
    FramePerSec.tick(FPS)

pygame.quit()
