from pygame import image
import piece
from constants import WHITE_PIECE, BISHOP_NAME, MERIDA_PIECES


class Bishop(piece.Piece):
    def __init__(self, color):
        self.name = BISHOP_NAME
        if color == WHITE_PIECE:
            black_or_white_icon = "wB.svg"
        else:
            black_or_white_icon = "bB.svg"
        icon_path = MERIDA_PIECES + black_or_white_icon
        super().__init__(color, image.load(icon_path))

    def move(self):
        pass
