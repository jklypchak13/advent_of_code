from collections import defaultdict


class Grid(defaultdict):
    def __init__(self, factory):
        self.factory = factory

    def __getitem__(self, key):
        return self.get(key, self.factory())


def get_input(path: str) -> list[str]:
    lines = []
    with open(path, 'r') as fp:
        lines = fp.read().split('\n')
    return lines


def get_input_grid(path: str, default_value: str = '') -> Grid:
    lines = get_input(path)
    grid = Grid(lambda: default_value)
    for i in range(len(lines)):
        for j in range(len(lines[i])):
            grid[i, j] = lines[i][j]
    return grid
