import piece
import constants

class Pawn(piece.Piece):
    def __init__(self, color, pos):
        super().__init__(color, pos)
        self.name = constants.PAWN_NAME

    def __str__(self):
        return "P"

    def move():
        pass