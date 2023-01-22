import piece
import constants

class King(piece.Piece):
    def __init__(self, color, pos):
        super().__init__(color, pos)
        self.name = constants.get_king_name()

    def __str__(self):
        return "K"

    def move():
        pass