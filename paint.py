import pygame


class Pixel:

    all_pixels = []

    def __init__(self, surface, colour, x_pos, y_pos, x_size=1, y_size=1):

        self.surface = surface

        self.colour = colour

        self.x_pos = x_pos
        self.y_pos = y_pos

        self.x_size = x_size
        self.y_size = y_size

        self.rect = pygame.rect.Rect(self.x_pos, self.y_pos, self.x_size, self.y_size)

        Pixel.all_pixels.append(self)

    def change_colour(self, new_colour):
        self.colour = new_colour

    def change_pos(self, new_x_pos, new_y_pos):
        self.x_pos = new_x_pos
        self.y_pos = new_y_pos

        self.rect = pygame.rect.Rect(self.x_pos, self.y_pos, self.x_size, self.y_size)

    def change_sizeI(self, new_x_size, new_y_size):
        self.x_size = new_x_size
        self.y_size = new_y_size

        self.rect = pygame.rect.Rect(self.x_pos, self.y_pos, self.x_size, self.y_size)

    def draw(self):
        pygame.draw.rect(self.surface, self.colour, self.rect)

    @classmethod
    def draw_all(cls):
        for pixel in cls.all_pixels:
            pixel.draw()

    @classmethod
    def scan_paint(cls, mouse_pos, colour):
        for pixel in cls.all_pixels:
            if not pixel.x_pos+pixel.x_size > mouse_pos[0] >= pixel.x_pos:
                continue

            if pixel.y_pos+pixel.y_size > mouse_pos[1] >= pixel.y_pos:
                pixel.change_colour(colour)
                break
