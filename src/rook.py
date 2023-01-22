import piece
import constants

class Rook(piece.Piece):
    def __init__(self, color, pos):
        super().__init__(color, pos)
        self.name = constants.get_rook_name()

    def __str__(self):
        return "R"

    def move():
        pass