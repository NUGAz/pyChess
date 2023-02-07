class Piece():
    def __init__(self, color):
        self.color = color

    def set_image(self, square_rect):
        pass

    def get_image(self):
        pass

    def update_image(self, pos):
        pass

    def move(self):
        raise NotImplementedError
