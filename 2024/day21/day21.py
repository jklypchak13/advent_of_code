from shared.types import Result
from shared.input import get_input

INPUT_DATA = "day21/input.txt"
SAMPLE_DATA = "day21/sample.txt"


def day21() -> Result:
    res = Result()
    input = get_input(INPUT_DATA)
    return res


if __name__ == '__main__':
    result = day21()
    print(f'Day 21 Part 1: {result.p1}')
    print(f'Day 21 Part 2: {result.p2}')
