from ui_elements import Text, Button
from math import floor
import utils
import constants
import pygame


class Scene():
    def __init__(self):
        self.sprite_group = pygame.sprite.Group()

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
        self.py_text = Text(constants.TITLE_PY, floor(pygame.display.Info().current_w * 0.05))
        self.title_text = Text(constants.TITLE_CHESS, floor(pygame.display.Info().current_w * 0.20))
        self.start_text = Text(constants.TITLE_START_SPACE, floor(pygame.display.Info().current_w * 0.05))

        self.sprite_group.add(self.py_text)
        self.sprite_group.add(self.title_text)
        self.sprite_group.add(self.start_text)

        self.start_text_blinking = 1
        self.start_sound = pygame.mixer.Sound(constants.SOUND_FX_PATH + constants.START_SOUND_EFFECT)

    def render(self, screen):
        screen.fill(constants.WHITE)

        """
        self.py_text.draw(screen)
        self.title_text.draw(screen)
        self.start_text.draw(screen)
        """
        self.sprite_group.draw(screen)

    def update(self):
        window_x = pygame.display.Info().current_w
        window_y = pygame.display.Info().current_h

        aspect_ratio = window_x / window_y
        center_x = window_x/2

        self.py_text.update(pos=(center_x/2.5, window_y * 0.12), font_size=floor(window_x * 0.03 * aspect_ratio))
        self.title_text.update(pos=(center_x-self.title_text.rect.width/2, window_y * 0.15), font_size=floor(window_x * 0.10 * aspect_ratio))

        self.calculate_blinking_animation(self.start_text.color)
        self.start_text.color = utils.add_to_tuple(self.start_text_blinking, self.start_text.color)
        self.start_text.update(pos=(center_x - self.start_text.rect.width/2, window_y * 0.80), font_size=floor(window_x * 0.03 * aspect_ratio))
    
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
        super().__init__()
        self.py_text = Text(0, 0, constants.TITLE_PY,
                            floor(pygame.display.Info().current_w * 0.02))
        self.title_text = Text(0, 0, constants.TITLE_CHESS,
                               floor(pygame.display.Info().current_w * 0.10))
        self.bg_image = pygame.transform.scale(pygame.image.load(constants.ICONS_PATH + constants.CHESS_BG).convert_alpha(),
                                               (pygame.display.Info().current_w,pygame.display.Info().current_w))
        self.sprite_group.add(self.py_text)
        self.sprite_group.add(self.title_text)
        
        self.play_button = Button(0, 0, 0, 0, pygame.display.get_window_size(), text=constants.PLAY_BUTTON, anchor="center")
        

    def render(self, screen):
        screen.fill(constants.WHITE)

        screen.blit(self.bg_image,(0,0))
        self.sprite_group.draw(screen)
        #self.py_text.draw(screen)
        #self.title_text.draw(screen)
    
    
    def update(self):
        window_x = pygame.display.Info().current_w
        window_y = pygame.display.Info().current_h
        center_x = window_x/2 

        self.py_text.update(center_x - (self.title_text.rect.centerx + self.py_text.rect.right * 0.70),window_y * 0.10 ,floor(window_x * 0.02))
        self.title_text.update(center_x - self.title_text.rect.centerx, window_y * 0.10, floor(window_x * 0.10))
        self.play_button.update()

    def handle_events(self, events):
        for event in events:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_BACKSPACE:
                self.manager.go_to(TitleScreen())
                
 
