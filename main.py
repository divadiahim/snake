from utils.text import Button_img
from utils.config import *
from utils.snake import *
WIN=pygame.display.set_mode((WIDTH,HEIGHT))
img_run = pygame.image.load("img/image.png").convert_alpha()
snake=snake(WIN)
# snake.grid_init()
# snake.draw_grid_init(0)
# snake.init_snake()

text=Button_img(img_run,(WIDTH//6,HEIGHT//2),0.35)
run=True
WIN.set_alpha(255)
while(run):
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                snake.fade(0,255,1)
                snake.fade(255,0,-1)
        text.draw(WIN)        
    pygame.display.update()                    

sys.exit()                        