import pygame
from pygame.locals import *
import os

pygame.init()

class Painter(object):
    def __init__(self, width, height):
        #our surface
        self.window = pygame.display.set_mode((width, height))
        self.window.fill((200,200,200))
        self.canvas = pygame.Surface((width-100, height))
        self.canvas.fill((255,255,255))
        
        #for run the programm
        self.running = False
        
        #for continuous drawing
        self.last_mpos = None
        
        #to determine when the mouse is inactive
        self.click = False
        
        #brush width
        self.widthx = 6
        self.widthy = 6
        pygame.display.set_caption("Paint at mininum")
        
        
        #color palen and eraser
        self.palette = [(0, 0, 0), (255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0), (255, 0, 255), (0, 255, 255), (255, 192, 203), (255, 255, 255)]
        #                 black       red           green       blue           yellow         purple        aqua             pink        #eraser (white)
        self.current_color = self.palette[0]        
        
        #color icons
        black_rect  = pygame.draw.rect(self.window, self.palette[0], (width-80, 10, 25, 25))
        red_rect    = pygame.draw.rect(self.window, self.palette[1], (width-50, 10, 25, 25))
        green_rect  = pygame.draw.rect(self.window, self.palette[2], (width-80, 40, 25, 25))
        blue_rect   = pygame.draw.rect(self.window, self.palette[3], (width-50, 40, 25, 25))
        yellow_rect = pygame.draw.rect(self.window, self.palette[4], (width-80, 70, 25, 25))
        purple_rect = pygame.draw.rect(self.window, self.palette[5], (width-50, 70, 25, 25))
        aque_rect   = pygame.draw.rect(self.window, self.palette[6], (width-80, 100, 25, 25))
        pink_rect   = pygame.draw.rect(self.window, self.palette[7], (width-50, 100, 25, 25))
        
        #eraser icon
        eraser = pygame.image.load("source\\paint\\eraser.png")
        eraser = pygame.transform.scale(eraser, (25, 25))
        eraser_rect = pygame.draw.rect(self.window, self.palette[8], (width-50, 130, 25, 25))
        self.window.blit(eraser, (width-50, 130))
        
        #hitbox of colors
        self.color_rects = [
            black_rect,
            red_rect,
            green_rect,
            blue_rect,
            yellow_rect,
            purple_rect,
            aque_rect,
            pink_rect,
            eraser_rect,
        ] 
        
        #for our shapes
        self.shapes = ["rect", "circle", "square", "right_triangle", "equilateral_triangle", "rhombus"]
        
        #for drawing shapes
        self.drawing_shape = None
        self.select_shape = False
        self.shape_start = None
        
        #his icons and hitboxes
        rect_button = pygame.draw.rect(self.window, (255,255,255), (width-90, 200, 40, 25))
        circle_button = pygame.draw.circle(self.window, (255,255,255), (width-30, 212), 13, 25)
        circle_button_rect = pygame.Rect(width-30, 200, 13, 25)
        square_button = pygame.draw.rect(self.window, (255,255,255), (width-75, 232, 25, 25))
        right_triangle_button = pygame.draw.polygon(self.window, (255,255,255), [(width-42, 255), (width-15,232), (width-15, 255)])
        right_triangle_button_rect = pygame.Rect(width-45, 232, 30, 25)
        equilateral_triangle_button = pygame.draw.polygon(self.window, (255,255,255), [(width-42, 285), (width-29,262), (width-15, 285)])
        equilateral_triangle_button_rect = pygame.Rect(width-45, 262, 30, 25)
        rhombus_button = pygame.draw.polygon(self.window, (255,255,255), [(width-75, 277.5), (width-62.5, 295), (width-50, 277.5), (width-62.5, 260)])
        rhombus_button_rect = pygame.Rect(width-75, 260, 27,38)
        
        #collected hitboxes
        self.button_rects = [
            rect_button,
            circle_button_rect,
            square_button,
            right_triangle_button_rect,
            equilateral_triangle_button_rect,
            rhombus_button_rect
        ]
        
    #part that will save your image
    def save(self):
        global amount
        amount = 0
        while os.path.exists(os.path.join(os.environ["USERPROFILE"], "Pictures", f"image{amount}.png")):
            amount += 1
        name = os.path.join(os.environ["USERPROFILE"], "Pictures", f"image{amount}.png")
        pygame.image.save(self.canvas, name)
        
    #part of load your image
    def load(self):
        name = os.path.join(os.environ["USERPROFILE"], "Pictures", input("Enter your image: "))
        try:
            self.canvas = pygame.image.load(name)
        except:
            print("No such file in Pictures!")
    
    #part of the manipulation of keys to call the functions required by the user
    def events(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                self.running = False
                break
            
            if event.type == MOUSEBUTTONDOWN:
                self.click = True
            
            if event.type == MOUSEBUTTONUP:
                self.click = False
                self.last_mpos = None
            
            if event.type == KEYDOWN:
                keys = pygame.key.get_pressed()
                if keys[K_LCTRL] or keys[K_RCTRL]:
                    if event.key == K_s:
                        self.save()
                    if event.key == K_o:
                        self.load()
                
                if event.key == K_EQUALS:
                    self.widthx += 1
                    self.widthy += 1
                if event.key == K_MINUS:
                    self.widthx -= 1
                    self.widthy -= 1
           
            #color select
            if event.type == MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                for i, rect in enumerate(self.color_rects):
                    if rect.collidepoint(mouse_x, mouse_y):
                        self.current_color = self.palette[i]
            
            
            #our shapes and how they are drawn
            if event.type == MOUSEBUTTONDOWN:
                self.shape_start = pygame.mouse.get_pos()
        
            if event.type == MOUSEBUTTONUP:
                if self.shape_start:  
                    shape_end = pygame.mouse.get_pos()
                    
                    if self.drawing_shape == "rect":
                        x1, y1 = self.shape_start
                        x2, y2 = shape_end
                        rect = pygame.Rect(min(x1, x2), min(y1, y2), abs(x2 - x1), abs(y2 - y1))
                        pygame.draw.rect(self.canvas, self.current_color, rect, self.widthx)  
                    
                    
                    
                    elif self.drawing_shape == "circle":
                        x1, y1 = self.shape_start
                        x2, y2 = shape_end
                        center = ((x1 + x2) // 2, (y1 + y2) // 2)
                        radius = max(abs(x2 - x1), abs(y2 - y1)) // 2
                        pygame.draw.circle(self.canvas, self.current_color, center, radius, self.widthx)



                    elif self.drawing_shape == "square":
                        x1, y1 = self.shape_start
                        x2, y2 = shape_end
                        side = min(abs(x2-x1), abs(y2-y1))
                        square = pygame.Rect(min(x1, x2), min(y1, y2), side, side)
                        pygame.draw.rect(self.canvas, self.current_color, square, self.widthx)


                        
                    elif self.drawing_shape == "right_triangle":
                        x1, y1 = self.shape_start
                        x2, y2 = shape_end
                        pygame.draw.polygon(self.canvas, self.current_color, [(x1, y1), (x2, y2), (x1, y2)], self.widthx)
                    


                    elif self.drawing_shape == "equilateral_triangle":
                        x1, y1 = self.shape_start
                        x2, y2 = shape_end
                        x3 = x1-(x2-x1)
                        pygame.draw.polygon(self.canvas, self.current_color, [(x1, y1), (x2, y2), (x3, y2)], self.widthx)
                    


                    elif self.drawing_shape == "rhombus":
                        x1, y1 = self.shape_start
                        x2, y2 = shape_end
    
                        mid_x = (x1 + x2) // 2  
                        mid_y = (y1 + y2) // 2  

    
                        top = (mid_x, y1)      
                        right = (x2, mid_y)    
                        bottom = (mid_x, y2)   
                        left = (x1, mid_y)     

                        pygame.draw.polygon(self.canvas, self.current_color, [top, right, bottom, left], self.widthx)

                    
                    self.shape_start = None
            
            if event.type == MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                for i, rect in enumerate(self.button_rects):
                    if rect.collidepoint(mouse_x, mouse_y):
                        if self.drawing_shape == self.shapes[i]:
                            self.drawing_shape = None
                        else:
                            self.drawing_shape = self.shapes[i]


    #draw part with brush
    def update(self):
        mx, my = pygame.mouse.get_pos()
    
        if self.drawing_shape is None and self.last_mpos is not None and self.click:
            mx0, my0 = self.last_mpos
            radius = self.widthx // 2

            for x in range(-radius, radius + 1):
                for y in range(-radius, radius + 1):
                    if x**2 + y**2 <= radius**2:
                        pygame.draw.line(self.canvas, self.current_color,
                                            (mx0 + x, my0 + y),
                                            (mx + x, my + y))
    
        self.last_mpos = (mx, my)


    #to generate an image
    def render(self):
        self.window.blit(self.canvas, (0,0))
        
    #main loop
    def mainLoop(self):
        self.running = True
        while self.running:
            self.events()
            self.update()
            self.render()
            pygame.display.flip()

#main block
def main():
    width = 740
    height = 480
    mainclass = Painter(width, height)
    mainclass.mainLoop()
    

#running code
if __name__ == "__main__":
    main()