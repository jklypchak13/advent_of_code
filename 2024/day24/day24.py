from shared.types import Result
from shared.input import get_input

INPUT_DATA = "day24/input.txt"
SAMPLE_DATA = "day24/sample.txt"


def day24() -> Result:
    res = Result()
    input = get_input(INPUT_DATA)
    return res


if __name__ == '__main__':
    result = day24()
    print(f'Day 24 Part 1: {result.p1}')
    print(f'Day 24 Part 2: {result.p2}')
