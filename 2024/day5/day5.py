from shared.types import Result
from shared.input import get_input

INPUT_DATA = "day5/input.txt"
SAMPLE_DATA = "day5/sample.txt"


def day5() -> Result:
    res = Result()
    input = get_input(INPUT_DATA)
    return res


if __name__ == '__main__':
    result = day5()
    print(f'Day 5 Part 1: {result.p1}')
    print(f'Day 5 Part 2: {result.p2}')
