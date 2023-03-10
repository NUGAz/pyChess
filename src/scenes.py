from math import floor
import pygame
from ui_elements import Text, Button
from board import Board
import utils
import constants


class Scene():
    def __init__(self):
        pass

    def render(self, screen):
        raise NotImplementedError

    def update(self):
        raise NotImplementedError

    def handle_events(self, events):
        raise NotImplementedError


class SceneManager():
    def __init__(self):
        self.go_to(TitleScreen())

    def go_to(self, scene):
        self.scene = scene
        self.scene.manager = self


class TitleScreen(Scene):
    def __init__(self):
        super().__init__()
        self.py_text = Text(constants.TITLE_PY, floor(
            pygame.display.Info().current_w * 0.05))
        self.title_text = Text(constants.TITLE_CHESS, floor(
            pygame.display.Info().current_w * 0.20))
        self.start_text = Text(constants.TITLE_START_SPACE, floor(
            pygame.display.Info().current_w * 0.05))

        self.start_text_blinking = 1
        self.start_sound = pygame.mixer.Sound(
            constants.SOUND_FX_PATH + constants.START_SOUND_EFFECT)

    def render(self, screen):
        screen.fill(constants.WHITE)

        self.py_text.draw(screen)
        self.title_text.draw(screen)
        self.start_text.draw(screen)

    def update(self):
        window_x = pygame.display.Info().current_w
        window_y = pygame.display.Info().current_h

        center_x = window_x/2

        self.py_text.update(text_pos=(center_x/2.5, window_y * 0.12),
                            font_size=floor(window_x * 0.03 * constants.ASPECT_RATIO_FRACTION))
        self.title_text.update(text_pos=(center_x-self.title_text.rect.width/2,
                               window_y * 0.15), font_size=floor(window_x * 0.10 * constants.ASPECT_RATIO_FRACTION))

        self.calculate_blinking_animation(self.start_text.color)
        self.start_text.color = utils.add_to_tuple(
            self.start_text_blinking, self.start_text.color)
        self.start_text.update(text_pos=(center_x - self.start_text.rect.width/2,
                               window_y * 0.80), font_size=floor(window_x * 0.03 * constants.ASPECT_RATIO_FRACTION))

    def calculate_blinking_animation(self, color_value_tuple):
        if (color_value_tuple == constants.WHITE):
            self.start_text_blinking = -3
        elif (color_value_tuple == constants.BLACK):
            self.start_text_blinking = 3

    def handle_events(self, events):
        for event in events:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                pygame.mixer.Sound.play(self.start_sound)
                pygame.time.delay(1000)
                self.manager.go_to(MainMenuScreen())


class MainMenuScreen(Scene):
    def __init__(self):
        super().__init__()
        self.py_text = Text(constants.TITLE_PY, floor(
            pygame.display.Info().current_w * 0.02))
        self.title_text = Text(constants.TITLE_CHESS,
                               floor(pygame.display.Info().current_w * 0.10))
        self.bg_image = pygame.transform.scale(pygame.image.load(constants.ICONS_PATH + constants.CHESS_BG).convert_alpha(),
                                               (pygame.display.Info().current_w, pygame.display.Info().current_w))

        self.play_button = Button(
            constants.PLAY_BUTTON, text_anchor=constants.CENTER)
        self.options_button = Button(
            constants.OPTIONS_BUTTON, text_anchor=constants.CENTER)
        self.exit_button = Button(
            constants.EXIT_BUTTON, text_anchor=constants.CENTER)

    def render(self, screen):
        screen.fill(constants.WHITE)

        self.py_text.draw(screen)
        self.title_text.draw(screen)

        self.play_button.draw(screen)
        self.options_button.draw(screen)
        self.exit_button.draw(screen)

    def update(self):
        window_x = pygame.display.Info().current_w
        window_y = pygame.display.Info().current_h

        center_x = window_x/2

        self.py_text.update(text_pos=(center_x/1.45, window_y * 0.09),
                            font_size=floor(window_x * 0.015 * constants.ASPECT_RATIO_FRACTION))
        self.title_text.update(text_pos=(center_x-self.title_text.rect.w/2,
                               window_y * 0.10), font_size=floor(window_x * 0.05 * constants.ASPECT_RATIO_FRACTION))

        self.play_button.update(
            rect_pos=(center_x-self.play_button.rect.w / 2,
                      window_y * 0.25 * constants.ASPECT_RATIO_FRACTION),
            rect_size=(window_x * 0.07 * constants.ASPECT_RATIO_FRACTION,
                       window_y * 0.07 * constants.ASPECT_RATIO_FRACTION),
            font_size=floor(window_x * 0.03 * constants.ASPECT_RATIO_FRACTION))

        self.options_button.update(
            rect_pos=(center_x-self.options_button.rect.w / 2,
                      window_y * 0.35 * constants.ASPECT_RATIO_FRACTION),
            rect_size=(window_x * 0.1 * constants.ASPECT_RATIO_FRACTION,
                       window_y * 0.07 * constants.ASPECT_RATIO_FRACTION),
            font_size=floor(window_x * 0.03 * constants.ASPECT_RATIO_FRACTION))

        self.exit_button.update(
            rect_pos=(center_x-self.exit_button.rect.w / 2,
                      window_y * 0.45 * constants.ASPECT_RATIO_FRACTION),
            rect_size=(window_x * 0.07 * constants.ASPECT_RATIO_FRACTION,
                       window_y * 0.07 * constants.ASPECT_RATIO_FRACTION),
            font_size=floor(window_x * 0.03 * constants.ASPECT_RATIO_FRACTION))

    def handle_events(self, events):
        for event in events:
            mouse_pos = pygame.mouse.get_pos()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_BACKSPACE:
                self.manager.go_to(TitleScreen())

            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.play_button.is_mouse_over(mouse_pos):
                    self.manager.go_to(GameScene())
                    pass
                elif self.options_button.is_mouse_over(mouse_pos):
                    # go to options scene
                    pass
                elif self.exit_button.is_mouse_over(mouse_pos):
                    pygame.quit()
            if event.type == pygame.MOUSEMOTION:
                if self.play_button.is_mouse_over(mouse_pos):
                    self.play_button.text.color = constants.TEXT_MOUSE_OVER_GREEN
                elif self.options_button.is_mouse_over(mouse_pos):
                    self.options_button.text.color = constants.TEXT_MOUSE_OVER_GREEN
                elif self.exit_button.is_mouse_over(mouse_pos):
                    self.exit_button.text.color = constants.TEXT_MOUSE_OVER_GREEN
                else:
                    self.play_button.text.color = constants.BLACK
                    self.options_button.text.color = constants.BLACK
                    self.exit_button.text.color = constants.BLACK


class GameScene(Scene):
    def __init__(self):
        super().__init__()
        self.board = Board()
        self.dragging = False
        self.piece_clicked_pos = None
        self.player_color = constants.WHITE_PIECE
        self.mouse_pos = pygame.mouse.get_pos()

    def render(self, screen):
        screen.fill(constants.WHITE)
        self.board.draw_board()
        self.board.set_piece_images()

    def update(self):
        if self.dragging:
            self.drag_piece()

    def handle_events(self, events):
        for event in events:
            self.mouse_pos = pygame.mouse.get_pos()

            if event.type == pygame.MOUSEBUTTONDOWN:
                self.piece_clicked_pos = self.get_piece_clicked(
                    self.mouse_pos)
                if self.piece_clicked_pos:
                    self.dragging = True
                    self.board.set_dragged_piece(self.piece_clicked_pos)

            elif event.type == pygame.MOUSEBUTTONUP:
                if self.dragging:
                    self.dragging = False
                    # if valid move
                    dropped_square = self.board.get_dropped_square(
                        self.mouse_pos)
                    if dropped_square:  # and valid move:
                        self.board.set_moved_piece(dropped_square)
                    else:
                        self.board.set_moved_piece(self.piece_clicked_pos)
                    self.piece_clicked_pos = None

    def drag_piece(self):
        self.board._dragged_piece.update_rect_center(self.mouse_pos)

    def get_piece_clicked(self, mouse_pos):
        for i in range(8):
            for j in range(8):
                if self.board.grid[i][j].piece is not None and self.board.grid[i][j].rect.collidepoint(mouse_pos):
                    return (i, j)

        return False
