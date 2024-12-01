from shared.types import Result
from shared.input import get_input

INPUT_DATA = "day16/input.txt"
SAMPLE_DATA = "day16/sample.txt"


def day16() -> Result:
    res = Result()
    input = get_input(INPUT_DATA)
    return res


if __name__ == '__main__':
    result = day16()
    print(f'Day 16 Part 1: {result.p1}')
    print(f'Day 16 Part 2: {result.p2}')
