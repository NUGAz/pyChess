from pygame import display, transform


class Piece():
    def __init__(self, color, image):
        self.color = color
        self._image = image
        self.resized_image = self._image
        self._rect = self._image.get_rect()

    def set_image(self):
        self.resized_image = transform.smoothscale(
            self._image, (self._rect.w, self._rect.h))
        display.get_surface().blit(self.resized_image, self._rect)

    @property
    def image(self):
        return self._image

    @property
    def rect(self):
        return self._rect

    @rect.setter
    def rect(self, new_rect):
        self._rect = new_rect

    def update_rect_center(self, new_center):
        self._rect.center = new_center

    def move(self):
        raise NotImplementedError
