import pygame
import chess
import constants
import math

from pygame.locals import *

play_button = None
exit_button = None

WINDOW_X = 1000
WINDOW_Y = 750

def draw_text(text, font, text_color, x, y):
    img = font.render(text, True, text_color)
    screen.blit(img, (x,y))

def draw_rect(x, y, width, height, color):
    rect = pygame.Rect(x, y, width, height)
    pygame.draw.rect(screen, color, rect)

def draw_button(x, y, width, height, color, text):
    button = pygame.Rect(x, y, width, height)
    pygame.draw.rect(screen, color, button)
    draw_text(text, button_font, constants.BLACK, x, y)
    return button

def draw_line(start_x, start_y, end_x, end_y, color):
    pygame.draw.line(screen, color, (start_x, start_y), (end_x, end_y))

def reset_screen():
    screen.fill(constants.WHITE)

def draw_main_title():
    chess_font_width, _ = title_font.size(constants.TITLE_CHESS)
    start_font_width, _ = start_font.size(constants.TITLE_START_SPACE)
    center_x = WINDOW_X/2


    draw_text(constants.TITLE_PY, start_font, constants.BLACK, WINDOW_X * 0.19, WINDOW_Y * 0.13)
    draw_text(constants.TITLE_CHESS, title_font, constants.BLACK, (center_x - chess_font_width / 2), WINDOW_Y * 0.20)
    draw_text(constants.TITLE_START_SPACE, start_font, constants.BLACK, (center_x - start_font_width / 2), WINDOW_Y * 0.80)

def draw_main_menu():
    global play_button
    global exit_button

    draw_text("py", title_font, constants.BLACK, 150, 20)
    draw_text("Chess", title_font, constants.BLACK, 250, 100)

    play_button = draw_button(350, 400, 100, 50, constants.WHITE, "Play")
    exit_button = draw_button(350, 500, 100, 50, constants.WHITE, "Exit")

def draw_chess_board():
    square_size = constants.CHESS_BOARD_SQUARE_SIZE
    offset = constants.CHESS_BOARD_OFFSET
    size_offseted = square_size + offset
    square_color_1 = constants.CHESS_BOARD_WHITE
    square_color_2 = constants.BLACK

    for i in range(1, 9):
        for j in range(1, 9, 2):
            x_pos = square_size * j + offset
            chess_game.rect_grid[i-1][j-1] = draw_rect(x_pos, square_size * i, square_size, square_size,square_color_1)
            chess_game.rect_grid[i-1][j] = draw_rect(x_pos + square_size, square_size * i, square_size, square_size, square_color_2)

        temp_color = square_color_1
        square_color_1 = square_color_2
        square_color_2 = temp_color


        #top horizontal
        draw_line(size_offseted, square_size, square_size*9 + offset, square_size, constants.BLACK)

        #left vertical
        draw_line(size_offseted, square_size, size_offseted, square_size*9, constants.BLACK)

        #right vertical
        draw_line(square_size*9 + offset, square_size, square_size*9 + offset, square_size*9, constants.BLACK)

        #bottom horizontal
        draw_line(size_offseted, square_size*9, square_size*9 + offset, square_size*9, constants.BLACK)

def draw_scene(scene_state):
    if(scene_state == constants.WELCOME_SCREEN):
        draw_main_title()
    if(scene_state == constants.MAIN_MENU_SCREEN):
        draw_main_menu()
    if(scene_state == constants.CHESS_SCREEN):
        draw_chess_board()

def calculate_new_window_size(event):
            global WINDOW_X
            global WINDOW_Y

            new_width, new_height = event.size
            
            aspect_ratio = new_width / new_height
            
            if aspect_ratio != constants.ASPECT_RATIO[0] /constants.ASPECT_RATIO[1]:
                if aspect_ratio > constants.ASPECT_RATIO[0] / constants.ASPECT_RATIO[1]:
                    new_height = int(new_width / constants.ASPECT_RATIO[0] * constants.ASPECT_RATIO[1])
                else:
                    new_width = int(new_height * constants.ASPECT_RATIO[0] / constants.ASPECT_RATIO[1])
            
            WINDOW_X = new_width
            WINDOW_Y = new_height
            # Resize the window to the new size
            pygame.display.set_mode((new_width, new_height), pygame.RESIZABLE)
            reset_screen()


if __name__ == "__main__":
    pygame.init()
    pygame.display.set_caption('Welcome to pyChess')
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((WINDOW_X, WINDOW_Y), pygame.RESIZABLE)
    current_state = constants.WELCOME_SCREEN
    
    chess_game = chess.Chess()

    title_font = pygame.font.SysFont("arial", math.floor(WINDOW_X * 0.20))
    start_font = pygame.font.SysFont("arial", math.floor(WINDOW_X * 0.05))
    button_font = pygame.font.SysFont("arial", math.floor(WINDOW_X * 0.10))

    reset_screen()
    running = True
    while running:
        draw_scene(current_state)
        for event in pygame.event.get():
            if event.type == VIDEORESIZE:
                calculate_new_window_size(event)

            if event.type == KEYDOWN:

                if event.key == K_BACKSPACE:
                    if(current_state == constants.WELCOME_SCREEN):
                        running = False

                    reset_screen()
                    current_state = current_state - 1 

                if event.key == K_SPACE:
                    if(current_state == constants.WELCOME_SCREEN):
                        current_state = constants.MAIN_MENU_SCREEN
                        reset_screen()
                    
            if event.type == MOUSEBUTTONDOWN: 
                    mouse_pos = pygame.mouse.get_pos()
                    if play_button.collidepoint(mouse_pos):
                        if(current_state == constants.MAIN_MENU_SCREEN):
                            current_state = constants.CHESS_SCREEN
                            reset_screen()

                    elif exit_button.collidepoint(mouse_pos):
                        running = False

            
            if event.type == QUIT:
                running = False
        pygame.display.flip()
    pygame.quit()