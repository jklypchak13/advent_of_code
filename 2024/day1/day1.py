from shared.types import Result
from shared.input import get_input

INPUT_DATA = "day1/input.txt"
SAMPLE_DATA = "day1/sample.txt"


def day1() -> Result:
    res = Result()
    input = get_input(INPUT_DATA)
    return res


if __name__ == '__main__':
    result = day1()
    print(f'Day 1 Part 1: {result.p1}')
    print(f'Day 1 Part 2: {result.p2}')
