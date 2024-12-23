from shared.grid import Grid
from shared.types import Result
from shared.input import get_input_grid

INPUT_DATA = "day10/input.txt"
SAMPLE_DATA = "day10/sample.txt"
HIGH_POINT = 9
DIRECTIONS = [(-1, 0), (1, 0), (0, 1), (0, -1)]

Point = tuple[int, int]


def find_trail_heads(grid: Grid) -> list[Point]:
    head = []
    for key, value in grid.items():
        if value == '0':
            head.append(key)
    return head


def get_neighbors(grid: Grid, position: Point) -> list[Point]:
    value = int(grid[position])
    neighbors = []
    for dx, dy in DIRECTIONS:
        new_position = position[0] + dx, position[1] + dy
        new_value = int(grid[new_position])
        if new_value == value + 1:
            neighbors.append(new_position)
    return neighbors


def count_peaks(grid: Grid, root: Point) -> Result:
    res = Result()
    res.p2 = 0
    needs_eval = [root]
    visited = set()
    while len(needs_eval) > 0:
        current = needs_eval.pop(0)
        value = int(grid[current])
        if value == HIGH_POINT:
            visited.add(current)
            res.p2 += 1
        needs_eval.extend(get_neighbors(grid, current))
    res.p1 = len(visited)
    return res


def day10() -> Result:
    res = Result()
    input = get_input_grid(INPUT_DATA, '0')
    heads = find_trail_heads(input)
    res.p1, res.p2 = 0, 0
    for head in heads:
        temp = count_peaks(input, head)
        res.p1 += temp.p1
        res.p2 += temp.p2
    return res


if __name__ == '__main__':
    result = day10()
    print(f'Day 10 Part 1: {result.p1}')
    print(f'Day 10 Part 2: {result.p2}')
