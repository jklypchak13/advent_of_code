import sys

OPEN_BOTTOM = '|7F'
OPEN_TOP = '|JL'
OPEN_LEFT = '-7J'
OPEN_RIGHT = '-FL'

# These are the offsets from this character that are valid to continue the loop
STEPS = {
    '|': [(-1, 0), (1, 0)],
    '-': [(0, -1), (0, 1)],
    'L': [(-1, 0), (0, 1)],
    'J': [(-1, 0), (0, -1)],
    '7': [(1, 0), (0, -1)],
    'F': [(1, 0), (0, 1)],
}


def find_start(lines):
    for i in range(len(lines)):
        for j in range(len(lines[i])):
            if lines[i][j] == 'S':
                return i, j


def take_step(lines, current_pos, prev_pos):
    options = STEPS[lines[current_pos[0]][current_pos[1]]]
    candidates = [(current_pos[0] + step[0], current_pos[1] + step[1]) for step in options]
    if candidates[0] == prev_pos:
        return candidates[1]
    assert candidates[1] == prev_pos
    return candidates[0]


def run_loop(lines, s_row, s_col):
    # First, need to find the next step to take
    current_pos = (-1, -1)
    if s_row > 0 and lines[s_row - 1][s_col] in OPEN_BOTTOM:
        current_pos = (s_row - 1, s_col)
    elif s_row < len(lines) - 1 and lines[s_row + 1][s_col] in OPEN_TOP:
        current_pos = (s_row + 1, s_col)
    else:
        # We know there need to be to directions that connect the loop. If we are still going, let's just assume we can go right.
        current_pos = (s_row, s_col + 1)

    loop = [(s_row, s_col)]
    prev_pos = (s_row, s_col)
    while current_pos != (s_row, s_col):
        loop.append(current_pos)
        next_pos = take_step(lines, current_pos, prev_pos)
        prev_pos = current_pos
        current_pos = next_pos
    return loop


def convert_to_high_res(lines, loop):
    """converts the line array to a higher resolution map, where each character is replaced by a 3x3 grid of characters, encoding the same data
    """
    result = []
    # Set everything to a 0
    for i in range(len(lines) * 3):
        row = []
        for j in range(len(lines[0]) * 3):
            row.append('0')
        result.append(row)

    # Set all items in the loop to a wall character (X)
    for row, column in loop:
        result[row * 3 + 1][column * 3 + 1] = 'X'

        # Special Handling for starting character
        if lines[row][column] == 'S':
            offsets = [(loop[1][0] - row, loop[1][1] - column), (loop[-1][0] - row, loop[-1][1] - column)]
        else:
            offsets = STEPS[lines[row][column]]
        for offset in offsets:
            result[row * 3 + 1 + offset[0]][column * 3 + 1 + offset[1]] = 'X'
    return result


def flood_fill(high_res, pos):
    needs_eval = [pos]
    while len(needs_eval) > 0:
        x, y = needs_eval.pop()
        if x < 0 or x >= len(high_res) or y < 0 or y >= len(high_res[0]) or high_res[x][y] != '0':
            continue
        high_res[x][y] = '1'
        needs_eval.append((x - 1, y))
        needs_eval.append((x + 1, y))
        needs_eval.append((x, y - 1))
        needs_eval.append((x, y + 1))


def count_inner_nodes(lines, loop):
    high_res = convert_to_high_res(lines, loop)
    flood_fill(high_res, (0, 0))  # Note, (0, 0) will not always be correct, but we'll assume it is

    total = 0
    # Count the 0's in middle places
    for i in range(len(lines)):
        for j in range(len(lines[0])):
            if high_res[i * 3 + 1][j * 3 + 1] == '0':
                total += 1
    return total


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('Need arguments')
        sys.exit(-1)

    # Get Data
    lines = []
    with open(sys.argv[1], 'r') as fp:
        lines = fp.read().split('\n')

    starting_row, starting_column = find_start(lines)

    loop = run_loop(lines, starting_row, starting_column)

    inner_nodes = count_inner_nodes(lines, loop)

    print(f'Part One Answer: {len(loop)//2}')
    print(f'Part Two Answer: {inner_nodes}')
