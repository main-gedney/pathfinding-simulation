SCREEN_SIZE = (640, 640)
FRAME_RATE = 10

TILE_SIZE = 16

WALL_COLOR = (255, 255, 255)
PATH_COLOR = (0, 0, 255)  # Also used for goal Square
DIRECTIONS = [(-1, 0), (1, 0), (0, -1), (0, 1)]

GRID_TILE_CHANCE = 30  # Percentage change of tiles being placed


TILES_WIDTH = SCREEN_SIZE[0] // TILE_SIZE
TILES_HEIGHT = SCREEN_SIZE[1] // TILE_SIZE