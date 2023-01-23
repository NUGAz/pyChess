import board

class Chess:
    def __init__(self):
        self.chess_board = board.Board()
        self.rect_grid = [[None for _ in range(8)] for _ in range(8)]