from shared.types import Result
from shared.input import get_input

INPUT_DATA = "day22/input.txt"
SAMPLE_DATA = "day22/sample.txt"


def day22() -> Result:
    res = Result()
    input = get_input(INPUT_DATA)
    return res


if __name__ == '__main__':
    result = day22()
    print(f'Day 22 Part 1: {result.p1}')
    print(f'Day 22 Part 2: {result.p2}')
