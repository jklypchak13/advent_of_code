from shared.types import Result
from shared.input import get_input

INPUT_DATA = "day10/input.txt"
SAMPLE_DATA = "day10/sample.txt"


def day10() -> Result:
    res = Result()
    input = get_input(INPUT_DATA)
    return res


if __name__ == '__main__':
    result = day10()
    print(f'Day 10 Part 1: {result.p1}')
    print(f'Day 10 Part 2: {result.p2}')
