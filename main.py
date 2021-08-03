from utils.config import *
from utils.snake import *
WIN=pygame.display.set_mode((WIDTH,HEIGHT))

snake=snake(WIN)
snake.grid_init()
snake.draw_grid_init(0)
snake.init_snake()
run=True
while(run):
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    pygame.display.update()                    

sys.exit()                        