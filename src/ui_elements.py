import pygame
from utils import add_tuples, sub_tuples
from constants import BLACK, WHITE, DEFAULT_FONT

class UiElement(pygame.sprite.Sprite):
    def __init__(self, color):
        pygame.sprite.Sprite.__init__(self)
        self.image = None
        self.rect = None
        self.color = color

        def set():
            raise NotImplementedError
        
        def draw(screen):
            screen.blit(self.image, self.rect)
        
        def update():
            pass
        
class Text(UiElement):
    def __init__(self, x, y, text, font_size, color=BLACK, font=DEFAULT_FONT):
        super().__init__(color)
        self.text = text
        self.font_name = font
        self.font_size = font_size
        self.font = pygame.font.SysFont(self.font_name, self.font_size)
        self.image = self.font.render(self.text, True, self.color)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update(self, **kwargs):
        if 'x' in kwargs:
            self.rect.x = kwargs['x']
        if 'y' in kwargs:
            self.rect.y = kwargs['y']
        if 'text' in kwargs:
            self.text = kwargs['text']
        if 'font_size' in kwargs:
            self.font_size = kwargs['font_size']
        if 'color' in kwargs:
            self.color = kwargs['color']
        if 'font_name' in kwargs:
            self.font_name = kwargs['font_name']

        self.font = pygame.font.SysFont(self.font_name, self.font_size)
        self.image = self.font.render(self.text, True, self.color)
        self.rect = self.image.get_rect(**kwargs)

    def get_font_size(self):
        return self.font.size(self.text)


class Button(UiElement):
    def __init__(self, x, y, color=WHITE, surface=None, text='', font_size=0, anchor='top-left'):
        super().__init__(x, y, color)
        if(surface == None):
            self.surface = pygame.display.get_surface()
        else:
            self.surface = surface

        self.text = Text(x + self.surface.get_width()/2, y + self.surface.get_height()/2,
                         0, 0, text, font_size)

        self.set()
    
    def set(self):
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.text.set()
    
    def draw(self, screen):
        screen.blit(self.rect, (self.x, self.y))