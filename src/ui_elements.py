import pygame
from constants import BLACK, DEFAULT_FONT


class Text(pygame.sprite.Sprite):
    def __init__(self, text, size, color=BLACK, font=DEFAULT_FONT, **kwargs):
        super(Text, self).__init__()
        self.text = text
        self.color = color
        self.font = pygame.font.SysFont(font, size)
        self.kwargs = kwargs
        self.set()

    def set(self):
        self.image = self.font.render(str(self.text), True, self.color)
        self.rect = self.image.get_rect(**self.kwargs)

    def update(self, size, font=DEFAULT_FONT):
        self.font = pygame.font.SysFont(font, size)
        self.set()

    def get_font_size(self):
        return self.font.size(self.text)


class Button:
    def __init__(self, surface, pos, text='', anchor='top-left'):
        self.surface = surface
        if anchor == 'center':
            self.pos = tuple(
                pos, (self.surface.get_width()/2, self.surface.get_height()/2))
        else:
            self.pos = pos
        self.text = Text(text, add_tuple(self.pos, (self.surface.get_width(
        )/2, self.surface.get_height()/2)), anchor='center')
