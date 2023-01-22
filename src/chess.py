import pygame
import board
import constants

from pygame.locals import *

class Square(pygame.sprite.Sprite):
    def __init__(self):
        super(Square, self).__init__()
        self.surf = pygame.Surface((25, 25))
        self.surf.fill((0,255,255))
        self.rect = self.surf.get_rect()

class Chess:
    def __init__(self):
        self.chess_board = board.Board()

def draw_board():
    square1 = Square()
    square2 = Square()
    square3 = Square()
    square4 = Square()
    screen.blit(square1.surf, (40, 40))
    screen.blit(square2.surf, (40, 530))
    screen.blit(square3.surf, (730, 40))
    screen.blit(square4.surf, (730, 530))


if __name__ == "__main__":
    pygame.init()
    screen = pygame.display.set_mode((constants.WINDOW_X, constants.WINDOW_Y))
    draw_board()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == KEYDOWN:

                if event.key == K_BACKSPACE:
                    running = False
                    
            elif event.type == QUIT:
                gameOn = False
    
        pygame.display.flip()