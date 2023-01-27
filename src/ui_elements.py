import pygame
from utils import add_tuples, sub_tuples
from constants import BLACK, WHITE,  DEFAULT_FONT

class UiElement(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color

        def set():
            raise NotImplementedError
        
        def draw(screen):
            raise NotImplementedError
        
        def update():
            raise NotImplementedError


class Text(UiElement):
    def __init__(self, x, y, width, height, text, font_size, color=BLACK, font=DEFAULT_FONT):
        super().__init__(x, y, width, height, color)
        self.text = text
        self.font_size = font_size
        self.font = pygame.font.SysFont(font, self.font_size)
        self.set()

    def set(self):
        self.image = self.font.render(str(self.text), True, self.color)
        self.rect = self.image.get_rect()

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))

    def update(self, x, y, font_size, font=DEFAULT_FONT):
        self.font_size = font_size
        self.font = pygame.font.SysFont(font, self.font_size)
        self.x = x
        self.y = y
        self.set()

    def get_font_size(self):
        return self.font.size(self.text)


class Button(UiElement):
    def __init__(self, x, y, width, height, color=WHITE, surface=None, text='', anchor='top-left'):
        super().__init__(x, y, width, height, color)
        if(surface == None):
            self.surface = pygame.display.get_surface()
        else:
            self.surface = surface

        self.text = Text(text, add_tuples(self.pos, (self.surface.get_width(
        )/2, self.surface.get_height()/2)))

        self.set()
    
    def set(self):
        pygame.Rect(self.pos[0], self.pos[1], self.size[0] , self.size[0])
    