import pygame
from constants import BLACK, WHITE, DEFAULT_FONT, CENTER, TOP_LEFT, TOP_RIGHT, BOTTOM_LEFT, BOTTOM_RIGHT


class UiElement():
    def __init__(self):
        self.image = None
        self.rect = None

        def set():
            raise NotImplementedError

        def draw(self, screen):
            raise NotImplementedError

        def update():
            raise NotImplementedError


class Text(UiElement):
    def __init__(self, text, font_size, color=BLACK, font_name=DEFAULT_FONT):
        super().__init__()
        self.text = text
        self.color = color
        self.font_name = font_name
        self.font_size = font_size
        self.set_font()
        self.rect = self.image.get_rect()

    def set_font(self):
        self.font = pygame.font.SysFont(self.font_name, self.font_size)
        self.image = self.font.render(self.text, True, self.color)

    def update(self, **kwargs):
        if 'text_pos' in kwargs:
            pos = kwargs.pop('text_pos')
            self.rect.update(pos[0], pos[1], self.rect.w, self.rect.h)
        if 'text' in kwargs:
            self.text = kwargs.pop('text')
        if 'font_size' in kwargs:
            self.font_size = kwargs.pop('font_size')
            self.set_font()
            self.rect.w, self.rect.h = self.image.get_width(), self.image.get_height()
        if 'text_color' in kwargs:
            self.color = kwargs.pop('color')
        if 'font_name' in kwargs:
            self.font_name = kwargs.pop('font_name')

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def get_font_size(self):
        return self.font.size(self.text)


class Button(UiElement):
    def __init__(self, text, color=WHITE, font_size=0, text_anchor=None):
        super().__init__()
        self.image = pygame.display.get_surface()
        self.rect = pygame.Rect(0, 0, 0, 0)
        self.color = color
        self.text_anchor = text_anchor
        self.text = Text(text, font_size)
        self.text.set_font()
        self.set_text_position()

    def update(self, **kwargs):
        if 'rect_pos' in kwargs:
            pos = kwargs.pop('rect_pos')
            self.rect.update(pos[0], pos[1], self.rect.w, self.rect.h)
        if 'rect_size' in kwargs:
            size = kwargs.pop('rect_size')
            self.rect.update(self.rect.x, self.rect.y, size[0], size[1])
        if 'rect_color' in kwargs:
            self.color = kwargs.pop('color')
        self.text.update(**kwargs)
        self.set_text_position()

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)
        self.text.draw(screen)

    def set_text_position(self):
        if self.text_anchor is None:  # free positioning
            pass
        elif self.text_anchor == CENTER:
            x_pos = (self.rect.x + self.rect.w/2) - self.text.rect.w/2
            y_pos = (self.rect.y + self.rect.h/2) - \
                self.text.rect.h/2
            self.text.rect.update(
                x_pos, y_pos, self.text.rect.w, self.text.rect.h)
        elif self.text_anchor == TOP_LEFT:
            self.text.rect.update(self.rect.x, self.rect.y,
                                  self.text.rect.w, self.text.rect.h)
        elif self.text_anchor == TOP_RIGHT:
            x_pos = self.rect.x + (self.rect.w - self.text.rect.w)
            self.text.rect.update(x_pos, self.rect.y,
                                  self.text.rect.w, self.text.rect.h)
        elif self.text_anchor == BOTTOM_LEFT:
            y_pos = self.rect.y + (self.rect.h - self.text.rect.h)
            self.text.rect.update(self.rect.x, y_pos,
                                  self.text.rect.w, self.text.rect.h)
        elif self.text_anchor == BOTTOM_RIGHT:
            x_pos = self.rect.x + (self.rect.w - self.text.rect.w)
            y_pos = self.rect.y + (self.rect.h - self.text.rect.h)
            self.text.rect.update(x_pos, y_pos,
                                  self.text.rect.w, self.text.rect.h)
