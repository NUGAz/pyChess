import piece
import constants

class Knight(piece.Piece):
    def __init__(self, color, pos):
        super().__init__(color, pos)
        self.name = constants.KNIGHT_NAME

    def __str__(self):
        return "N"
        
    def move():
        pass