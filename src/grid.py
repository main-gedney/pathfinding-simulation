from random import randint

from .config import *


def generate_grid() -> list[list[int]]:
    print('Generating new grid')

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

    return grid


def generate_empty_grid() -> list[list[int]]:
    print('Generating new empty grid')

    return [[' '] * TILES_WIDTH for _ in range(TILES_HEIGHT)]
