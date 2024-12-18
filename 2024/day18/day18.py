from shared.types import Result
from shared.input import get_input
from shared.grid import Grid, get_adj4

INPUT_DATA = "day18/input.txt"
SAMPLE_DATA = "day18/sample.txt"

REAL_INPUT = True
REAL_SIZE = 71
SAMPLE_SIZE = 7
SIZE = REAL_SIZE if REAL_INPUT else SAMPLE_SIZE

Point = tuple[int, int]


def get_simulated_grid(input: list[str], count: int) -> Grid:
    grid = Grid(lambda: '.', [])
    for i in range(count):
        line = input[i]
        x, y = tuple(line.split(','))
        grid[int(x), int(y)] = '#'
    return grid


def bfs_grid(grid: Grid, start: Point, end: Point) -> int:
    visited = set([start])
    needs_eval = [(start, 0)]

    while len(needs_eval) > 0:
        pos, count = needs_eval.pop(0)
        if pos == end:
            return count

        for neighbor in get_adj4(pos[0], pos[1]):
            if neighbor in visited or min(neighbor) < 0 or max(neighbor) >= SIZE or grid[neighbor] == '#':
                continue
            visited.add(neighbor)
            needs_eval.append((neighbor, count + 1))
    return -1


def find_first_bad_byte(input: list[str]) -> str:
    lower = 0
    upper = len(input)
    while upper - lower > 1:
        i = (upper + lower) // 2
        grid = get_simulated_grid(input, i)
        res = bfs_grid(grid, (0, 0), (SIZE - 1, SIZE - 1))
        if res == -1:
            upper = i
        else:
            lower = i
    return input[lower]


def day18() -> Result:
    res = Result()
    input = get_input(INPUT_DATA if REAL_INPUT else SAMPLE_DATA)
    grid = get_simulated_grid(input, 1024 if REAL_INPUT else 12)
    res.p1 = bfs_grid(grid, (0, 0), (SIZE - 1, SIZE - 1))
    res.p2 = find_first_bad_byte(input)

    return res


if __name__ == '__main__':
    result = day18()
    print(f'Day 18 Part 1: {result.p1}')
    print(f'Day 18 Part 2: {result.p2}')
