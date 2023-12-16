import sys


def valid_position(grid, position):
    x, y = position
    return 0 <= x < len(grid) and 0 <= y < len(grid[0])


def process_turn(character, direction):
    if character == '/':
        return (direction[1] * -1, direction[0] * -1)
    else:
        return (direction[1], direction[0])


def follow_trail(grid, starting_position, starting_dir, visited, loop_checker):

    position = starting_position
    direction = starting_dir
    while valid_position(grid, position):
        visited.add(position)
        current = grid[position[0]][position[1]]
        x, y = position
        dx, dy = direction

        match current:
            case '.':
                position = (x + dx, y + dy)
            case '-':
                if position in loop_checker and direction in loop_checker[position]:
                    return
                elif position not in loop_checker:
                    loop_checker[position] = []
                loop_checker[position].append(direction)
                if dy > 0:
                    position = (x + dx, y + dy)
                else:
                    # Continue this thread, spawn another
                    position = (x, y + 1)
                    direction = (0, 1)
                    follow_trail(grid, (x, y - 1), (0, -1), visited, loop_checker)
            case '|':
                if position in loop_checker and direction in loop_checker[position]:
                    return
                elif position not in loop_checker:
                    loop_checker[position] = []
                loop_checker[position].append(direction)
                if dx > 0:
                    position = (x + dx, y + dy)
                else:
                    # Continue this thread, spawn another
                    position = (x + 1, y)
                    direction = (1, 0)
                    follow_trail(grid, (x - 1, y), (-1, 0), visited, loop_checker)
            case default:
                if position in loop_checker and direction in loop_checker[position]:
                    return
                elif position not in loop_checker:
                    loop_checker[position] = []
                loop_checker[position].append(direction)
                direction = process_turn(current, direction)
                dx, dy = direction
                position = (x + dx, y + dy)


def energize_grid(grid, start, direction):
    visited = set()

    loop_checker = {}
    visited.add((0, 0))
    follow_trail(grid, start, direction, visited, loop_checker)

    return len(visited)


def find_best_entrance(grid):
    best = 0

    for column in range(len(grid[0])):
        best = max(best, energize_grid(grid, (0, column), (1, 0)))
        best = max(best, energize_grid(grid, (len(grid) - 1, column), (-1, 0)))

    for row in range(len(grid)):
        best = max(best, energize_grid(grid, (row, 0), (0, 1)))
        best = max(best, energize_grid(grid, (row, len(grid[0]) - 1), (0, -1)))
    return best


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('Need arguments')
        sys.exit(-1)

    # Get Data
    lines = []
    with open(sys.argv[1], 'r') as fp:
        lines = fp.read().split('\n')

    print(f'Part One Answer: {energize_grid(lines, (0,0), (0, 1))}')
    print(f'Part Two Answer: {find_best_entrance(lines)}')
