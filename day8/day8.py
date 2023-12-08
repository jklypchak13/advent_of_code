import sys
import math

START = 'AAA'
DEST = 'ZZZ'


def load_instructions(lines):
    return {line.split(' = ')[0]: line.split(' = ')[1][1:-1].split(', ') for line in lines}


def do_run(start, instructions, directions, done):
    current = start
    steps = 0
    while not done(current):
        current = instructions[current][directions[steps % len(directions)]]
        steps += 1
    return steps


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('Need arguments')
        sys.exit(-1)

    # Get Data
    lines = []
    with open(sys.argv[1], 'r') as fp:
        lines = fp.read().split('\n')

    # Load Input
    directions = [0 if c == 'L' else 1 for c in lines[0]]
    instructions = load_instructions(lines[2:])

    print(f'Part One Answer: {do_run(START, instructions, directions, lambda x : x == DEST)}')

    starts = [current for current in instructions.keys() if current.endswith('A')]
    steps = [do_run(current, instructions, directions, lambda x: x.endswith('Z')) for current in starts]

    print(f'Part Two Answer: {math.lcm(*steps)}')
