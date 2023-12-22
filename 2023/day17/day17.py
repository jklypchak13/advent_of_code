import sys
import heapq


def valid_indexes(grid, x, y):
    return 0 <= x < len(grid) and 0 <= y < len(grid[0])


def find_minimum_path(grid, min_steps, max_steps):
    needs_eval = [(grid[1][0], (1, 0), (1, 0), 0), (grid[0][1], (0, 1), (0, 1), 0)]
    visited = set()
    end = len(grid) - 1, len(grid[0]) - 1
    while needs_eval:
        heat, (x, y), (dx, dy), steps = heapq.heappop(needs_eval)
        if (x, y) == end and min_steps <= steps:
            return heat
        if ((x, y), (dx, dy), steps) in visited:
            continue
        visited.add(((x, y), (dx, dy), steps))
        if steps < (max_steps - 1) and valid_indexes(grid, x + dx, y + dy):
            s_pos = (x + dx, y + dy)
            heapq.heappush(needs_eval, (heat + grid[s_pos[0]][s_pos[1]], s_pos, (dx, dy), steps + 1))
        if min_steps <= steps:
            lx, ly, rx, ry = dy, -dx, -dy, dx
            l_pos, r_pos = (x + lx, y + ly), (x + rx, y + ry)
            for xx, yy, pos in zip((lx, rx), (ly, ry), (l_pos, r_pos)):
                if valid_indexes(grid, pos[0], pos[1]):
                    heapq.heappush(needs_eval, (heat + grid[pos[0]][pos[1]], pos, (xx, yy), 0))


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('Need arguments')
        sys.exit(-1)

    # Get Data
    lines = []
    with open(sys.argv[1], 'r') as fp:
        lines = fp.read().split('\n')

    # Convert data strings to integers
    data = []
    for line in lines:
        row = [int(value) for value in line]
        data.append(row)

    print(f'Part One Answer: {find_minimum_path(data, 0,3)}')
    print(f'Part Two Answer: {find_minimum_path(data, 3, 10)}')
