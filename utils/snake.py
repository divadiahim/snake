from sys import byteorder
import random
from utils.config import BG_COLOR, COLOR, COLS, HEIGHT, PIXEL_SIZE, ROWS, SNAKE_COLOR, WIDTH
import pygame
pygame.init()
pygame.font.init()
class snake:
    def __init__(self,win):
        self.win=win
        self.grid_init()
        self.draw_grid_init()
        self.init_snake(5)
        self.blurSurf(3)
        self.init_fade()
          
    def grid_init(self):
        self.arr=[]
        for i in range(ROWS):
            self.arr.append([])
            for j in range(COLS):
               self.arr[i].append(BG_COLOR)
        return self.arr
    def draw_grid_init(self):
        for i,row in enumerate(self.arr):
            for j,color_val in enumerate(row):
                pygame.draw.rect(self.win,color_val,(i*PIXEL_SIZE,j*PIXEL_SIZE,PIXEL_SIZE,PIXEL_SIZE))

    def draw_snake(self,poz,len):
        x_random=random.randint(1,ROWS)
        y_random=random.randint(1,COLS)
        self.arr[x_random][y_random]=COLOR
        
        x,y=poz
        for i in range(len):
            self.arr[x][y+i]=SNAKE_COLOR
        self.draw_grid_init()

                
    def init_snake(self,len):
        self.len=len
        poz=(0,0)
        self.draw_snake(poz,self.len)

    def blurSurf(self, amt):
        if amt < 1.0:
            raise ValueError("Arg 'amt' must be greater than 1.0, passed in value is %s"%amt)
        scale = 1.0/float(amt)
        surf_size = self.win.get_size()
        scale_size = (int(surf_size[0]*scale), int(surf_size[1]*scale))
        surf = pygame.transform.smoothscale(self.win, scale_size)
        surf = pygame.transform.smoothscale(surf, surf_size)
        self.win.blit(surf,(0,0))
        pygame.display.update()

    def fade(self,start,stop,index):
       
        fade = pygame.Surface((WIDTH, HEIGHT))
        fade.fill((0,0,0))
        for alpha in range(start, stop,index):
            pygame.event.pump()
            print(alpha)
            fade.set_alpha(alpha)
            self.draw_grid_init()
            self.win.blit(fade,(0,0))
            pygame.display.update()
            pygame.time.delay(2)  

    def init_fade(self):
        fade = pygame.Surface((WIDTH, HEIGHT))
        fade.fill((0,0,0))
        fade.set_alpha(110)
        self.win.blit(fade,(0,0))
        pygame.display.update()
         