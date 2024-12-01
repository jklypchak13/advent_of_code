from shared.types import Result
from shared.input import get_input

INPUT_DATA = "day18/input.txt"
SAMPLE_DATA = "day18/sample.txt"


def day18() -> Result:
    res = Result()
    input = get_input(INPUT_DATA)
    return res


if __name__ == '__main__':
    result = day18()
    print(f'Day 18 Part 1: {result.p1}')
    print(f'Day 18 Part 2: {result.p2}')
