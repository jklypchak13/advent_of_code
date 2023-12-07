import sys


def get_seeds(line):
    seeds = line.split(': ')[1].split(' ')
    return [int(s) for s in seeds]


def get_part_two_seeds(line):
    seeds = get_seeds(line)
    result = []
    for i in range(0, len(seeds), 2):
        for j in range(seeds[i], seeds[i] + seeds[i + 1]):
            result.append(j)
    return result


def get_map_sections(lines):
    maps = []

    current_map = []
    for line in lines:
        if line == '':
            maps.append(current_map)
            current_map = []
        else:
            current_map.append(line)
    maps.append(current_map)
    return maps


def build_map_list(map):
    # build_map_functions
    def helper(number):
        for i, line in enumerate(map):
            # skip first line
            if i == 0:
                continue
            dest, source, length = line.split(' ')
            if int(source) <= number < int(source) + int(length):
                return int(dest) + number - int(source)
        return number
    return helper


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
    maps = get_map_sections(lines[2:])

    functions = []
    for map_lines in maps:
        functions .append(build_map_list(map_lines))

    locations = []
    for seed in seeds:
        print(f'Seed: {seed}')
        current = seed
        for function in functions:
            current = function(current)
        locations.append(current)
    print(min(locations))
    print(get_part_two_seeds(lines[0]))
