from .nodes import Node
from .uninformed import Agent
from ..config import *


class BestFirst(Agent):
    def __init__(self, grid: list[list[int]]) -> None:
        super().__init__(grid, 'Greedy Best-First')

    @staticmethod
    def _create_node(x: int, y: int, parent: Node) -> None:
        cost = abs((TILES_WIDTH - 1) - x) + abs((TILES_HEIGHT - 1) - y)

        return Node(x, y, parent, cost)

    def _remove(self) -> Node:
        best = 0

        for index in range(1,len( self.frontier)):
            if self.frontier[index].cost < self.frontier[best].cost:
                best = index

        return self.frontier.pop(best)


class AStar(Agent):
    def __init__(self, grid: list[list[int]]) -> None:
        super().__init__(grid, 'A-Star')

    @staticmethod
    def _create_node(x: int, y: int, parent: Node) -> None:
        cost = abs((TILES_WIDTH - 1) - x) + abs((TILES_HEIGHT - 1) - y) + parent.distance

        return Node(x, y, parent, cost)

    def _remove(self) -> Node:
        best = 0

        for index in range(1,len( self.frontier)):
            if self.frontier[index].cost < self.frontier[best].cost:
                best = index

        return self.frontier.pop(best)