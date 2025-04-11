import pygame, sys, os, random, time, psycopg2
sys.path.append(os.path.abspath('..'))

from config import load_config




# database connection and create table
config = load_config()
conn = psycopg2.connect(**config)
    
conn.autocommit = True #авто транзакции
    
cursor = conn.cursor()
    
sql = """CREATE TABLE IF NOT EXISTS users (
                id SERIAL PRIMARY KEY,
                username VARCHAR(50) UNIQUE NOT NULL
)"""
cursor.execute(sql)

sql = """CREATE TABLE IF NOT EXISTS user_score (
                id SERIAL PRIMARY KEY,
                user_id INTEGER NOT NULL REFERENCES users(id) ON DELETE CASCADE,
                level INTEGER NOT NULL,
                score INTEGER NOT NULL
)"""
cursor.execute(sql)


pygame.init()

def is_not_exist_username(username):
    sql = """SELECT username FROM users WHERE username = %s"""
    cursor.execute(sql, (username,))
    return cursor.fetchone() is None
    
    

def save_score(user_id, level, score):
    cursor.execute(
        "UPDATE user_score SET level = %s, score = %s WHERE user_id = %s",
        (level, score, user_id)
    )
    print("Progress saved!")


#screen settings
Screen_Width, Screen_Height = 800, 800
screen = pygame.display.set_mode((800, 800))
pygame.display.set_caption("Snake")

BLOCK_SIZE = 50 #our block

#fonts
Font = pygame.font.SysFont("Verdana", BLOCK_SIZE // 2)
Font_for_win = pygame.font.SysFont("Verdana", BLOCK_SIZE*2)

clock = pygame.time.Clock()
speed = 4
apples_eaten = 0

#wall class
class Wall:
    def __init__(self, level):
        self.body = []
        self.create_walls(level)

    #walls in levels
    def create_walls(self, level):
        self.body = []
        if level == 2:
            self.body = [(i, 5) for i in range(5, 10)]
        elif level == 3:
            self.body = [(i, 10) for i in range(3, 7)] + [(7, i) for i in range(3, 7)]
        elif level == 4:
            self.body = [(i, 7) for i in range(12, 15)] + [(4, i) for i in range(2, 6)]
        elif level == 5:
            self.body = [(10, i) for i in range(2, 6)] + [(i, 12) for i in range(12, 15)]
        elif level == 6:
            self.body = [(3, i) for i in range(5, 10)] + [(i, 3) for i in range(12, 15)]

    def draw(self, screen):
        for x, y in self.body:
            pygame.draw.rect(screen, (255, 255, 255), (x * BLOCK_SIZE, y * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE))

#snake class
class Snake:
    def __init__(self):
        self.x, self.y = BLOCK_SIZE, BLOCK_SIZE
        self.xdir = 1
        self.ydir = 0
        self.next_xdir = self.xdir
        self.next_ydir = self.ydir
        self.head = pygame.Rect(self.x, self.y, BLOCK_SIZE, BLOCK_SIZE)
        self.body = [pygame.Rect(self.x - BLOCK_SIZE, self.y, BLOCK_SIZE, BLOCK_SIZE)]
        self.dead = False

    #draw part
    def update(self):
        global apple, speed, wall, level, apples_eaten

        self.xdir = self.next_xdir
        self.ydir = self.next_ydir

        #if we crash into ourselves or go beyond the border
        for square in self.body:
            if self.head.x == square.x and self.head.y == square.y:
                self.dead = True
            if self.head.x not in range(0, Screen_Width) or self.head.y not in range(0, Screen_Height):
                self.dead = True

        #if we crash 
        for wx, wy in wall.body:
            if self.head.x == wx * BLOCK_SIZE and self.head.y == wy * BLOCK_SIZE:
                self.dead = True

        #if we lose
        if self.dead:
            save_score(user_id, int_level, apples_eaten)
            time.sleep(0.5)
            speed = 4
            self.x, self.y = BLOCK_SIZE, BLOCK_SIZE
            self.head = pygame.Rect(self.x, self.y, BLOCK_SIZE, BLOCK_SIZE)
            self.body = [pygame.Rect(self.x - BLOCK_SIZE, self.y, BLOCK_SIZE, BLOCK_SIZE)]
            self.xdir = 1
            self.ydir = 0
            self.next_xdir = self.xdir
            self.next_ydir = self.ydir
            self.dead = False
            apple = Apple()
            level = 1
            wall = Wall(level)
            apples_eaten = 0
            pygame.time.set_timer(APPLE_DISAPPEAR, 0)
            pygame.time.set_timer(APPLE_DISAPPEAR, 4000)
            

        self.body.append(self.head)
        for i in range(len(self.body) - 1):
            self.body[i].x, self.body[i].y = self.body[i + 1].x, self.body[i + 1].y
        self.head.x += self.xdir * BLOCK_SIZE
        self.head.y += self.ydir * BLOCK_SIZE
        self.body.remove(self.head)

#apple class
class Apple:
    def __init__(self):
        while True:
            self.x = int(random.randint(0, Screen_Width - BLOCK_SIZE) / BLOCK_SIZE) * BLOCK_SIZE
            self.y = int(random.randint(0, Screen_Height - BLOCK_SIZE) / BLOCK_SIZE) * BLOCK_SIZE
            self.rect = pygame.Rect(self.x, self.y, BLOCK_SIZE, BLOCK_SIZE)

            #so that the apple does not spawn under the wall or the snake itself
            if not any(segment.x == self.x and segment.y == self.y for segment in snake.body) and \
            not (snake.head.x == self.x and snake.head.y == self.y) and \
            not any(wx * BLOCK_SIZE == self.x and wy * BLOCK_SIZE == self.y for wx, wy in wall.body):
                break

        
    def update(self):
        pygame.draw.rect(screen, (255, 0, 0), self.rect)

#net
def drawGrid():
    for x in range(0, Screen_Width, BLOCK_SIZE):
        for y in range(0, Screen_Height, BLOCK_SIZE):
            rect = pygame.Rect(x, y, BLOCK_SIZE, BLOCK_SIZE)
            pygame.draw.rect(screen, "#3c3c3b", rect, 1)

score = Font.render("1", True, (255, 255, 255))
score_rect = score.get_rect(center=(Screen_Width / 20, Screen_Height / 20))

drawGrid()

snake = Snake()
level = 1
previous_level = level
wall = Wall(level)
apple = Apple()
user_id = None
pause = False

APPLE_DISAPPEAR = pygame.USEREVENT + 1
pygame.time.set_timer(APPLE_DISAPPEAR, 4000)

global run #for main loop
run = True 

#start screen and username input button
startScreen = True
username_text = pygame.font.SysFont("Verdana", 30)
username = ""
#start screen 
while startScreen:
    screen.fill((0, 0, 0))
    
    #clue
    start_font = pygame.font.SysFont("Verdana", 30)
    start_text = start_font.render("Enter your name and press ENTER to Start", True, (255,255,255))
    start_text_rect = start_text.get_rect(center=(Screen_Width//2, 250))
    screen.blit(start_text, start_text_rect) 
    
    #white rectangle
    rect_width, rect_height = 650, 50
    rect_x = (Screen_Width - rect_width) // 2
    rect_y = (Screen_Height - rect_height) // 2
    pygame.draw.rect(screen, (255, 255, 255), (rect_x, rect_y, rect_width, rect_height))
    
    #draw text inside rectangle
    input_text = username_text.render(username, True, (0, 0, 0))
    screen.blit(input_text, (rect_x + 10, rect_y + 10))
    
    #events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            startScreen = False
            run = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE:
                username = username[:-1]
            elif event.key == pygame.K_RETURN and username:
                
                if is_not_exist_username(username):
                    sql = """INSERT INTO users (username) VALUES (%s) RETURNING id"""
                    cursor.execute(sql, (username,))
                    user_id = cursor.fetchone()[0]
                    
                    sql = """INSERT INTO user_score (user_id,level, score) VALUES (%s, %s, %s)"""
                    cursor.execute(sql, (user_id,1,0))

                    print(f"{username}! Your level is: 1")
                else: 
                    sql = """SELECT id FROM users WHERE username = %s"""
                    cursor.execute(sql, (username,))
                    user_id = cursor.fetchone()[0]
                                        
                    cursor.execute("SELECT level FROM user_score WHERE user_id = %s", (user_id,))
                    level = cursor.fetchone()[0]
                    print(f"{username}! Your level is: {level}")
                    
                startScreen = False
                    
            elif len(username) < 29:
                username += event.unicode
    
    
    pygame.display.update()
    clock.tick(60)

#main loop
while run:
    for event in pygame.event.get(): #keyboard actions
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            
            #pause
            if event.key == pygame.K_p:
                if not pause:
                    pause = True
                    print("Game paused. Saving...")
                    save_score(user_id, int_level, apples_eaten)
                else:
                    pause = False
                    print("The game continues")
        
            if not pause:
                if event.key == pygame.K_DOWN and not snake.ydir == -1:
                    snake.next_ydir = 1
                    snake.next_xdir = 0
                elif event.key == pygame.K_UP and not snake.ydir == 1:
                    snake.next_ydir = -1
                    snake.next_xdir = 0
                elif event.key == pygame.K_LEFT and not snake.xdir == 1:
                    snake.next_ydir = 0
                    snake.next_xdir = -1
                elif event.key == pygame.K_RIGHT and not snake.xdir == -1:
                    snake.next_ydir = 0
                    snake.next_xdir = 1
                
        
        if event.type == APPLE_DISAPPEAR and not pause: #timer for apple
            apple = Apple()
    
    if pause:
        continue
    
    snake.update()
    
    if level == 7: #endgame
        win = Font_for_win.render("You win", True, (255, 255, 255))
        screen.blit(win, (Screen_Width//3, 380))
        pygame.display.update()
        time.sleep(2)
        screen.fill((0, 255, 0))
        save_score(user_id, int_level+1, apples_eaten)
        run = False
    
    
    screen.fill((0, 0, 0))
    drawGrid()
    
    apple.update()
    
    score = Font.render(f"Score: {apples_eaten}", True, (255, 255, 255))
    int_level = int((len(snake.body) - 1) / 4) #how we calculate levels
    level = min(int_level + 1, 7)
    level_text = Font.render(f"Level: {level}", True, (255, 255, 255))
    
    #max speed
    if speed < 11:
        speed = int_level + 4 
    
    pygame.draw.rect(screen, (0, 255, 0), snake.head)
    
    #draw body
    for square in snake.body:
        pygame.draw.rect(screen, (0, 255, 0), square)

    #text
    screen.blit(score, (20, 10))
    screen.blit(level_text, (20, 45))

    #update walls when level changes
    if level != previous_level:
        wall = Wall(level)

    previous_level = level

    #draw walls
    wall.draw(screen) 

    #adding body part for snake (apple eaten)
    if snake.head.x == apple.x and snake.head.y == apple.y:
        snake.body.append(pygame.Rect(snake.body[-1].x, snake.body[-1].y, BLOCK_SIZE, BLOCK_SIZE))
        apple = Apple()
        apples_eaten += random.randint(1,3)
        
        pygame.time.set_timer(APPLE_DISAPPEAR, 4000)
        
    apple.update()
    
    pygame.display.update()
    clock.tick(speed)
pygame.quit()


conn.close()