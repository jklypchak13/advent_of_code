import sys


def shoelace(points):
    n = len(points)
    res = 0
    for i in range(n):
        x1, y1 = points[i]
        x2, y2 = points[(i + 1) % n]
        res += x1 * y2 - x2 * y1
    return abs(res) // 2


def get_instruction(color):
    DIRECTIONS = ['R', 'D', 'L', 'U']
    return DIRECTIONS[int(color[-2])], int(color[2:-2], 16)


def dig_hole(lines, use_color):
    DIRECTION_MAP = {
        'D': (1, 0),
        'U': (-1, 0),
        'L': (0, -1),
        'R': (0, 1),
    }

    points = [(0, 0)]
    pos = (0, 0)
    perimeter = 0
    for line in lines:
        direction, number, color = line.split(' ')
        if use_color:
            direction, number = get_instruction(color)
        number = int(number)
        perimeter += number
        dx, dy = DIRECTION_MAP[direction]
        x, y = pos
        pos = (x + dx * number, y + dy * number)
        points.append(pos)
    return shoelace(points) + perimeter // 2 + 1


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('Need arguments')
        sys.exit(-1)

    # Get Data
    lines = []
    with open(sys.argv[1], 'r') as fp:
        lines = fp.read().split('\n')

    print(f'Part One Answer: {dig_hole(lines, False)}')
    print(f'Part Two Answer: {dig_hole(lines, True)}')
