import piece
import constants

class Bishop(piece.Piece):
    def __init__(self, color, pos):
        super().__init__(color, pos)
        self.name = constants.BISHOP_NAME

    def __str__(self):
        return "B"

    def move():
        pass