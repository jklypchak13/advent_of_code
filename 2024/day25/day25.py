from shared.types import Result
from shared.input import get_input

INPUT_DATA = "day25/input.txt"
SAMPLE_DATA = "day25/sample.txt"


def day25() -> Result:
    res = Result()
    input = get_input(INPUT_DATA)
    return res


if __name__ == '__main__':
    result = day25()
    print(f'Day 25 Part 1: {result.p1}')
    print(f'Day 25 Part 2: {result.p2}')
