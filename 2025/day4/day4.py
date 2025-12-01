from aoc_utils.types import Result
from aoc_utils.input import get_input

INPUT_DATA = "day4/input.txt"
SAMPLE_DATA = "day4/sample.txt"

def day4() -> Result:
    res = Result()
    input = get_input(INPUT_DATA)
    res.p1 = '0'
    res.p2 = '0'
    return res


if __name__ == '__main__':
    result = day4()
    print(f'Day 4 Part 1: {result.p1}')
    print(f'Day 4 Part 2: {result.p2}')
