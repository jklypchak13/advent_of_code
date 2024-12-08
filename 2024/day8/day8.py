from shared.types import Result
from shared.input import get_input_grid, Grid

INPUT_DATA = "day8/input.txt"
SAMPLE_DATA = "day8/sample.txt"

Point = tuple[int, int]


def get_antenna_locations(grid: Grid) -> dict[str, list[Point]]:
    res: dict[str, list[Point]] = {}
    for pos, value in grid.items():
        if value.isalnum():
            if value in res:
                res[value].append(pos)
            else:
                res[value] = [pos]
    return res


def get_points_in_line(grid: Grid, p1: Point, p2: Point) -> list[Point]:
    dx = p1[0] - p2[0]
    dy = p1[1] - p2[1]
    points = set()
    # Go backwards from p1
    x, y = p1
    while (x, y) in grid:
        points.add((x, y))
        x -= dx
        y -= dy
    # Go forwards from p1
    x, y = p1
    while (x, y) in grid:
        points.add((x, y))
        x += dx
        y += dy
    return points


def get_pt_dist(p1: Point, p2: Point) -> int:
    dx = abs(p1[0] - p2[0])
    dy = abs(p1[1] - p2[1])
    return dx + dy


def is_antinode(point: Point, parent_one: Point, parent_two: Point) -> bool:
    d1 = get_pt_dist(parent_one, point)
    d2 = get_pt_dist(parent_two, point)
    return d1 == d2 * 2 or d2 == d1 * 2


def count_positions(grid: Grid, antennas: list[Point], use_harmonics: bool) -> int:
    res = set()
    pairs = [(antennas[i], antennas[j]) for i in range(len(antennas)) for j in range(i + 1, len(antennas))]
    for p1, p2 in pairs:
        points = get_points_in_line(grid, p1, p2)
        for point in points:
            if use_harmonics or is_antinode(point, p1, p2):
                res.add(point)
    return res


def count_antinodes(grid: Grid, antennas: dict[str, list[Point]], use_harmonics=False) -> int:
    antinodes = set()
    for positions in antennas.values():
        antinodes.update(count_positions(grid, positions, use_harmonics))
    return len(antinodes)


def day8() -> Result:
    res = Result()
    input = get_input_grid(INPUT_DATA)
    antenna_map = get_antenna_locations(input)
    res.p1 = count_antinodes(input, antenna_map)
    res.p2 = count_antinodes(input, antenna_map, True)
    return res


if __name__ == '__main__':
    result = day8()
    print(f'Day 8 Part 1: {result.p1}')
    print(f'Day 8 Part 2: {result.p2}')
