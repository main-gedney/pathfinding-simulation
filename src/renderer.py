import pygame

from .agents import Agent
from .config import *

class Renderer:
    def __init__(self, grid: list[list[int]]) -> None:
        self.screen = pygame.display.get_surface()

        self.walls = None
        self.update_walls(grid)

    @staticmethod
    def _draw_rect(x: int, y: int, color: tuple[int, int, int], surface: pygame.surface.Surface) -> None:
        pygame.draw.rect(surface, color, (x, y, TILE_SIZE, TILE_SIZE))

    def _render_agent(self, surface: pygame.surface.Surface, agent: Agent) -> None:
        for node in agent.frontier:
            self._draw_rect((node.x * TILE_SIZE), (node.y * TILE_SIZE), FRONTIER_COLOR, surface)
        for node in agent.explored:
            self._draw_rect((node.x * TILE_SIZE), (node.y * TILE_SIZE), EXPLORED_COLOR, surface)
        for node in agent.path:
            self._draw_rect((node.x * TILE_SIZE), (node.y * TILE_SIZE), PATH_COLOR, surface)

    def update_walls(self, grid: list[list[int]]) -> None:
        self.walls = pygame.surface.Surface(SCREEN_SIZE)

        for y in range(TILES_HEIGHT):
            for x in range(TILES_WIDTH):
                if grid[y][x] == '#':
                    self._draw_rect(x * TILE_SIZE, y * TILE_SIZE, WALL_COLOR, self.walls)

    def render(self, agent: Agent) -> None:
        surface = pygame.surface.Surface(SCREEN_SIZE)

        surface.blit(self.walls, (0, 0))
        self._render_agent(surface,  agent)
        self._draw_rect(((TILES_WIDTH - 2) * TILE_SIZE), ((TILES_HEIGHT - 2) * TILE_SIZE), PATH_COLOR, self.walls)

        self.screen.blit(surface, (0, 0))
