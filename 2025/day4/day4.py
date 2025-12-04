from aoc_utils.types import Result
from aoc_utils.input import get_input_grid, Grid
from aoc_utils.grid import get_adj8

INPUT_DATA = "day4/input.txt"
SAMPLE_DATA = "day4/sample.txt"

# Remove the removeable boxes, return the removed number removed, and the set of neighbors adjacent to removed boxes
def remove_boxes(grid:Grid, check:set)->tuple[int, set]:
    MAX_NEIGHBORS = 3
    removed = set()
    need_check = set()
    for x, y in check:
        neighbor_boxes = [pos for pos in get_adj8(x,y) if pos in grid]
        if len(neighbor_boxes) <= MAX_NEIGHBORS:
            removed.add((x,y))
            need_check.update(neighbor_boxes)

    # Do the removals
    for val in removed:
        grid.pop(val)

    return len(removed), need_check.difference(removed)


def clean_grid(grid:Grid):
    # Remove non-boxes, since we only actually care about where those are
    BOX = '@'
    keys = set(grid.keys())
    for x,y in keys:
        if grid[x,y] != BOX:
            grid.pop((x,y))

def day4() -> Result:
    res = Result()
    grid = get_input_grid(INPUT_DATA)
    clean_grid((grid))

    # Part 1
    needs_check = grid.keys()
    res.p1, needs_check = remove_boxes(grid, needs_check)

    # Part 2
    res.p2 = res.p1
    removed = res.p2
    while removed > 0:
        removed, needs_check = remove_boxes(grid, needs_check)
        res.p2 += removed

    return res


if __name__ == '__main__':
    result = day4()
    print(f'Day 4 Part 1: {result.p1}')
    print(f'Day 4 Part 2: {result.p2}')
