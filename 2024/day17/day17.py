from shared.types import Result
from shared.input import get_input

INPUT_DATA = "day17/input.txt"
SAMPLE_DATA = "day17/sample.txt"


def day17() -> Result:
    res = Result()
    input = get_input(INPUT_DATA)
    return res


if __name__ == '__main__':
    result = day17()
    print(f'Day 17 Part 1: {result.p1}')
    print(f'Day 17 Part 2: {result.p2}')
