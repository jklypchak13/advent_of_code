from shared.grid import Grid
from shared.types import Result
from shared.input import get_input_grid

INPUT_DATA = "day4/input.txt"
SAMPLE_DATA = "day4/sample.txt"


def get_letters_in_direction(grid: Grid, x: int, y: int, dx: int, dy: int, cnt: int) -> str:
    word = ''
    for _ in range(cnt):
        x += dx
        y += dy
        word += grid[x, y]
    return word


def cnt_xmas(grid: Grid, x: int, y: int) -> int:
    assert grid[x, y] == 'X'
    count = 0
    for dx in range(-1, 2):
        for dy in range(-1, 2):
            word = get_letters_in_direction(grid, x, y, dx, dy, 3)
            if word == 'MAS':
                count += 1
    return count


def total_xmas(grid: Grid) -> int:
    total = 0
    for (x, y) in grid:
        if grid[x, y] != 'X':
            continue
        total += cnt_xmas(grid, x, y)
    return total


def is_mas(w1: str, w2: str) -> bool:
    return (w1 == 'S' and w2 == 'M') or (w1 == 'M' and w2 == 'S')


def is_x_mas(grid: Grid, x: int, y: int) -> bool:
    assert grid[x, y] == 'A'
    top_left = get_letters_in_direction(grid, x, y, -1, -1, 1)
    bot_right = get_letters_in_direction(grid, x, y, 1, 1, 1)

    bot_left = get_letters_in_direction(grid, x, y, 1, -1, 1)
    top_right = get_letters_in_direction(grid, x, y, -1, 1, 1)

    return is_mas(top_left, bot_right) and is_mas(bot_left, top_right)


def cnt_x_mas(grid: Grid) -> int:
    total = 0
    for x, y in grid:
        if grid[x, y] != 'A':
            continue
        total += 1 if is_x_mas(grid, x, y) else 0
    return total


def day4() -> Result:
    res = Result()
    input = get_input_grid(INPUT_DATA)
    res.p1 = total_xmas(input)
    res.p2 = cnt_x_mas(input)
    return res


if __name__ == '__main__':
    result = day4()
    print(f'Day 4 Part 1: {result.p1}')
    print(f'Day 4 Part 2: {result.p2}')
