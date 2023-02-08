import piece
from constants import WHITE_PIECE, BLACK_PIECE, KING_NAME, MERIDA_PIECES
from pygame import image, display, transform


class King(piece.Piece):
    def __init__(self, color):
        super().__init__(color)
        self.name = KING_NAME
        if color == WHITE_PIECE:
            black_or_white_icon = "wK.svg"
        else:
            black_or_white_icon = "bK.svg"
        self.image = image.load(MERIDA_PIECES + black_or_white_icon)

    def set_image(self, square_rect):
        self.image = transform.smoothscale(
            self.image, (square_rect.w, square_rect.h))
        display.get_surface().blit(self.image, square_rect)

    def get_image(self):
        return self.image

    def move(self):
        pass
