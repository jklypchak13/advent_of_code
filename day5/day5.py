import sys
from typing import List, Tuple


def get_min(seeds):
    low = seeds[0][0]

    for seeds in seeds:
        if seeds[0] < low:
            low = seeds[0]
    return low


def get_seeds(line):
    seeds = line.split(': ')[1].split(' ')

    res = []

    for i in range(0, len(seeds), 2):
        res.append((int(seeds[i]), int(seeds[i]) + int(seeds[i + 1]) - 1))
    return res


def get_seeds_part_one(line):
    seeds = line.split(': ')[1].split(' ')

    return [(int(seed), int(seed)) for seed in seeds]


def get_total_seeds(seeds):
    total = 0
    for low, high in seeds:
        total += high - low + 1
    return total


def get_map_function(lines):
    def helper(seeds):
        j = 0
        res = []
        while j < len(seeds):
            added = False
            seed_low, seed_high = seeds[j]
            for i, line in enumerate(lines):
                if i == 0:
                    continue
                dst, source, length = line.split(' ')
                lower = int(source)
                higher = lower + int(length) - 1
                offset = int(dst) - lower
                if (seed_low >= lower and seed_high <= higher):
                    added = True
                    res.append((seed_low + offset, seed_high + offset))
                    break
                elif (seed_low < lower and lower <= seed_high <= higher):
                    added = True
                    seeds.append((seed_low, lower - 1))
                    res.append((int(dst), seed_high + offset))
                    break
                elif (higher >= seed_low >= lower and seed_high > higher):
                    added = True
                    res.append((seed_low + offset, higher + offset))
                    seeds.append((higher + 1, seed_high))
                    break
            if not added:
                added = True
                res.append((seed_low, seed_high))
            j += 1
        return res
    return helper


def build_maps(lines):
    maps = []
    current_lines = []
    for line in lines:
        if line == '':
            maps.append(get_map_function(current_lines))
            current_lines = []
        else:
            current_lines.append(line)
    maps.append(get_map_function(current_lines))
    return maps


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('Need arguments')
        sys.exit(-1)

    # Get Data
    data = ''
    with open(sys.argv[1], 'r') as fp:
        data = fp.read()

    lines = data.split('\n')
    seeds = get_seeds(lines[0])
    part_one_seeds = get_seeds_part_one(lines[0])

    maps = build_maps(lines[2:])

    current = seeds
    current_part_one = part_one_seeds
    for m in maps:
        new_seeds: List[Tuple[int, int]] = []
        current = m(current)
        current_part_one = m(current_part_one)

    print(f'Part One Answer: {get_min(current_part_one)}')
    print(f'Part Two Answer: {get_min(current)}')
