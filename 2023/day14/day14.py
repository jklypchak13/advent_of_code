import sys

TARGET_CYCLE = 1000000000


def shift_data(line):
    for i in reversed(range(0, len(lines))):
        if line[i] == 'O':
            # Find next open .
            open_spot = i
            current = i
            while current >= 0 and line[current] != '#':
                if line[current] == '.':
                    open_spot = current
                current -= 1
            if open_spot != i:
                line[open_spot] = 'O'
                line[i] = '.'
    return line


def read_column(lines, column):
    res = []
    for i in range(len(lines)):
        res.append(lines[i][column])
    return res


def write_column(lines, data, column):
    for i in range(len(lines)):
        lines[i][column] = data[i]


def read_row(lines, row):
    res = []
    for i in range(len(lines[0])):
        res.append(lines[row][i])
    return res


def write_row(lines, data, row):
    for j in range(len(lines[0])):
        lines[row][j] = data[j]


def shift(lines, read_fn, write_fn, reverse=False):
    for i in range(len(lines)):
        data = read_fn(lines, i)
        if reverse:
            data.reverse()
        data = shift_data(data)
        if reverse:
            data.reverse()
        write_fn(lines, data, i)


def score_grid(lines):
    total = 0
    for i, line in enumerate(lines):
        # Count the O's
        total += (len(lines) - i) * line.count('O')
    return total


def do_cycle(lines):
    shift(lines, read_column, write_column)
    shift(lines, read_row, write_row)
    shift(lines, read_column, write_column, reverse=True)
    shift(lines, read_row, write_row, reverse=True)


def get_grid_string(lines):
    res = ''
    for line in lines:
        for c in line:
            res += c
        res += '\n'
    return res[:-1]


def part_one(grid):
    shift(grid, read_column, write_column)
    return score_grid(grid)


def part_two(grid):
    seen_positions = {get_grid_string(grid): 0}
    cycle_count = 0
    for i in range(1, TARGET_CYCLE):
        cycle_count += 1
        do_cycle(grid)
        grid_string = get_grid_string(grid)
        if grid_string in seen_positions:
            break
        else:
            seen_positions[grid_string] = i - 1
    starting_index = seen_positions[get_grid_string(data)] - 1
    cycle_length = cycle_count - starting_index

    for position, cycle_num in seen_positions.items():
        if cycle_num - starting_index == ((TARGET_CYCLE - cycle_count + 1) % cycle_length):
            grid = []
            for line in position.split('\n'):
                grid.append(list(line))
            return score_grid(grid)


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('Need arguments')
        sys.exit(-1)

    # Get Data
    lines = []
    with open(sys.argv[1], 'r') as fp:
        lines = fp.read().split('\n')
    data = []
    for line in lines:
        data.append(list(line))

    part_one_grid = data.copy()
    print(f'Part One Answer: {part_one(part_one_grid)}')
    print(f'Part Two Answer: {part_two(data)}')
