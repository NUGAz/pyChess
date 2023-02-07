import piece
from constants import WHITE_PIECE, BLACK_PIECE, ROOK_NAME, MERIDA_PIECES
from pygame import image, display, transform


class Rook(piece.Piece):
    def __init__(self, color):
        super().__init__(color)
        self.name = ROOK_NAME
        if color == WHITE_PIECE:
            black_or_white_icon = "wR.svg"
        else:
            black_or_white_icon = "bR.svg"
        self.image = image.load(MERIDA_PIECES + black_or_white_icon)
        self.rect = self.image.get_rect()

    def set_image(self, square_rect):
        screen = display.get_surface()
        self.image = transform.smoothscale(
            self.image, (square_rect.w, square_rect.h))
        self.rect = square_rect
        screen.blit(self.image, self.rect)

    def update_image(self, pos):
        self.rect.center = pos
        screen = display.get_surface()
        screen.blit(self.image, self.rect)

    def get_image(self):
        return self.image.get_rect()

    def move(self):
        pass
