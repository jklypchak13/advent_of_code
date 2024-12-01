from shared.types import Result
from shared.input import get_input

INPUT_DATA = "day23/input.txt"
SAMPLE_DATA = "day23/sample.txt"


def day23() -> Result:
    res = Result()
    input = get_input(INPUT_DATA)
    return res


if __name__ == '__main__':
    result = day23()
    print(f'Day 23 Part 1: {result.p1}')
    print(f'Day 23 Part 2: {result.p2}')