import pygame

from .agents import Agent
from .config import *

class Renderer:
    def __init__(self, grid: list[list[int]]) -> None:
        self.screen = pygame.display.get_surface()

        pygame.font.init()
        self.font = pygame.font.SysFont("monospace", 16)

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

    def _render_text(self, agent: Agent) -> None:
        text = f'Agent: {agent.name} | Steps: {agent.steps} | Path Len.: {agent.path_length}'
        text_surface = self.font.render(text, True, TEXT_COLOR)

        self.screen.blit(text_surface, (6, 3))

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

        self.screen.fill(HEADER_COLOR)
        self.screen.blit(surface, (0, HEADER_SIZE))
        self._render_text(agent)
