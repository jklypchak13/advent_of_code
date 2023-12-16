import sys


def count_incorrect_spots(line, left, right):
    incorrect = 0
    length = min(left + 1, len(line) - right)

    for i in range(length):
        if line[left - i] != line[right + i]:
            incorrect += 1
    return incorrect


def find_vertical_line(group, wrong_spots):
    # Assume the line is mirrored between 0 and 1
    left = 0
    right = 1

    while left < len(group[0]) - 1:
        incorrect_spots = 0
        for line in group:
            incorrect_spots += count_incorrect_spots(line, left, right)
            # Exit early if we have too many failures
            if incorrect_spots > wrong_spots:
                break
        # If we have the correct number of missed spots, return!
        if incorrect_spots == wrong_spots:
            return left + 1
        left += 1
        right += 1
    return 0


def find_horizontal_line(group: list[str], wrong_spots):
    flipped = list(reversed(list(zip(*group))))
    return find_vertical_line(flipped, wrong_spots)


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('Need arguments')
        sys.exit(-1)

    # Get Data
    lines = []
    with open(sys.argv[1], 'r') as fp:
        lines = fp.read().split('\n')

    # Split the lines into the different groups (on "")
    groups = []
    current_group = []
    for line in lines:
        if line == '':
            groups.append(current_group)
            current_group = []
        else:
            current_group.append(line)
    groups.append(current_group)

    part_one_total = 0
    part_two_total = 0
    for group in groups:
        part_one_total += find_vertical_line(group, 0)
        part_one_total += 100 * find_horizontal_line(group, 0)
        part_two_total += find_vertical_line(group, 1)
        part_two_total += 100 * find_horizontal_line(group, 1)

    print(f'Part One Answer: {part_one_total}')
    print(f'Part Two Answer: {part_two_total}')
