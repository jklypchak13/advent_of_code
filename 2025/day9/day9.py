from aoc_utils.types import Result
from aoc_utils.input import get_input
from itertools import combinations
from aoc_utils.grid import get_adj4
from collections import deque

INPUT_DATA = "day9/input.txt"
SAMPLE_DATA = "day9/sample.txt"

DEFAULT = 0
BOUNDARY = 1
OUTSIDE = 2
class Point:
    def __init__(self, x,y):
        self.x = int(x)
        self.y = int(y)

class Compressor:

    def __init__(self, x_values, y_values):
        self.x_value_map = {value: i+1 for i, value in enumerate(sorted(list(x_values)))}
        self.y_value_map = {value: i+1 for i, value in enumerate(sorted(list(y_values)))}

    def compress(self, point:Point):
        return Point(self.x_value_map[point.x], self.y_value_map[point.y])

def area(a:Point, b:Point):
    return (abs(a.x - b.x)+1) * (abs(a.y-b.y) + 1)

def calculate_areas(points:list[Point]):
    distances = []
    for x,y in combinations(points, 2):
        distances.append((area(x,y), x, y))
    return sorted(distances, key= lambda x: x[0], reverse=True)

def construct_boundary(grid:list[list], points:list[Point]):
    for i in range(len(points)):
        x,y = points[i].x, points[i].y
        next = points[(i+1)%len(points)]
        grid[y][x] = BOUNDARY
        dx =  next.x - x
        if dx != 0:
            dx = int(dx / abs(dx))
        dy =  next.y - y
        if dy != 0:
            dy = int(dy / abs(dy))
        while x != next.x or y != next.y:
            x += dx
            y += dy
            grid[y][x] = BOUNDARY


def flood_fill(grid, rows, columns):
    # Start from 0, 0. we offset everything by 1, so this is guranteed to be outside of the boundary
    needs_eval = deque([(0,0)])
    while len(needs_eval) > 0:
        x,y = needs_eval.pop()
        if grid[y][x] != DEFAULT:
            continue
        grid[y][x] = OUTSIDE
        for pos in get_adj4(x,y):
            dx, dy = pos
            if not (0<= dx < columns and 0<= dy < rows):
                continue
            if grid[dy][dx] != DEFAULT:
                continue
            needs_eval.append(pos)

def valid_rect(psum, p1, p2):
    x1 = min(p1.x, p2.x)
    y1 = min(p1.y, p2.y)
    x2 = max(p1.x, p2.x)
    y2 = max(p1.y, p2.y)

    total_zeros = (
        psum[y2+1][x2+1]
        - psum[y1][x2+1]
        - psum[y2+1][x1]
        + psum[y1][x1]
    )

    return total_zeros == 0

def compute_prefix_sum_table(grid, rows, columns):
    psum = [[0]* (columns+1) for _ in range(rows+1)]
    for i in range(rows):
        row_sum = 0
        for j in range(columns):
            row_sum += 1 if grid[i][j] == OUTSIDE else 0
            psum[i+1][j+1] = psum[i][j+1] + row_sum
    return psum

def day9() -> Result:
    res = Result()
    input_lines = get_input(INPUT_DATA)

    # Parse the input points
    x_values = [int(line.split(',')[0]) for line in input_lines]
    y_values = [int(line.split(',')[1]) for line in input_lines]
    points = [Point(x,y) for x,y in zip(x_values, y_values)]
    areas = calculate_areas(points)
    max_area, _, _ = areas[0]
    res.p1 = max_area

    # Compress the points to the smallest possible values
    unique_x_values = set(x_values)
    unique_y_values = set(y_values)
    compressor = Compressor(unique_x_values, unique_y_values)
    point_map = {(p.x, p.y): compressor.compress(p) for p in points}
    compressed_points = list(map(lambda p: point_map[p.x, p.y], points))

    # Determine our bounding box
    max_point = Point(max(unique_x_values), max(unique_y_values))
    compressed_max = compressor.compress(max_point)
    columns = compressed_max.x + 2
    rows = compressed_max.y + 2

    # Construct Grid
    grid = [[DEFAULT]* (columns) for _ in range(rows)]
    construct_boundary(grid, compressed_points)
    flood_fill(grid, rows, columns)

    psum = compute_prefix_sum_table(grid, rows, columns)
    for current_area, p1, p2 in areas:
        compressed_p1 = point_map[p1.x, p1.y]
        compressed_p2 = point_map[p2.x, p2.y]
        if valid_rect(psum, compressed_p1, compressed_p2):
            res.p2 = current_area
            break
    return res


if __name__ == '__main__':
    result = day9()
    print(f'Day 9 Part 1: {result.p1}')
    print(f'Day 9 Part 2: {result.p2}')