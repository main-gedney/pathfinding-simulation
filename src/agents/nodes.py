class Node:
    def __init__(self, x: int, y: int, parent: 'Node' = None, cost: int = 0) -> None:
        self.x = x
        self.y = y
        self.parent = parent
        self.cost = cost

        if parent:
            self.distance = parent.distance + 1
        else:
            self.distance = 0

    def __str__(self) -> str:
        return f'({self.x}, {self.y})'

    def __eq__(self, other: 'Node') -> bool:
        return self.x == other.x and self.y == other.y