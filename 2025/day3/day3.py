from aoc_utils.types import Result
from aoc_utils.input import get_input

INPUT_DATA = "day3/input.txt"
SAMPLE_DATA = "day3/sample.txt"

def day3() -> Result:
    res = Result()
    input = get_input(INPUT_DATA)
    res.p1 = '0'
    res.p2 = '0'
    return res


if __name__ == '__main__':
    result = day3()
    print(f'Day 3 Part 1: {result.p1}')
    print(f'Day 3 Part 2: {result.p2}')
