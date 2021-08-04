from .snake import *

# class Button:
#     def __init__(self,text,pos):
#         # top rectangle
#         # text
#         smallfont = pygame.font.SysFont('Corbel', 55)
#         self.text_surf = smallfont.render(text, True, SNAKE_COLOR)
#         self.poz=pos

#     def draw(self,win):
#         win.blit(self.text_surf,self.poz)

class Button_img:
    def __init__(self, image,pos, scale):
        width = image.get_width()
        height = image.get_height()
        self.image = pygame.transform.scale(
            image, (int(width * scale), int(height * scale)))
        self.rect = self.image.get_rect()
        self.rect.topleft = pos
        
    def draw(self, win):
        
        win.blit(self.image, (self.rect.x, self.rect.y))
    