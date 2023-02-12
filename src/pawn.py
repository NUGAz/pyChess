import piece
from constants import WHITE_PIECE, BLACK_PIECE, PAWN_NAME, MERIDA_PIECES
from pygame import image, display, transform


class Pawn(piece.Piece):
    def __init__(self, color):
        super().__init__(color)
        self.name = PAWN_NAME
        self._first_move = True
        if color == WHITE_PIECE:
            black_or_white_icon = "wP.svg"
        else:
            black_or_white_icon = "bP.svg"
        self.image = image.load(MERIDA_PIECES + black_or_white_icon)

    def set_image(self, square_rect):
        self.image = transform.smoothscale(
            self.image, (square_rect.w, square_rect.h))
        display.get_surface().blit(self.image, square_rect)

    def get_image(self):
        return self.image

    @property
    def first_move(self):
        return self._first_move

    @first_move.setter
    def first_move(self, first_move_false=False):
        self._first_move = first_move_false

    def move(self):
        valid_moves = [(1, 0)]
        if self._first_move:
            valid_moves.append((2, 0))
        return valid_moves
