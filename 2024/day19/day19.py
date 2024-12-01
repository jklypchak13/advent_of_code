from shared.types import Result
from shared.input import get_input

INPUT_DATA = "day19/input.txt"
SAMPLE_DATA = "day19/sample.txt"


def day19() -> Result:
    res = Result()
    input = get_input(INPUT_DATA)
    return res


if __name__ == '__main__':
    result = day19()
    print(f'Day 19 Part 1: {result.p1}')
    print(f'Day 19 Part 2: {result.p2}')
