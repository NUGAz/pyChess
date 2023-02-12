from pygame import image
import piece
from constants import WHITE_PIECE, KNIGHT_NAME, MERIDA_PIECES


class Knight(piece.Piece):
    def __init__(self, color):
        self.name = KNIGHT_NAME
        if color == WHITE_PIECE:
            black_or_white_icon = "wN.svg"
        else:
            black_or_white_icon = "bN.svg"
        icon_path = MERIDA_PIECES + black_or_white_icon
        super().__init__(color, image.load(icon_path))

    def move(self):
        pass
