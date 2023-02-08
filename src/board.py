import pygame
import knight
import king
import rook
import pawn
import queen
import bishop
from piece import Piece
from constants import BLACK, CHESS_BOARD_BLACK, CHESS_BOARD_WHITE, WHITE, ASPECT_RATIO_FRACTION, WHITE_PIECE, BLACK_PIECE


class BoardSquare():
    def __init__(self):
        self.rect = None
        self.piece = None


class Board():
    def __init__(self):
        self.grid = [[BoardSquare() for _ in range(8)] for _ in range(8)]
        self.dragged_piece = Piece(None)
        self.initialize_chess_board()
        self.reset_board()

    def reset_board(self):
        # Black Pieces
        self.grid[0][0].piece = rook.Rook(BLACK_PIECE)
        self.grid[0][1].piece = knight.Knight(BLACK_PIECE)
        self.grid[0][2].piece = bishop.Bishop(BLACK_PIECE)
        self.grid[0][3].piece = queen.Queen(BLACK_PIECE)
        self.grid[0][4].piece = king.King(BLACK_PIECE)
        self.grid[0][5].piece = bishop.Bishop(BLACK_PIECE)
        self.grid[0][6].piece = knight.Knight(BLACK_PIECE)
        self.grid[0][7].piece = rook.Rook(BLACK_PIECE)

        # White Pieces
        self.grid[7][0].piece = rook.Rook(WHITE_PIECE)
        self.grid[7][1].piece = knight.Knight(WHITE_PIECE)
        self.grid[7][2].piece = bishop.Bishop(WHITE_PIECE)
        self.grid[7][3].piece = queen.Queen(WHITE_PIECE)
        self.grid[7][4].piece = king.King(WHITE_PIECE)
        self.grid[7][5].piece = bishop.Bishop(WHITE_PIECE)
        self.grid[7][6].piece = knight.Knight(WHITE_PIECE)
        self.grid[7][7].piece = rook.Rook(WHITE_PIECE)

        # Pawns
        for i in range(8):
            self.grid[6][i].piece = pawn.Pawn(WHITE_PIECE)
            self.grid[1][i].piece = pawn.Pawn(BLACK_PIECE)

    def draw_rect(self, screen, x, y, width, height, color):
        rect = pygame.Rect(x, y, width, height)
        return pygame.draw.rect(screen, color, rect)

    def initialize_chess_board(self):
        self.draw_board()
        self.set_piece_images()

    def draw_board(self):
        window_x = pygame.display.Info().current_w
        window_y = pygame.display.Info().current_h

        screen = pygame.display.get_surface()

        screen.fill(WHITE)

        # board will cover 85% of the vertical height of the screen
        square_size = self.get_square_size()
        board_size = 8 * square_size
        x_board_offset = (window_x - board_size) / 2
        y_board_offset = (window_y - board_size) / 2
        square_color_white = CHESS_BOARD_WHITE
        square_color_black = CHESS_BOARD_BLACK

        for i in range(1, 9):
            for j in range(1, 9, 2):
                x_pos = square_size * (j-1) + x_board_offset
                y_pos = square_size * (i-1) + y_board_offset
                self.grid[i-1][j-1].rect = self.draw_rect(screen,
                                                          x_pos, y_pos, square_size,
                                                          square_size, square_color_white)
                self.grid[i-1][j].rect = self.draw_rect(screen,
                                                        x_pos + square_size, y_pos,
                                                        square_size, square_size, square_color_black)

            temp_color = square_color_white
            square_color_white = square_color_black
            square_color_black = temp_color

        # top horizontal
        pygame.draw.line(screen, BLACK, (x_board_offset, y_board_offset),
                         (self.grid[0][7].rect.x + square_size, y_board_offset))

        # left vertical
        pygame.draw.line(screen, BLACK, (x_board_offset, y_board_offset),
                         (x_board_offset, self.grid[7][0].rect.y + square_size))

        # right vertical
        pygame.draw.line(screen, BLACK, (self.grid[0][7].rect.x + square_size, y_board_offset),
                         (self.grid[0][7].rect.x + square_size, self.grid[7][0].rect.y + square_size))

        # bottom horizontal
        pygame.draw.line(screen, BLACK, (x_board_offset, self.grid[7][0].rect.y + square_size),
                         (self.grid[0][7].rect.x + square_size, self.grid[7][0].rect.y + square_size))

    def get_square_size(self):
        window_x = pygame.display.Info().current_w
        window_y = pygame.display.Info().current_h
        return min(window_y * 0.80 / 8, window_x *
                   0.9 / ASPECT_RATIO_FRACTION / 8)

    def set_piece_images(self):
        for i in range(8):
            for j in range(8):
                if self.grid[i][j].piece is not None:
                    self.grid[i][j].piece.set_image(self.grid[i][j].rect)

    def set_dragged_piece(self, pos):
        self.dragged_piece = self.grid[pos[0]][pos[1]].piece

    def set_moved_piece(self, pos):
        self.grid[pos[0]][pos[1]].piece = self.dragged_piece
        self.dragged_piece = None

    def get_dropped_square(self, mouse_pos):
        square_size = self.get_square_size()
        if mouse_pos[1] < self.grid[0][0].rect.y or mouse_pos[1] > self.grid[7][0].rect.y + square_size:
            return False

        if mouse_pos[0] > self.grid[0][7].rect.x + square_size or mouse_pos[0] < self.grid[0][0].rect.x:
            return False

        y_pos = x_pos = 0
        for i in range(8):
            if mouse_pos[0] < self.grid[0][i].rect.x + square_size:
                y_pos = i
                break

        for i in range(8):
            if mouse_pos[1] < self.grid[i][0].rect.y + square_size:
                x_pos = i
                break

        if self.dragged_piece == self.grid[x_pos][y_pos]:
            return False
        return (x_pos, y_pos)
