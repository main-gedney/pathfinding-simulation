from .nodes import Node
from ..config import TILES_WIDTH, TILES_HEIGHT, DIRECTIONS


class Agent:
    def __init__(self, grid: list[list[int]]) -> None:
        self.grid = grid

        self.frontier = [Node(1, 1)]
        self.explored = []
        self.path = []

        self.path_found = False
        self.finished = False

    @staticmethod
    def _goal_test(node: Node) -> bool:
        return node.x == (TILES_WIDTH - 2) and node.y == (TILES_HEIGHT - 2)

    def _get_path(self, node: Node) -> None:
        self.path_found = True

        while node:
            self.path.append(node)
            node = node.parent

    def _get_neighbors(self, node: Node) -> list[Node]:
        x, y = node.x, node.y
        nodes = []

        for dx, dy in DIRECTIONS:
            nx, ny = (x + dx), (y + dy)
            if 0 <= nx < TILES_WIDTH and 0 <= ny < TILES_HEIGHT:
                if self.grid[ny][nx] == ' ':
                    nodes.append(Node(nx, ny, node))

        return nodes

    def _remove(self) -> Node:
        raise NotImplementedError

    def step(self) -> bool:
        if self.finished:
            return True
        if not self.frontier:
            self.finished = True
            return True

        node = self._remove()
        if self._goal_test(node):
            self._get_path(node)
            self.finished = True
            return True

        self.explored.append(node)

        for child in self._get_neighbors(node):
            if child not in self.explored and child not in self.frontier:
                self.frontier.append(child)

        return False

