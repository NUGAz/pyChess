from pygame import image
import piece
from constants import WHITE_PIECE, QUEEN_NAME, MERIDA_PIECES


class Queen(piece.Piece):
    def __init__(self, color):
        self.name = QUEEN_NAME
        if color == WHITE_PIECE:
            black_or_white_icon = "wQ.svg"
        else:
            black_or_white_icon = "bQ.svg"
        icon_path = MERIDA_PIECES + black_or_white_icon
        super().__init__(color, image.load(icon_path))

    def move(self):
        pass
