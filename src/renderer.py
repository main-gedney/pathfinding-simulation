import pygame

from .config import *

class Renderer:
    def __init__(self, grid: list[list[int]]) -> None:
        self.grid = grid
        self.screen = pygame.display.get_surface()

        print(self.grid)

        self.walls = None

    @staticmethod
    def _draw_rect(x: int, y: int, color: tuple[int, int, int], surface: pygame.surface.Surface) -> None:
        pygame.draw.rect(surface, color, (x, y, TILE_SIZE, TILE_SIZE))

    def _render_walls(self) -> None:
        self.walls = pygame.surface.Surface(SCREEN_SIZE)

        for y in range(TILES_HEIGHT):
            for x in range(TILES_WIDTH):
                if self.grid[y][x] == '#':
                    self._draw_rect(x * TILE_SIZE, y * TILE_SIZE, (255, 255, 255), self.walls)

    def render(self) -> None:
        surface = pygame.surface.Surface(SCREEN_SIZE)
        surface.fill((0, 0, 0))

        if self.walls is None:
            self._render_walls()
        surface.blit(self.walls, (0, 0))

        self.screen.blit(surface, (0, 0))
