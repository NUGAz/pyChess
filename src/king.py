from pygame import image
import piece
from constants import WHITE_PIECE, KING_NAME, MERIDA_PIECES


class King(piece.Piece):
    def __init__(self, color):
        self.name = KING_NAME
        if color == WHITE_PIECE:
            black_or_white_icon = "wK.svg"
        else:
            black_or_white_icon = "bK.svg"
        icon_path = MERIDA_PIECES + black_or_white_icon
        super().__init__(color, image.load(icon_path))

    def move(self):
        pass
