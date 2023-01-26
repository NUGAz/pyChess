from ui_elements import Text
from math import floor
import constants
import pygame


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
        super(TitleScreen, self).__init__()
        self.py_text = Text(constants.TITLE_PY,
                            floor(pygame.display.Info().current_w * 0.05))
        self.title_text = Text(constants.TITLE_CHESS,
                               floor(pygame.display.Info().current_w * 0.20))
        self.start_text = Text(constants.TITLE_START_SPACE,
                               floor(pygame.display.Info().current_w * 0.05))
        self.start_text_blinking = 1
        self.start_sound = pygame.mixer.Sound("assets/sounds/start_sound.wav")

    def render(self, screen):
        screen.fill(constants.WHITE)

        window_x = pygame.display.Info().current_w
        window_y = pygame.display.Info().current_h

        center_x = window_x/2

        screen.blit(self.py_text.image, ((center_x - (self.title_text.rect.centerx + self.py_text.rect.right * 0.70)), window_y * 0.20))
        screen.blit(self.title_text.image,
                    ((center_x - self.title_text.rect.centerx), window_y * 0.20))
        screen.blit(self.start_text.image,
                    ((center_x - self.start_text.rect.centerx), window_y * 0.80))

    def update(self):
        current_w = pygame.display.Info().current_w
        self.py_text.update(floor(current_w * 0.05))
        self.title_text.update(floor(current_w * 0.20))

        self.calculate_blinking_animation(self.start_text.color)
        self.start_text.color = tuple(rgb + self.start_text_blinking for rgb in self.start_text.color)
        self.start_text.update(floor(current_w * 0.05))
    
    def calculate_blinking_animation(self, color_value_tuple):
        if(color_value_tuple == constants.WHITE):
            self.start_text_blinking = -3
        elif(color_value_tuple == constants.BLACK):
            self.start_text_blinking = 3


    def handle_events(self, events):
        for event in events:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                pygame.mixer.Sound.play(self.start_sound)
                pygame.time.delay(1000)
                self.manager.go_to(MainMenuScreen())
            


class MainMenuScreen(Scene):
    def __init__(self):
        super(MainMenuScreen, self).__init__()
        self.py_text = Text(constants.TITLE_PY,
                            floor(pygame.display.Info().current_w * 0.05))

    def render(self, screen):
        screen.fill(constants.WHITE)

        window_x = pygame.display.Info().current_w

        screen.blit(self.py_text.image, (window_x * 0.19, window_x * 0.13))

    def update(self):
        pass

    def handle_events(self, events):
        for event in events:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_BACKSPACE:
                self.manager.go_to(TitleScreen())
                
 
