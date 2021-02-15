import pygame
from pygame import display, event
from pygame.locals import *


SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 500


def render():
    pygame.init()

    screen = display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])

    active = True

    while active:

        for ev in event.get():
            if ev.type == KEYDOWN and ev.key == K_ESCAPE:
                active = False
            elif ev.type == QUIT:
                active = False

        screen.fill((255, 255, 255))
        surface = pygame.Surface((50, 50))

        surface.fill((0, 0, 0))
        rect = surface.get_rect()

        surf_center = ((SCREEN_WIDTH - surface.get_width()) / 2, (SCREEN_HEIGHT - surface.get_height()) / 2)
        screen.blit(surface, surf_center)

        pygame.display.flip()

    pygame.quit()


if __name__ == '__main__':
    render()
