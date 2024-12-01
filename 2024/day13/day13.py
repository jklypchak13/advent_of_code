from shared.types import Result
from shared.input import get_input

INPUT_DATA = "day13/input.txt"
SAMPLE_DATA = "day13/sample.txt"


def day13() -> Result:
    res = Result()
    input = get_input(INPUT_DATA)
    return res


if __name__ == '__main__':
    result = day13()
    print(f'Day 13 Part 1: {result.p1}')
    print(f'Day 13 Part 2: {result.p2}')
