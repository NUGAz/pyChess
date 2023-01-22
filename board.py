import knight, king, rook, pawn, queen, bishop

class Board():
    def __init__(self):
        self.grid = [[None for _ in range(8)] for _ in range(8)]
        self.reset_board()

    def reset_board(self):
        self.grid[0][0] = rook.Rook("black", (0, 0))
        self.grid[0][1] = knight.Knight("black", (0, 1))
        self.grid[0][2] = bishop.Bishop("black", (0, 2))
        self.grid[0][3] = queen.Queen("black", (0, 3))
        self.grid[0][4] = king.King("black", (0, 4))
        self.grid[0][5] = bishop.Bishop("black", (0, 5))
        self.grid[0][6] = knight.Knight("black", (0, 6))
        self.grid[0][7] = rook.Rook("black", (0, 7))
        for i in range(8):
            self.grid[1][i] = pawn.Pawn("black", (1, i))
        self.grid[7][0] = rook.Rook("white", (7, 0))
        self.grid[7][1] = knight.Knight("white", (7, 1))
        self.grid[7][2] = bishop.Bishop("white", (7, 2))
        self.grid[7][3] = queen.Queen("white", (7, 3))
        self.grid[7][4] = king.King("white", (7, 4))
        self.grid[7][5] = bishop.Bishop("white", (7, 5))
        self.grid[7][6] = knight.Knight("white", (7, 6))
        self.grid[7][7] = rook.Rook("white", (7, 7))
        for i in range(8):
            self.grid[6][i] = pawn.Pawn("white", (6, i))

    def print_board(self):
        for i in range(8):
            for j in range(8):
                if(self.grid[i][j] == None):
                     print("_ ", end="")
                else:
                    print(self.grid[i][j].__str__() + " ", end="")
            print("\n")