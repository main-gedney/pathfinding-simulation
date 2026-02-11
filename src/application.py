import pygame
from sys import exit

from .agents import *
from .config import *
from .grid import generate_grid
from .renderer import Renderer

agents = [DepthFirst, BreadthFirst]


class Application:
    def __init__(self) -> None:
        print('Creating new application')

        pygame.init()

        self.screen = pygame.display.set_mode(SCREEN_SIZE)
        self.clock = pygame.time.Clock()

        self.grid = generate_grid()
        self.renderer = Renderer(self.grid)

        self.agent_index = 0
        self.agent = agents[self.agent_index](self.grid)

        self.running = False

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

                elif event.key == pygame.K_SPACE:
                    self.running = not self.running
                elif event.key == pygame.K_RETURN:
                    self.agent.step()

                elif event.key == pygame.K_LEFT:
                    self.agent_index -= 1
                    if self.agent_index < 0:
                        self.agent_index = len(agents) - 1
                    self.agent = agents[self.agent_index](self.grid)
                elif event.key == pygame.K_RIGHT:
                    self.agent_index += 1
                    if self.agent_index == len(agents) :
                        self.agent_index = 0
                    self.agent = agents[self.agent_index](self.grid)

                elif event.key == pygame.K_g:
                    if not self.running:
                        self.grid = generate_grid()
                        self.renderer.update_walls(self.grid)
                        self.agent = agents[self.agent_index](self.grid)
                elif event.key == pygame.K_r:
                    self.running = False
                    self.agent = agents[self.agent_index](self.grid)

    def run(self) -> None:
        print('Running application')

        while True:
            self._handle_events()

            if not self.agent.finished and self.running:
                self.agent.step()

            self.renderer.render(self.agent)

            pygame.display.flip()
            self.clock.tick(FRAME_RATE)
