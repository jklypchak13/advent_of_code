import sys

import time


def load_brick(line):
    first = [int(value) for value in line.split('~')[0].split(',')]
    second = [int(value) for value in line.split('~')[1].split(',')]
    return first, second


def add_to_space(first, second, brick_id, space):
    res = set()

    min_x = min(first[0], second[0])
    min_y = min(first[1], second[1])
    min_z = min(first[2], second[2])
    max_x = max(first[0], second[0])
    max_y = max(first[1], second[1])
    max_z = max(first[2], second[2])

    closest_z = 0
    for (x, y, z), id in space.items():
        if min_x <= x <= max_x and min_y <= y <= max_y:
            if z > closest_z:
                res = set([id])
                closest_z = z
            elif z == closest_z:
                res.add(id)

    shift = closest_z + 1 - min_z
    for x in range(min_x, max_x + 1):
        for y in range(min_y, max_y + 1):
            for z in range(min_z + shift, max_z + 1 + shift):
                space[(x, y, z)] = brick_id
    return res


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('Need arguments')
        sys.exit(-1)

    # Get Data
    lines = []
    with open(sys.argv[1], 'r') as fp:
        lines = fp.read().split('\n')

    # Load the space
    bricks = []
    for i, line in enumerate(lines):
        bricks.append(load_brick(line))

    bricks.sort(key=lambda x: min(x[0][2], x[1][2]))

    space = {}
    can_remove = set([i for i in range(len(lines))])
    rests_on = {}
    for i, brick in enumerate(bricks):
        supported_by = add_to_space(brick[0], brick[1], i, space)
        rests_on[i] = set(supported_by.copy())
        if len(supported_by) == 1:
            brick_id = supported_by.pop()
            if brick_id in can_remove:
                can_remove.remove(brick_id)

    total = 0
    for c_i in range(len(lines)):
        if c_i in can_remove:
            continue
        fall = set()
        new_fall = set([c_i])
        while len(new_fall) > len(fall):
            fall.update(new_fall)
            for c_j in range(len(lines)):
                if all(ro in new_fall for ro in rests_on[c_j]):
                    new_fall.add(c_j)
        total += len(fall) - 1

    for i in range(len(lines)):
        print(rests_on[i])
    print(f'Part One Answer: {len(can_remove)}')
    print(f'Part Two Answer: {total}')
