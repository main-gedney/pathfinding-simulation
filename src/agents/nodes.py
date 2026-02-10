class Node:
    def __init__(self, x: int, y: int, parent: 'Node' = None, cost: int = 0) -> None:
        self.x = x
        self.y = y
        self.parent = parent
        self.cost = cost

    def __str__(self) -> str:
        return f'({self.x}, {self.y})'