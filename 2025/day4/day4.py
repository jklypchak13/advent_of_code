from aoc_utils.types import Result
from aoc_utils.input import get_input_grid, Grid
from aoc_utils.grid import get_adj8

from copy import deepcopy

INPUT_DATA = "day4/input.txt"
SAMPLE_DATA = "day4/sample.txt"

BOX = '@'

def count_boxes(neighbors):
    total = 0
    for value in neighbors:
        if value == BOX:
            total += 1
    return total

# Remove the removeable boxes, return the number removed
def remove_boxes(grid:Grid)->int:
    MAX_NEIGHBORS = 3
    removed = set()
    for x, y in grid.keys():
        neighbors = [grid[i,j] for i,j in get_adj8(x,y)]
        neighbor_boxes = count_boxes(neighbors)
        if neighbor_boxes <= MAX_NEIGHBORS:
            removed.add((x,y))

    # Do the removals
    for val in removed:
        grid.pop(val)

    return len(removed)

def clean_grid(grid:Grid):
    # Remove non-boxes, since we only actually care about where those are
    remove = set()
    for x,y in grid.keys():
        if grid[x,y] != BOX:
            remove.add((x,y))
    for value in remove:
        grid.pop(value)


def day4() -> Result:
    res = Result()
    grid = get_input_grid(INPUT_DATA)
    clean_grid((grid))

    # Part 1
    res.p1 = remove_boxes(grid)

    # Part 2
    res.p2 = res.p1
    removed = res.p2
    while removed > 0:
        removed = remove_boxes(grid)
        res.p2 += removed

    return res


if __name__ == '__main__':
    result = day4()
    print(f'Day 4 Part 1: {result.p1}')
    print(f'Day 4 Part 2: {result.p2}')
