from shared.types import Result
from shared.input import get_input

INPUT_DATA = "day14/input.txt"
SAMPLE_DATA = "day14/sample.txt"


def day14() -> Result:
    res = Result()
    input = get_input(INPUT_DATA)
    return res


if __name__ == '__main__':
    result = day14()
    print(f'Day 14 Part 1: {result.p1}')
    print(f'Day 14 Part 2: {result.p2}')
