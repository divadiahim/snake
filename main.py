from utils.text import Button_img
from utils.config import *
from utils.snake import *
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
x_start=r=u=d=l=x=0
y_start=y=0     
snake_pos=[]
len=len_old=0
moved=False
def pop(len,len_old):
    if len>len_old:
        pass
    else:
        pixel_to_remove=snake_pos[0]
        x_to_remove,y_to_remove=pixel_to_remove
        snake.arr[x_to_remove][y_to_remove]=BG_COLOR
        snake_pos.pop(0)
        len_old=len
        snake.draw_grid_init()
while(run):
    
    for event in pygame.event.get():
        
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT and not(last_state==2):
                left=True
                up=False
                down=False
                right=False
                print("left")
                last_state=1
            if event.key == pygame.K_RIGHT and not(last_state==1):
                print("right")
                right=True
                up=False
                down=False
                left=False
                last_state=2
            if event.key == pygame.K_UP and not(last_state==4):
                print("up")
                up=True
                down=False
                right=left=False
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
        if(right or left or up or down):
            moved=True             
        if(right):
            snake_pos.append((x,y))
            snake.arr[x][y]=SNAKE_COLOR
            snake.draw_grid_init()
            pygame.display.update()
            r=r+1
            x=x_start+r
        
        if(left):
            snake_pos.append((x,y))
            snake.arr[x][y]=SNAKE_COLOR
            snake.draw_grid_init()
            pygame.display.update()
            r=r-1
            x=x_start+r
        

        if(down):
            snake_pos.append((x,y))
            snake.arr[x][y]=SNAKE_COLOR
            snake.draw_grid_init()
            pygame.display.update()
            y=y_start+d
            d=d+1
            
            u=l=0
        if(up):
            snake_pos.append((x,y))
            snake.arr[x][y]=SNAKE_COLOR
            snake.draw_grid_init()
            pygame.display.update()
            d=d-1
            y=y_start+d
        
        
        x_random,y_random=random

        if(snake.arr[x_random][y_random]==SNAKE_COLOR):
            len=len+1
            random=snake.draw_random()
            pygame.display.update()
        if(moved):       
            pop(len,len_old)
        print(len,len_old)
        len_old=len
    # pygame.display.update()                    
    pygame.time.delay(300)
    
    
   
    # print(snake_pos)
    
sys.exit()                        