import pygame
from scenes import SceneManager
import constants


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
