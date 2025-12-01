from aoc_utils.types import Result
from aoc_utils.input import get_input

INPUT_DATA = "day7/input.txt"
SAMPLE_DATA = "day7/sample.txt"

def day7() -> Result:
    res = Result()
    input = get_input(INPUT_DATA)
    res.p1 = '0'
    res.p2 = '0'
    return res


if __name__ == '__main__':
    result = day7()
    print(f'Day 7 Part 1: {result.p1}')
    print(f'Day 7 Part 2: {result.p2}')
