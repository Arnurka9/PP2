import pygame
import os

pygame.init()

def play_next_music():
    global all_musics
    all_musics = all_musics[1:] + [all_musics[0]]
    pygame.mixer.music.load(all_musics[0])
    pygame.mixer.music.play()

def play_previous_music():
    global all_musics
    all_musics = [all_musics[-1]] + all_musics[:-1]
    pygame.mixer.music.load(all_musics[0])
    pygame.mixer.music.play()


screen = pygame.display.set_mode((300, 400))
pygame.display.set_caption("Music player")

clock = pygame.time.Clock()

#color
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

#main icon
image = pygame.image.load("music/music-player.png")
image = pygame.transform.scale(image, (200, 200))

image_x = (300-image.get_width()) / 2
image_y = 10


#pause/right/left

pause = pygame.image.load("music/music-pause-button-pair-of-lines-svgrepo-com.svg")
pause = pygame.transform.scale(pause, (100, 100))
pause_rect = pause.get_rect(topleft=(230-pause.get_width(), 227))


right = pygame.image.load("music/reshot-icon-arrow-right-circle-DPXFUH2YQV.svg")
right = pygame.transform.scale(right, (50, 50))
right_rect = right.get_rect(topleft=(285 - pause.get_width(), 220))


left = pygame.image.load("music/reshot-icon-arrow-left-circle-CQ7KNXYF43.svg")
left = pygame.transform.scale(left, (50, 50))
left_rect = left.get_rect(topleft=(160 - pause.get_width(), 220))


#music
path_music = os.path.join(os.environ["USERPROFILE"], "Music")
musics = os.listdir(path_music)
true_musics = [os.path.join(path_music, music) for music in musics if music.endswith(".mp3")]

musics_in_music = os.listdir(r"music")
true_musics_in_music = [os.path.join("music\\", mus) for mus in musics_in_music if mus.endswith(".mp3")]
all_musics = true_musics_in_music + true_musics


#text
font = pygame.font.Font(None, 22)

clue1 = font.render("Space - Play/Pause the music", True, BLACK)
clue2 = font.render("Right Arrow - Play the next music", True, BLACK)
clue3 = font.render("Left Arrow - Play the previous music", True, BLACK)

clue1_x = 10
clue1_y = 300

clue2_x = 10
clue2_y = 330

clue3_x = 10
clue3_y = 360

#running code

if all_musics:
    pygame.mixer.music.load(all_musics[0])
    pygame.mixer.music.play()


running = True
is_in_pause = False


while running:
    screen.fill(WHITE)    
    
    if not pygame.mixer.music.get_busy() and not is_in_pause:
        play_next_music()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        if event.type == pygame.KEYDOWN:    
            if event.key == pygame.K_RIGHT:
                play_next_music()
            
            if event.key == pygame.K_LEFT:
                play_previous_music()
            
            if event.key == pygame.K_SPACE:
                if is_in_pause:
                    pygame.mixer.music.unpause()
                else:
                    pygame.mixer.music.pause()
                is_in_pause = not is_in_pause
        
       
        if event.type == pygame.MOUSEBUTTONDOWN:
            if pause_rect.collidepoint(event.pos):
                if is_in_pause:
                    pygame.mixer.music.unpause()
                else:
                    pygame.mixer.music.pause()
                is_in_pause = not is_in_pause
                
            if right_rect.collidepoint(event.pos):
                play_next_music()
            
            if left_rect.collidepoint(event.pos):
                play_previous_music()
                

    screen.blit(image, (image_x, image_y))
    screen.blit(pause, pause_rect.topleft)
    screen.blit(right, right_rect.topleft)
    screen.blit(left, left_rect.topleft)
    
    screen.blit(clue1, (clue1_x, clue1_y))
    screen.blit(clue2, (clue2_x, clue2_y))
    screen.blit(clue3, (clue3_x, clue3_y))
    
    pygame.display.flip()
    
    clock.tick(60)

print(all_musics)
pygame.quit()