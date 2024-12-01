from shared.types import Result
from shared.input import get_input

INPUT_DATA = "day20/input.txt"
SAMPLE_DATA = "day20/sample.txt"


def day20() -> Result:
    res = Result()
    input = get_input(INPUT_DATA)
    return res


if __name__ == '__main__':
    result = day20()
    print(f'Day 20 Part 1: {result.p1}')
    print(f'Day 20 Part 2: {result.p2}')
