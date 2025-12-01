from aoc_utils.types import Result
from aoc_utils.input import get_input

INPUT_DATA = "day1/input.txt"
SAMPLE_DATA = "day1/sample.txt"

def parse_instruction(line):
    direction = line[0]
    value = int(line[1:])
    return direction, value

def get_new_position(starting_value, direction, count):
    value = 0
    if direction == 'L':
        value = starting_value - count
    else:
        value = starting_value + count
    return value % 100

def count_zero_ends(rotations):
    position = 50
    zeroes = 0
    for line in rotations:
        direction, count = parse_instruction(line)
        new_position = get_new_position(position, direction, count)
        if new_position == 0:
            zeroes += 1
        position = new_position
    return zeroes

def passed_zero(start, end, direction):
    if end == 0:
        return True
    # check for start == 0 because we counted it when we clicked to it
    if direction == 'L' and end > start and start != 0:
        return True
    elif direction == 'R' and start > end:
        return True
    return False

def count_zero_passed(rotations):
    clicks = 0
    value = 50
    for line in rotations:
        direction, count = parse_instruction(line)
        # Account for going in a full circle
        clicks += count // 100
        count = count % 100
        new_value = get_new_position(value, direction, count)
        clicks += 1 if passed_zero(value, new_value, direction) else 0
        value = new_value
    return clicks

def day1() -> Result:
    res = Result()
    input_values = get_input(INPUT_DATA)
    res.p1 = count_zero_ends(input_values)
    res.p2 = count_zero_passed(input_values)
    return res


if __name__ == '__main__':
    result = day1()
    print(f'Day 1 Part 1: {result.p1}')
    print(f'Day 1 Part 2: {result.p2}')
