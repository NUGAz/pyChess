from os import path
"""
Game Config Related Constants
"""
# Window Size
ASPECT_RATIO = (16, 9)
GAME_FPS = 60
DEFAULT_FONT = 'arial'
DEFAULT_WINDOW_SIZE = (1280, 720)

"""
File and Folder Costants
"""
# Folders
SOUND_FX_PATH = "assets/sounds/"
ICONS_PATH = "assets/icons/"

#
# SOUND_FX_PATH = path.dirname(__file__) #ICONS_PATH = path.dirname(__file__)

# Sound Files
START_SOUND_EFFECT = "start_sound.wav"

# Image Files
CHESS_BG = "chess_bg.png"

# RGB values
WHITE = (255, 255, 255)
CHESS_BOARD_WHITE = (250, 250, 250)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 128)

# Chess board square size
CHESS_BOARD_SQUARE_SIZE = 62.5
CHESS_BOARD_OFFSET = 90

"""
String Literals
"""
# Piece Names
BISHOP_NAME = "bishop"
KING_NAME = "king"
KNIGHT_NAME = "Knight"
PAWN_NAME = "pawn"
ROOK_NAME = "rook"
QUEEN_NAME = "queen"

# Title_Texts
TITLE_CHESS = "Chess"
TITLE_PY = "py"
TITLE_START_SPACE = "Press Space to advance"

# Main Menu Texts
PLAY_BUTTON = "Play"
OPTIONS_BUTTON = "Options"
EXIT_BUTTON = "Exit"

# Anchors
CENTER = "center"
TOP_LEFT = "top-left"
TOP_RIGHT = "top-right"
BOTTOM_RIGHT = "bottom-right"
BOTTOM_LEFT = "bottom-left"

"""
Screen States
"""

WELCOME_SCREEN = 0
MAIN_MENU_SCREEN = 1
CHESS_SCREEN = 2
