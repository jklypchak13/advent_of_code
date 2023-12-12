import sys


def get_next_value(line: list[int]):
    if set(line) == {0}:
        return 0
    diffs = [line[i + 1] - line[i] for i in range(len(line) - 1)]
    return line[-1] + get_next_value(diffs)


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('Need arguments')
        sys.exit(-1)

    # Get Data
    lines = []
    with open(sys.argv[1], 'r') as fp:
        lines = fp.read().split('\n')

    total = 0
    total_two = 0
    for line in lines:
        total += get_next_value([int(value) for value in line.split(' ')])
        total_two += get_next_value(list(reversed([int(value) for value in line.split(' ')])))

    print(f'Part One Answer: {total}')
    print(f'Part Two Answer: {total_two}')
