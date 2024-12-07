from shared.types import Result
from shared.input import get_input
from typing import Callable

INPUT_DATA = "day7/input.txt"
SAMPLE_DATA = "day7/sample.txt"

# Operations
Operation = Callable[[int, int], int]
def add(x, y): return x + y
def mult(x, y): return x * y
def concat(x, y): return int(str(x) + str(y))


def is_valid(target: int, total: int, values: list[int], ops: list[Operation]) -> bool:
    # Check for early return if we are out of values, or we have passed our target
    if len(values) == 0 or total > target:
        return target == total

    # Remove the first value
    current = values[0]
    new_values = values[1:]

    # Try the different operations
    for op in ops:
        if is_valid(target, op(total, current), new_values, ops):
            return True
    return False


def valid_equation(line: str, ops: list[Operation]) -> int:
    data = line.split(': ')
    target = int(data[0])
    values = [int(val) for val in data[1].split(' ')]
    first = values.pop(0)
    return target if is_valid(target, first, values, ops) else 0


def day7() -> Result:
    res = Result()
    input = get_input(INPUT_DATA)
    res.p1 = 0
    res.p2 = 0
    p1_ops = [add, mult]
    p2_ops = [add, mult, concat]
    for line in input:
        res.p1 += valid_equation(line, p1_ops)
        res.p2 += valid_equation(line, p2_ops)
    return res


if __name__ == '__main__':
    result = day7()
    print(f'Day 7 Part 1: {result.p1}')
    print(f'Day 7 Part 2: {result.p2}')
