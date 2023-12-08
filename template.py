import sys


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('Need arguments')
        sys.exit(-1)

    # Get Data
    lines = []
    with open(sys.argv[1], 'r') as fp:
        lines = fp.read().split('\n')

    print(f'Part One Answer: {0}')
    print(f'Part Two Answer: {0}')
