from shared.types import Result
from shared.input import get_input

INPUT_DATA = "day12/input.txt"
SAMPLE_DATA = "day12/sample.txt"


def day12() -> Result:
    res = Result()
    input = get_input(INPUT_DATA)
    return res


if __name__ == '__main__':
    result = day12()
    print(f'Day 12 Part 1: {result.p1}')
    print(f'Day 12 Part 2: {result.p2}')
