import pygame
import board

class Chess:
    def __init__(self):
        self.chess_board = board.Board()

if __name__ == "__main__":
    chess_game = Chess()
    chess_game.chess_board.print_board()