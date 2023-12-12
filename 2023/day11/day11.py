import sys
from typing import List


def construct_nodes(universe):
    res = []
    for i in range(len(universe)):
        for j in range(len(universe[0])):
            if universe[i][j] == '#':
                res.append((i, j))
    return res


def values_in_range(low, high, values):
    count = 0
    for value in values:
        if low < value < high:
            count += 1
    return count


def walk_path(a, b, empty_values, large_distance):
    start, end = min(a, b), max(a, b)
    return end - start + ((large_distance - 1) * values_in_range(start, end, empty_values))


def get_distance(start, end, empty_rows, empty_columns, large_distance):
    vert_distance = walk_path(start[0], end[0], empty_rows, large_distance)
    horiz_distance = walk_path(start[1], end[1], empty_columns, large_distance)
    return vert_distance + horiz_distance


def count_universe(lines, large_distance):
    # Get empty rows
    empty_rows = []
    for i, row in enumerate(lines):
        if '#' not in row:
            empty_rows.append(i)

    # Get empty columns
    empty_columns = []
    for j in range(len(lines[0])):
        empty = True
        for row in lines:
            if row[j] == '#':
                empty = False
        if empty:
            empty_columns.append(j)

    distance = 0
    galaxies = construct_nodes(lines)
    for i in range(len(galaxies)):
        for j in range(i, len(galaxies)):
            distance += get_distance(galaxies[i], galaxies[j], empty_rows, empty_columns, large_distance)
    return distance


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('Need arguments')
        sys.exit(-1)

    # Get Data
    lines = []
    with open(sys.argv[1], 'r') as fp:
        lines = fp.read().split('\n')

    print(f'Part One Answer: {count_universe(lines, 2)}')
    print(f'Part Two Answer: {count_universe(lines, 1_000_000)}')
