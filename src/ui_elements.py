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
    def __init__(self, text, font_size, color=BLACK, font_name=DEFAULT_FONT):
        super().__init__(color)
        self.text = text
        self.font_name = font_name
        self.font_size = font_size
        self.set_font()
        self.rect = self.image.get_rect()

    def set_font(self):
        self.font = pygame.font.SysFont(self.font_name, self.font_size)
        self.image = self.font.render(self.text, True, self.color)
        
    def update(self, **kwargs):
        if 'pos' in kwargs:
            pos = kwargs.pop('pos')
            self.rect.update(pos[0], pos[1], self.rect.w, self.rect.h)
        if 'text' in kwargs:
            self.text = kwargs.pop('text')
        if 'font_size' in kwargs:
            self.font_size = kwargs.pop('font_size')
            self.set_font()
            self.rect.w, self.rect.h = self.image.get_width(), self.image.get_height()
        if 'color' in kwargs:
            self.color = kwargs.pop('color')
        if 'font_name' in kwargs:
            self.font_name = kwargs.pop('font_name')

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