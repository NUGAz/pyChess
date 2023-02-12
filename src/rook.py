from pygame import image
import piece
from constants import WHITE_PIECE, ROOK_NAME, MERIDA_PIECES


class Rook(piece.Piece):
    def __init__(self, color):
        self.name = ROOK_NAME
        if color == WHITE_PIECE:
            black_or_white_icon = "wR.svg"
        else:
            black_or_white_icon = "bR.svg"
        icon_path = MERIDA_PIECES + black_or_white_icon
        super().__init__(color, image.load(icon_path))

    def move(self):
        pass
