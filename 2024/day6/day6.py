from shared.types import Result
from shared.input import get_input_grid, Grid

INPUT_DATA = "day6/input.txt"
SAMPLE_DATA = "day6/sample.txt"


def find_start(grid: Grid) -> tuple[int, int]:
    for key, val in grid.items():
        if val == '^':
            return key
    return -1, -1


def turn(dx: int, dy: int) -> tuple[int, int]:
    if dx != 0:
        x = 0
        y = -dx
    if dy != 0:
        y = 0
        x = dy
    return x, y


def get_distinct_positions(grid: Grid) -> set[tuple[int, int]]:
    x, y = find_start(grid)
    visited = set()
    dx, dy = (-1, 0)

    while grid[x, y] != '':
        visited.add((x, y))
        next_char = grid[x + dx, y + dy]
        if next_char == '#':
            dx, dy = turn(dx, dy)
        else:
            x = x + dx
            y = y + dy
    return visited


def has_loop(grid: Grid) -> bool:
    x, y = find_start(grid)
    visited = set()
    dx = -1
    dy = 0
    while True:
        if (x, y, dx, dy) in visited:
            return True
        visited.add((x, y, dx, dy))
        next_char = grid[x + dx, y + dy]
        if next_char == '':
            break
        if next_char == '#':
            dx, dy = turn(dx, dy)
        else:
            x = x + dx
            y = y + dy
    return False


def count_possible_loops_positions(grid: Grid, visited: set[tuple[int, int]]) -> int:
    sx, sy = find_start(grid)
    count = 0
    for x, y in visited:
        if (x, y) == (sx, sy):
            continue
        temp = grid[x, y]
        grid[x, y] = '#'
        count += 1 if has_loop(grid) else 0
        grid[x, y] = temp
    return count


def day6() -> Result:
    res = Result()
    input = get_input_grid(INPUT_DATA)
    visited = get_distinct_positions(input)
    res.p1 = len(visited)
    res.p2 = count_possible_loops_positions(input, visited)

    return res


if __name__ == '__main__':
    result = day6()
    print(f'Day 6 Part 1: {result.p1}')
    print(f'Day 6 Part 2: {result.p2}')
