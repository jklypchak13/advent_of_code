import sys
import functools


memo = {}


def get_arrangements(springs, groups):
    # Check if we are done/have found a valid configuration
    if len(springs) == 0:
        return 1 if len(groups) == 0 else 0
    if len(groups) == 0:
        return 1 if '#' not in springs else 0

    # Check Memoization table
    key = springs, groups
    if key in memo:
        return memo[key]

    current = springs[0]
    res = 0
    # process a ., or treat the current ? as a .
    if current in '.?':
        res += get_arrangements(springs[1:], groups)

    # Process a #, or treat the current ? as a #
    if current in '#?':
        # See if we can consume the next group
        if groups[0] <= len(springs) and '.' not in springs[0:groups[0]] and (len(line) == groups[0] or line[groups[0]] != '#'):
            res += get_arrangements(springs[groups[0] + 1:], groups[1:])
    memo[key] = res
    return res


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('Need arguments')
        sys.exit(-1)

    # Get Data
    lines = []
    with open(sys.argv[1], 'r') as fp:
        lines = fp.read().split('\n')

    total_arrangements = 0
    total_two = 0
    for line in lines:
        springs = line.split(' ')[0]
        part_two_springs = f'{springs}?' * 5
        groups = tuple([int(value) for value in line.split(' ')[1].split(',')])
        total_arrangements += get_arrangements(springs, groups)
        total_two += get_arrangements(part_two_springs[:-1], groups * 5)

    print(f'Part One Answer: {total_arrangements}')
    print(f'Part Two Answer: {total_two}')
