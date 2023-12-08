import sys

ONLY_DIGITS = [f'{i}' for i in range(1, 10)]
WORD_DIGITS = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']


def calibration_from_line(line: str, digits):
    first = -1
    last = -1
    for i in range(len(line)):
        for index, digit in enumerate(digits):
            if line[i:].startswith(digit):
                last = index % 9 + 1
                if first == -1:
                    first = last
    return first * 10 + last


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('Need arguments')
        sys.exit(-1)

    # Get Data
    data = []
    with open(sys.argv[1], 'r') as fp:
        data = fp.readlines()

    digit_group = WORD_DIGITS
    digit_group.extend(ONLY_DIGITS)
    part_one_answer, part_two_answer = 0, 0
    for line in data:
        part_one_answer += calibration_from_line(line, ONLY_DIGITS)
        part_two_answer += calibration_from_line(line, digit_group)
    print(f'Part One Answer: {part_one_answer}')
    print(f'Part Two Answer: {part_two_answer}')
