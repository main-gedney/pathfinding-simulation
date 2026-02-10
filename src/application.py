import pygame
from sys import exit

from .config import *
from .grid import generate_grid
from .renderer import Renderer


class Application:
    def __init__(self) -> None:
        print('Creating new application')

        pygame.init()

        self.screen = pygame.display.set_mode(SCREEN_SIZE)
        self.clock = pygame.time.Clock()

        self.grid = generate_grid()
        self.renderer = Renderer(self.grid)

    @staticmethod
    def _quit() -> None:
        pygame.quit()
        exit()

    def _handle_events(self) -> None:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self._quit()

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self._quit()
                elif event.key == pygame.K_g:
                    self.grid = generate_grid()
                    self.renderer.update_walls(self.grid)

    def run(self) -> None:
        print('Running application')

        while True:
            self._handle_events()

            self.renderer.render()

            pygame.display.flip()
            self.clock.tick(FRAME_RATE)
