import pygame
import board
import constants

from pygame.locals import *

class Square(pygame.sprite.Sprite):
    def __init__(self):
        super(Square, self).__init__()
        self.surf = pygame.Surface((25, 25))
        self.surf.fill(constants.BLUE)
        self.rect = self.surf.get_rect()

if __name__ == "__main__":
    pygame.init()
    screen = pygame.display.set_mode((constants.WINDOW_X, constants.WINDOW_Y))
    pygame.display.set_caption('Welcome to pyChess')

    smallfont = pygame.font.SysFont('Corbel',35) 
    text = smallfont.render('quit' , True , constants.WHITE) 

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == KEYDOWN:

                if event.key == K_BACKSPACE:
                    running = False
                    
            if event.type == pygame.MOUSEBUTTONDOWN: 
                pass

        pygame.display.flip()