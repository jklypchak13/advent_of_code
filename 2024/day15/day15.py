from shared.types import Result
from shared.input import Grid

INPUT_DATA = "day15/input.txt"
SAMPLE_DATA = "day15/sample.txt"

DIRECTIONS = {
    '^': (-1, 0),
    'v': (1, 0),
    '>': (0, 1),
    '<': (0, -1),
}

Point = tuple[int, int]


def can_move(grid: Grid, position: Point, dx: int, dy: int) -> bool:
    if position not in grid or grid[position] == '#':
        return False

    if grid[position] == '.':
        return True

    # We are at a box
    if grid[position] not in '[]' or dy != 0:
        return can_move(grid, (position[0] + dx, position[1] + dy), dx, dy)

    other_direction = 1 if grid[position] == '[' else -1
    current_column = can_move(grid, (position[0] + dx, position[1] + dy), dx, dy)
    other_column = can_move(grid, (position[0] + dx, position[1] + dy + other_direction), dx, dy)
    return current_column and other_column


def push_boxes(grid: Grid, position: Point, dx: int, dy: int) -> Grid:
    if grid[position] == '.':
        return grid

    next = position[0] + dx, position[1] + dy
    grid = push_boxes(grid, next, dx, dy)

    if grid[position] in '[]' and dy == 0:
        # Need to push the ones next to me as well
        other_dir = 1 if grid[position] == '[' else -1
        other_half = position[0], position[1] + other_dir
        other_next = position[0] + dx, position[1] + other_dir
        push_boxes(grid, other_next, dx, dy)
        grid[other_next] = grid[other_half]
        grid[other_half] = '.'

    grid[next] = grid[position]
    grid[position] = '.'

    return grid


def follow_instructions(grid: Grid, start: Point, instructions: str) -> Grid:
    current = start
    for instruction in instructions:
        dx, dy = DIRECTIONS[instruction]
        next_position = current[0] + dx, current[1] + dy
        if can_move(grid, next_position, dx, dy):
            grid = push_boxes(grid, next_position, dx, dy)
            grid[current] = '.'
            current = current[0] + dx, current[1] + dy
            grid[current] = '@'
    return grid


def get_box_positions(grid: Grid) -> int:
    score = 0
    for key, val in grid.items():
        if val not in 'O[':
            continue
        score += key[0] * 100 + key[1]
    return score


def get_wide_grid(grid_data: str) -> Grid:
    WIDE_MAP = {
        '#': '##',
        'O': '[]',
        '.': '..',
        '@': '@.',
    }
    grid = Grid(lambda: '', [])
    grid_data = grid_data.split('\n')
    for i in range(len(grid_data)):
        for j in range(len(grid_data)):
            data = WIDE_MAP[grid_data[i][j]]
            grid[i, 2 * j] = data[0]
            grid[i, 2 * j + 1] = data[1]
    return grid


def fix_warehouse(grid, instructions):
    for pos, val in grid.items():
        if val == '@':
            initial_position = pos
    follow_instructions(grid, initial_position, instructions)
    return get_box_positions(grid)


def day15() -> Result:
    res = Result()

    data = ''
    with open(INPUT_DATA, 'r') as fp:
        data = fp.read()

    grid_data = data.split('\n\n')[0]
    instructions = ''.join(data.split('\n\n')[1].split('\n'))
    normal_grid = Grid(lambda: '', grid_data.split('\n'))
    wide_grid = get_wide_grid(grid_data)

    res.p1 = fix_warehouse(normal_grid, instructions)
    res.p2 = fix_warehouse(wide_grid, instructions)

    return res


if __name__ == '__main__':
    result = day15()
    print(f'Day 15 Part 1: {result.p1}')
    print(f'Day 15 Part 2: {result.p2}')
