import sys

ITERATION_COUNT = 50


def get_neighbors(position):
    OFFSETS = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    x, y = position
    return [(x + dx, y + dy) for dx, dy in OFFSETS]


def get_possible_positions(positions, open_spaces, i):
    result = set()
    for position in positions:
        open_spaces[position] = i
        for neighbor in get_neighbors(position):
            if neighbor in open_spaces.keys() and open_spaces[neighbor] == -1:
                result.add(neighbor)
    return list(result)


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('Need arguments')
        sys.exit(-1)

    # Get Data
    lines = []
    with open(sys.argv[1], 'r') as fp:
        lines = fp.read().split('\n')

    max_x = len(lines) * 3
    max_y = len(lines) * 3
    starting_position = None
    open_spaces = {}
    for i in range(len(lines)):
        for j in range(len(lines[0])):

            if lines[i][j] != '#':
                for x in range(0, 3):
                    for y in range(0, 3):
                        open_spaces[(i + x * len(lines), j + y * len(lines))] = -1
            if lines[i][j] == 'S':
                starting_position = (i, j)

    positions = [starting_position]

    i = 0
    while (-1) in open_spaces.values():
        positions = get_possible_positions(positions, open_spaces, i)
        i += 1

    res = []
    for i in range(max_x):
        row = []
        for j in range(max_y):
            if (i, j) in open_spaces:
                row.append(f'{open_spaces[i,j] % 2}')
            else:
                row.append('#')
        res.append(row)

    print(res)
    with open('test.txt', 'w') as fp:
        for row in res:
            fp.write(''.join(row))
            fp.write('\n')
    # total = 0
    # for value in open_spaces.values():
    #     if value != 0:
    #         total += (ITERATION_COUNT // len(lines)) // (value)

    # print(total)
    # print(f'Part One Answer: {len(positions)}')
    # print(f'Part Two Answer: {0}')
