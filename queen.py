import piece
import constants

class Queen(piece.Piece):
    def __init__(self, color, pos):
        super().__init__(color, pos)
        self.name = constants.get_queen_name()

    def __str__(self):
        return "Q"

    def move():
        pass