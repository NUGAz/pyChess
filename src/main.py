import pygame
from scenes import SceneManager
import constants


def draw_rect(x, y, width, height, color):
    rect = pygame.Rect(x, y, width, height)
    return pygame.draw.rect(screen, color, rect)


def draw_button(x, y, width, height, color, text):
    button = pygame.Rect(x, y, width, height)
    pygame.draw.rect(screen, color, button)
    draw_text(text, button_font, constants.BLACK, x, y)
    return button


def draw_line(start_x, start_y, end_x, end_y, color):
    pygame.draw.line(screen, color, (start_x, start_y), (end_x, end_y))


def draw_chess_board():
    square_size = constants.CHESS_BOARD_SQUARE_SIZE
    offset = constants.CHESS_BOARD_OFFSET
    size_offseted = square_size + offset
    square_color_1 = constants.CHESS_BOARD_WHITE
    square_color_2 = constants.BLACK

    for i in range(1, 9):
        for j in range(1, 9, 2):
            x_pos = square_size * j + offset
            chess_game.rect_grid[i-1][j-1] = draw_rect(
                x_pos, square_size * i, square_size, square_size, square_color_1)
            chess_game.rect_grid[i-1][j] = draw_rect(
                x_pos + square_size, square_size * i, square_size, square_size, square_color_2)

        temp_color = square_color_1
        square_color_1 = square_color_2
        square_color_2 = temp_color

        # top horizontal
        draw_line(size_offseted, square_size, square_size *
                  9 + offset, square_size, constants.BLACK)

        # left vertical
        draw_line(size_offseted, square_size, size_offseted,
                  square_size*9, constants.BLACK)

        # right vertical
        draw_line(square_size*9 + offset, square_size, square_size *
                  9 + offset, square_size*9, constants.BLACK)

        # bottom horizontal
        draw_line(size_offseted, square_size*9, square_size *
                  9 + offset, square_size*9, constants.BLACK)


def calculate_new_window_size(resizable_event):
    new_width, new_height = resizable_event[0].size

    aspect_ratio = new_width / new_height

    if aspect_ratio != constants.ASPECT_RATIO[0] / constants.ASPECT_RATIO[1]:
        if aspect_ratio > constants.ASPECT_RATIO[0] / constants.ASPECT_RATIO[1]:
            new_height = int(
                new_width / constants.ASPECT_RATIO[0] * constants.ASPECT_RATIO[1])
        else:
            new_width = int(
                new_height * constants.ASPECT_RATIO[0] / constants.ASPECT_RATIO[1])

    pygame.display.set_mode((new_width, new_height), pygame.RESIZABLE)


if __name__ == "__main__":
    pygame.init()
    pygame.display.set_caption('Welcome to pyChess')
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode(
        constants.DEFAULT_WINDOW_SIZE, pygame.RESIZABLE)

    scene_manager = SceneManager()
    event = pygame.event

    RUNNING = True
    while RUNNING:
        clock.tick(constants.GAME_FPS)

        if pygame.event.peek(pygame.VIDEORESIZE):
            calculate_new_window_size(pygame.event.get(pygame.VIDEORESIZE))
        if pygame.event.get(pygame.QUIT):
            RUNNING = False
            pygame.quit()

        if RUNNING:
            scene_manager.scene.handle_events(pygame.event.get())
            scene_manager.scene.update()
            scene_manager.scene.render(screen)
            pygame.display.flip()
