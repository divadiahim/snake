from sys import byteorder
from utils.config import BG_COLOR, COLOR, COLS, PIXEL_SIZE, ROWS, SNAKE_COLOR
import pygame
pygame.init()
class snake:
    def __init__(self,win):
        self.win=win
    def grid_init(self):
        self.arr=[]
        for i in range(ROWS):
            self.arr.append([])
            for j in range(COLS):
               self.arr[i].append(BG_COLOR)
        return self.arr
    def draw_grid_init(self,border):
        for i,row in enumerate(self.arr):
            for j,color_val in enumerate(row):
                pygame.draw.rect(self.win,color_val,(i*PIXEL_SIZE,j*PIXEL_SIZE,PIXEL_SIZE,PIXEL_SIZE),border)

    def draw_snake(self,poz,len):
        x,y=poz
        for i in range(len):
            self.arr[x][x+i]=SNAKE_COLOR
        self.draw_grid_init(0)

                
    def init_snake(self):
        poz=(5,5)
        self.draw_snake(poz,5)