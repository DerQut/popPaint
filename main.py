import pygame
from pygame.locals import *

import paint
import pixels


def main():

    screen = pygame.display.set_mode((1280, 720), DOUBLEBUF)
    pygame.display.set_caption("Paint")
    paint_surface = pygame.surface.Surface((1280, 720))
    surface_cords = (0, 0)

    running = True
    clicking = False

    clock = pygame.time.Clock()

    pixels.generate_pixels(paint_surface, (255, 255, 255), 1280, 720, 10, 10)

    while running:

        screen.fill((128, 128, 128))

        mouse_pos = pygame.mouse.get_pos()

        events = pygame.event.get()
        for event in events:
            if event.type == pygame.WINDOWCLOSE:
                running = False

            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    clicking = True
            elif event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    clicking = False

        if clicking:
            paint.Pixel.scan_paint((mouse_pos[0]-surface_cords[0], mouse_pos[1]-surface_cords[1]), (0, 0, 0))

        paint_surface.fill((255, 255, 255))
        paint.Pixel.draw_all()
        screen.blit(paint_surface, surface_cords)

        pygame.display.flip()
        clock.tick(240)


if __name__ == '__main__':
    main()
