from shared.types import Result
from shared.input import get_input

INPUT_DATA = "day15/input.txt"
SAMPLE_DATA = "day15/sample.txt"


def day15() -> Result:
    res = Result()
    input = get_input(INPUT_DATA)
    return res


if __name__ == '__main__':
    result = day15()
    print(f'Day 15 Part 1: {result.p1}')
    print(f'Day 15 Part 2: {result.p2}')
