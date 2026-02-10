from random import randint

from .config import *


def generate_grid() -> list[list[int]]:
    grid = []
    for _ in range(TILES_HEIGHT):
        row = []
        for _ in range(TILES_WIDTH):
            index = randint(0, 100)

            if index <= GRID_TILE_CHANCE:
                row.append('#')
            else:
                row.append(' ')
        grid.append(row)

    for y in range(0, 3):
        for x in range(0, 3):
            grid[y][x] = ' '
    for y in range(1, 4):
        for x in range(1, 4):
            grid[TILES_HEIGHT - y][TILES_WIDTH - x] = ' '

    grid[TILES_HEIGHT - 2][TILES_WIDTH - 2] = 'x'

    return grid