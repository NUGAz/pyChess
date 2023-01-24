import math

"""
Game Config Related Constants
"""
#Window Size
ASPECT_RATIO = (4,3)
WINDOW_X = 1000
WINDOW_Y = 750
CENTER_X = WINDOW_X / 2
CENTER_Y = WINDOW_Y / 2
TITLE_FONT_SIZE = math.floor(WINDOW_X / 6)
GAME_FPS = 60

#Scaling factors

#RGB values
WHITE = (255, 255, 255)
CHESS_BOARD_WHITE = (250, 250, 250)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 128)

#Chess board square size
CHESS_BOARD_SQUARE_SIZE = 62.5
CHESS_BOARD_OFFSET = 90

"""
String Literals
"""
#Piece Names
BISHOP_NAME = "bishop"
KING_NAME = "king"
KNIGHT_NAME = "Knight"
PAWN_NAME = "pawn"
ROOK_NAME = "rook"
QUEEN_NAME = "queen"

"""
Screen States
"""

WELCOME_SCREEN = 0
MAIN_MENU_SCREEN = 1
CHESS_SCREEN = 2