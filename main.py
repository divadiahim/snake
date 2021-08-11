from typing import Collection
from utils.text import Button_img
from utils.config import *
from utils.snake import *
from utils import sound
WIN=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Snake")
img_run = pygame.image.load("img/image.png").convert_alpha()
snake=snake(WIN)
# snake.grid_init()
# snake.draw_grid_init(0)
# snake.init_snake()

text=Button_img(img_run,(WIDTH//6,HEIGHT//2),0.35)
run=True
WIN.set_alpha(255)
running=False
left=False
right=False
up=False
down=False
last_state=0
#1-left 2-right 3-up 4-down
x_start=r=u=d=l=x=i=0
y_start=y=0     
snake_pos=[]
len=len_old=0
moved=False
def pop(len,len_old):
    if len>len_old:
        pass
    else:
        len_old=len
        pixel_to_remove=snake_pos[0]
        x_to_remove,y_to_remove=pixel_to_remove
        snake_pos.pop(0)
        snake.arr[x_to_remove][y_to_remove]=BG_COLOR
        snake.draw_grid_init()
        # print('''deleted''')
        # print()
clock = pygame.time.Clock()        
while(run):
    
    # print('a')
    clock.tick(15)
    for event in pygame.event.get():
        
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT and not(last_state==2):
                left=True
                up=down=right=False
                print("left")
                last_state=1
            if event.key == pygame.K_RIGHT and not(last_state==1):
                print("right")
                right=True
                up=down=left=False
                last_state=2
            if event.key == pygame.K_UP and not(last_state==4):
                print("up")
                up=True
                right=left=down=False
                last_state=3
            if event.key == pygame.K_DOWN and not(last_state==3):
                last_state=4
                down=True
                up=right=left=False
                print("down")

            if (event.key == pygame.K_SPACE and running==False):
                snake.fade(110,255,1,1)
                snake.grid_init()
                snake.draw_grid_init()
                random=snake.init_snake(1)
                snake.fade(255,0,-1)
                print("a")
                # snake.arr[15][15]=SNAKE_COLOR
                pygame.display.update()
                
                running=True
        if running==False:        
            text.draw(WIN)
            pygame.display.update()
    if running:
        

        if(right):
            if(x==COLS):
                x=0
                r=0
            if(snake.arr[x][y]==SNAKE_COLOR and i>0):
                sys.exit()
            snake.arr[x][y]=SNAKE_COLOR
            snake_pos.append((x,y))
            snake.draw_grid_init()
            pygame.display.update()
            r=r+1
            x=x_start+r
            pygame.time.delay(150)
            print(x)
        
        if(left):
            if(x<0):
                x=r=COLS-1
            if(snake.arr[x][y]==SNAKE_COLOR and i>0):
                sys.exit()
            snake.arr[x][y]=SNAKE_COLOR
            snake_pos.append((x,y))
            snake.draw_grid_init()
            pygame.display.update()
            r=r-1
            x=x_start+r
            pygame.time.delay(150)
            print(x)
        if(down):
            if(y==ROWS):
                y=0
                d=0
            if(snake.arr[x][y]==SNAKE_COLOR and i>0):
                sys.exit()
            snake.arr[x][y]=SNAKE_COLOR
            snake_pos.append((x,y))
            snake.draw_grid_init()
            pygame.display.update()
            d=d+1
            y=y_start+d
            pygame.time.delay(150)
            print(y)
            
        if(up):
            if(y<0):
                y=d=ROWS-1
            if(snake.arr[x][y]==SNAKE_COLOR and i>0):
                sys.exit()
            snake.arr[x][y]=SNAKE_COLOR
            snake_pos.append((x,y))
            snake.draw_grid_init()
            pygame.display.update()
            d=d-1
            y=y_start+d
            pygame.time.delay(150)

            
     
        x_random,y_random=random

        if(snake.arr[x_random][y_random]==SNAKE_COLOR):
            sound.Note(500).play(-1)
            pygame.time.delay(60)
            pygame.mixer.stop()
            len=len+1
            random=snake.draw_random()
            pygame.display.update()

        if(right or left or up or down):
            moved=True
            i=i+1

        if(moved):       
            pop(len,len_old)
        # print(len,len_old)
        len_old=len
        
          
        # print(x,y)
    # print(snake_pos)
    
sys.exit()                        