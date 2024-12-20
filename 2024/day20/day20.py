from shared.types import Result
from shared.input import get_input_grid
from shared.grid import Grid, get_adj4

INPUT_DATA = "day20/input.txt"
SAMPLE_DATA = "day20/sample.txt"


def run_race(grid: Grid) -> Grid:
    result = Grid(lambda: -1, [])
    start_pos = (0, 0)
    for pos, value in grid.items():
        if value == 'S':
            start_pos = pos
    time = 0
    pos = start_pos
    while grid[pos] != 'E':
        grid[pos] = time
        result[pos] = time
        for neighbor in get_adj4(*pos):
            if neighbor in grid and grid[neighbor] == '.' or grid[neighbor] == 'E':
                pos = neighbor
        time += 1
    grid[pos] = time
    result[pos] = time
    return result, time


def get_distance(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])


def count_valid_cheats(path, max_distance, minimum_savings) -> int:
    count = 0

    for i in range(len(path)):
        for j in range(i + 1 + minimum_savings, len(path)):
            start, end, dist = (i, j, get_distance(path[i], path[j]))
            time_saved = end - start - dist

            if dist <= max_distance and time_saved >= minimum_savings:
                count += 1
    return count


def day20() -> Result:
    res = Result()
    grid = get_input_grid(INPUT_DATA)
    times, fair_time = run_race(grid)
    path = [0] * (fair_time + 1)
    for pos, time in times.items():
        path[time] = pos

    res.p1 = count_valid_cheats(path, 2, 100)
    res.p2 = count_valid_cheats(path, 20, 100)

    return res


if __name__ == '__main__':
    result = day20()
    print(f'Day 20 Part 1: {result.p1}')
    print(f'Day 20 Part 2: {result.p2}')
