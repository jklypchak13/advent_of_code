from shared.types import Result
from shared.input import get_input

INPUT_DATA = "day11/input.txt"
SAMPLE_DATA = "day11/sample.txt"


def day11() -> Result:
    res = Result()
    input = get_input(INPUT_DATA)
    return res


if __name__ == '__main__':
    result = day11()
    print(f'Day 11 Part 1: {result.p1}')
    print(f'Day 11 Part 2: {result.p2}')
