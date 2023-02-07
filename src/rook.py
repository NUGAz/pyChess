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

    def set_image(self, square_rect):
        screen = display.get_surface()
        self.image = transform.smoothscale(
            self.image, (square_rect.w, square_rect.h))
        screen.blit(self.image, square_rect)

    def move():
        pass
