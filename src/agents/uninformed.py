from .nodes import Node
from ..config import TILES_WIDTH, TILES_HEIGHT


class Agent:
    def __init__(self, grid: list[list[int]]) -> None:
        self.explored = [Node(1, 1)]
        self.frontier = [
            Node(0, 1, self.explored[0]),
            Node(2, 1, self.explored[0]),
            Node(1, 0, self.explored[0]),
            Node(1, 2, self.explored[0])
        ]

        self.grid = grid
        self.grid[1][1] = 'e'
        self.grid[0][1] = 'f'
        self.grid[2][1] = 'f'
        self.grid[1][0] = 'f'
        self.grid[1][2] = 'f'

        self.path_found = False

    @staticmethod
    def _goal_test(node: Node) -> bool:
        if node.y == TILES_HEIGHT - 2:
            print(node)

        return node.x == TILES_WIDTH - 2 and node.y == TILES_HEIGHT - 2

    def _find_path(self, node: Node) -> None:
        self.path_found = True
        print('Goal reached')

        cur_node = node
        while cur_node.parent is not None:
            cur_node = cur_node.parent
            self.grid[cur_node.y][cur_node.x] = 'p'
        self.grid[TILES_HEIGHT - 2][TILES_WIDTH - 2] = 'p'

    def _update_frontier(self, current: Node) -> None:
        x, y = current.x, current.y

        new_nodes = []
        if x != 0 and self.grid[y][x - 1] == ' ':
            self.grid[y][x - 1] = 'f'
            new_nodes.append(Node(x - 1, y, current))
        if (x + 1) != TILES_WIDTH and self.grid[y][x + 1] == ' ':
            self.grid[y][x + 1] = 'f'
            new_nodes.append(Node(x + 1, y, current))
        if y != 0 and self.grid[y - 1][x] == ' ':
            self.grid[y - 1][x] = 'f'
            new_nodes.append(Node(x, y - 1, current))
        if (y + 1) != TILES_WIDTH and self.grid[y + 1][x] == ' ':
            self.grid[y + 1][x] = 'f'
            new_nodes.append(Node(x, y + 1, current))

        for item in new_nodes:
            if self._goal_test(item):
                self._find_path(item)

        self.frontier = [*self.frontier, *new_nodes]

    def update(self) -> None:
        raise NotImplementedError
