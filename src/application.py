import pygame
from sys import exit

from .agents import *
from .config import *
from .grid import generate_grid, generate_empty_grid
from .renderer import Renderer

agents = [DepthFirst, BreadthFirst, BestFirst, AStar]


class Application:
    def __init__(self) -> None:
        print('Creating new application')

        pygame.init()

        self.screen = pygame.display.set_mode(SCREEN_SIZE)
        pygame.display.set_caption('Pathfinding Simulation')
        pygame.display.set_icon(pygame.image.load('media/icon.png'))
        self.clock = pygame.time.Clock()

        self.grid = generate_grid()
        self.renderer = Renderer(self.grid)

        self.agent_index = 0
        self.agent = agents[self.agent_index](self.grid)

        self.mouse_down = []
        self.running = False

    @staticmethod
    def _quit() -> None:
        pygame.quit()
        exit()

    def _handle_events(self) -> None:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self._quit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    self.mouse_down.append(1)
                elif event.button == 3:
                    self.mouse_down.append(3)
            elif event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    self.mouse_down.remove(1)
                elif event.button == 3:
                    self.mouse_down.remove(3)

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self._quit()

                elif event.key == pygame.K_SPACE:
                    self.running = not self.running
                elif event.key == pygame.K_RETURN:
                    self.agent.step()

                elif event.key == pygame.K_LEFT:
                    self.agent_index -= 1
                    if self.agent_index < 0:
                        self.agent_index = len(agents) - 1
                    self.agent = agents[self.agent_index](self.grid)
                    self.running = False
                elif event.key == pygame.K_RIGHT:
                    self.agent_index += 1
                    if self.agent_index == len(agents) :
                        self.agent_index = 0
                    self.agent = agents[self.agent_index](self.grid)
                    self.running = False

                elif event.key == pygame.K_g:
                    if not self.running:
                        self.grid = generate_grid()
                        self.renderer.update_walls(self.grid)
                        self.agent = agents[self.agent_index](self.grid)
                elif event.key == pygame.K_c:
                    if not self.running:
                        self.grid = generate_empty_grid()
                        self.renderer.update_walls(self.grid)
                        self.agent = agents[self.agent_index](self.grid)
                elif event.key == pygame.K_r:
                    self.running = False
                    self.agent = agents[self.agent_index](self.grid)

    def _draw_tiles(self) -> None:
        mouse_pos = pygame.mouse.get_pos()
        x, y = ((mouse_pos[0] // TILE_SIZE), ((mouse_pos[1] - HEADER_SIZE) // TILE_SIZE))

        if 0 <= y < TILES_HEIGHT and 0 <= x < TILES_WIDTH:
            if self.grid[y][x] == ' ' and self.mouse_down[0] == 1:
                self.grid[y][x] = '#'
            if self.grid[y][x] == '#' and self.mouse_down[0] == 3:
                self.grid[y][x] = ' '

        self.renderer.update_walls(self.grid)

    def run(self) -> None:
        print('Running application')

        while True:
            self._handle_events()

            if not self.agent.finished and self.running:
                self.agent.step()

            if  self.mouse_down and not self.running:
                self._draw_tiles()

            self.renderer.render(self.agent)

            pygame.display.flip()
            self.clock.tick(FRAME_RATE)
