
import sys

COLOR_MAP = {'red': 0, 'green': 1, 'blue': 2}


def is_valid(minimums):
    MASTER = (12, 13, 14)
    for current, max in zip(minimums, MASTER):
        if current > max:
            return False
    return True


def get_minimum_from_line(line):
    # Remove Game label
    line = line.split(': ')[1]
    samples = line.split("; ")

    minimum = [0, 0, 0]
    for sample in samples:
        for color in sample.split(', '):
            data = color.split(' ')
            number = int(data[0])
            index = COLOR_MAP[data[1]]
            minimum[index] = max(number, minimum[index])

    return minimum


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('Need arguments')
        sys.exit(-1)

    # Get Data
    data = []
    with open(sys.argv[1], 'r') as fp:
        data = fp.readlines()

    part_one_answer, part_two_answer = 0, 0
    for line in data:
        game_id = int(line.split(': ')[0].split(' ')[1])
        minimum = get_minimum_from_line(line.strip())
        if is_valid(minimum):
            part_one_answer += game_id
        part_two_answer += minimum[0] * minimum[1] * minimum[2]

    print(f'Part One Answer: {part_one_answer}')
    print(f'Part Two Answer: {part_two_answer}')
