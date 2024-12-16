from collections import defaultdict
from shared.types import Result
from shared.input import get_input_grid
from shared.grid import Grid, get_adj4
import heapq

INPUT_DATA = "day16/input.txt"
SAMPLE_DATA = "day16/sample.txt"

Point = tuple[int, int]


def get_neighbors(position: Point, direction: Point) -> tuple[Point, Point]:
    # neighbors are either one step forward, or turned to the left and right
    x, y = position
    dx, dy = direction
    if dx == 0:
        return [((x + dx, y + dy), (dx, dy)), (position, (1, 0)), (position, (-1, 0))]
    return [((x + dx, y + dy), (dx, dy)), (position, (0, 1)), (position, (0, -1))]


def find_shortest_paths(grid: Grid, start_pos: Point) -> tuple[int, set]:
    needs_eval = []
    heapq.heappush(needs_eval, (0, (start_pos, (), (0, 1))))
    paths = set()
    distances = defaultdict(lambda: float("inf"))
    best_score = float("inf")

    while len(needs_eval) > 0:
        score, (current_pos, path, direction) = heapq.heappop(needs_eval)
        path = path + (current_pos,)

        # We have passed the best score we have found, we can stop
        if score > best_score:
            return best_score, paths

        # Record our best score, and start adding paths
        if grid[current_pos] == 'E':
            best_score = score
            paths.add(path)

        for neighbor, new_direction in get_neighbors(current_pos, direction):
            if grid[neighbor] == '#':
                continue

            # Compute the score of this new neighbor
            new_score = score
            new_score += 1000 if new_direction != direction else 1

            # Ensure we haven't seen this neighbor on a better path already
            if distances[(neighbor, new_direction)] < new_score:
                continue
            distances[(neighbor, new_direction)] = new_score
            search_state = neighbor, path, new_direction
            heapq.heappush(needs_eval, (new_score, search_state))

    return best_score, paths


def count_points(paths: set) -> int:
    points = set()
    for path in paths:
        for point in path:
            points.add(point)
    return len(points)


def day16() -> Result:
    res = Result()
    grid = get_input_grid(INPUT_DATA)

    start_pos = 0, 0
    for key in grid:
        if grid[key] == 'S':
            start_pos = key

    best_score, paths = find_shortest_paths(grid, start_pos)
    res.p1 = best_score
    res.p2 = count_points(paths)
    return res


if __name__ == '__main__':
    result = day16()
    print(f'Day 16 Part 1: {result.p1}')
    print(f'Day 16 Part 2: {result.p2}')
