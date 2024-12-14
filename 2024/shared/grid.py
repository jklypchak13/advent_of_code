
from collections import defaultdict


def get_adj8(x: int, y: int) -> list[tuple[int, int]]:
    """returns the positions adjacent to a given x,y coordiante, counting the diagnols
    """
    result = []
    for dx in range(-1, 2):
        for dy in range(-1, 2):
            if dx == 0 and dy == 0:
                continue
            result.append((x + dx, y + dy))
    return result


def get_adj4(x: int, y: int) -> list[tuple[int, int]]:
    """returns the positions adjacent to a given x,y coordinate, excluding diagnols
    """
    result = []
    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        result.append((x + dx, y + dy))
    return result


class Grid(defaultdict):
    def __init__(self, factory):
        self.factory = factory

    def __getitem__(self, key):
        return self.get(key, self.factory())
