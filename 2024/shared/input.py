
from shared.grid import Grid


def get_input(path: str) -> list[str]:
    lines = []
    with open(path, 'r') as fp:
        lines = fp.read().split('\n')
    return lines


def get_input_grid(path: str, default_value: str = '') -> Grid:
    lines = get_input(path)
    grid = Grid(lambda: default_value, lines)
    return grid
