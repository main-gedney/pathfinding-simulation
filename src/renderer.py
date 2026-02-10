import pygame

from .config import *

class Renderer:
    def __init__(self, grid: list[list[int]]) -> None:
        self.screen = pygame.display.get_surface()

        self.walls = None
        self.update_walls(grid)

    @staticmethod
    def _draw_rect(x: int, y: int, color: tuple[int, int, int], surface: pygame.surface.Surface) -> None:
        pygame.draw.rect(surface, color, (x, y, TILE_SIZE, TILE_SIZE))

    def update_walls(self, grid: list[list[int]]) -> None:
        self.walls = pygame.surface.Surface(SCREEN_SIZE)

        for y in range(TILES_HEIGHT):
            for x in range(TILES_WIDTH):
                if grid[y][x] == '#':
                    self._draw_rect(x * TILE_SIZE, y * TILE_SIZE, WALL_COLOR, self.walls)
                elif grid[y][x] == 'x':
                    self._draw_rect(x * TILE_SIZE, y * TILE_SIZE, PATH_COLOR, self.walls)

    def render(self) -> None:
        surface = pygame.surface.Surface(SCREEN_SIZE)
        surface.fill((0, 0, 0))

        surface.blit(self.walls, (0, 0))

        self.screen.blit(surface, (0, 0))
