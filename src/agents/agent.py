from .nodes import Node
from ..config import TILES_WIDTH, TILES_HEIGHT, DIRECTIONS


class Agent:
    def __init__(self, grid: list[list[int]], name: str) -> None:
        self.grid = grid

        self.frontier = [Node(1, 1)]
        self.explored = []
        self.path = []

        self.finished = False
        self.path_found = False
        self.path_length = -1

        self.steps = 0
        self.name = name

    @staticmethod
    def _goal_test(node: Node) -> bool:
        return node.x == (TILES_WIDTH - 2) and node.y == (TILES_HEIGHT - 2)

    def _get_path(self, node: Node) -> None:
        self.path_found = True
        print('Path found')

        while node:
            self.path.append(node)
            self.path_length += 1
            node = node.parent

    @staticmethod
    def _create_node(x: int, y: int, parent: Node) -> Node:
        return Node(x, y, parent)

    def _get_neighbors(self, node: Node) -> list[Node]:
        x, y = node.x, node.y
        nodes = []

        for dx, dy in DIRECTIONS:
            nx, ny = (x + dx), (y + dy)
            if 0 <= nx < TILES_WIDTH and 0 <= ny < TILES_HEIGHT:
                if self.grid[ny][nx] == ' ':
                    nodes.append(self._create_node(nx, ny, node))

        return nodes

    def _remove(self) -> Node:
        raise NotImplementedError

    def step(self) -> bool:
        if self.finished:
            return True
        if not self.frontier:
            print('No solution found')

            self.finished = True
            return True

        self.steps += 1

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

