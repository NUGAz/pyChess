import piece
import constants

class Knight(piece.Piece):
    def __init__(self, color, pos):
        super().__init__(color, pos)
        self.name = constants.get_knight_name()

    def __str__(self):
        return "N"
        
    def move():
        pass