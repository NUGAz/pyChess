from pygame import image
import piece
from constants import WHITE_PIECE, PAWN_NAME, MERIDA_PIECES


class Pawn(piece.Piece):
    def __init__(self, color):
        if color == WHITE_PIECE:
            black_or_white_icon = "wP.svg"
        else:
            black_or_white_icon = "bP.svg"
        icon_path = MERIDA_PIECES + black_or_white_icon
        super().__init__(color, image.load(icon_path))

        self.name = PAWN_NAME
        self._first_move = True

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
