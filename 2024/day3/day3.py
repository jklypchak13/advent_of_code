from shared.types import Result
from shared.input import get_input
import re

INPUT_DATA = "day3/input.txt"
SAMPLE_DATA = "day3/sample.txt"


def process_instructions(data, regex: re.Pattern):
    total = 0
    active = True
    hits = regex.findall(data)
    for hit in hits:
        if hit == 'do()':
            active = True
        elif hit == "don't()":
            active = False
        elif active:
            digits = hit[4:-1].split(',')
            total += int(digits[0]) * int(digits[1])
    return total


def day3() -> Result:
    MULT_REGEX = 'mul\([0-9]{1,3},[0-9]{1,3}\)'
    DO_REGEX = 'do\(\)'
    DONT_REGEX = "don't\(\)"
    res = Result()
    input = ''.join(get_input(INPUT_DATA))
    res.p1 = process_instructions(input, re.compile(f'{MULT_REGEX}'))
    res.p2 = process_instructions(input, re.compile(f'({MULT_REGEX}|{DO_REGEX}|{DONT_REGEX})'))
    return res


if __name__ == '__main__':
    result = day3()
    print(f'Day 3 Part 1: {result.p1}')
    print(f'Day 3 Part 2: {result.p2}')
