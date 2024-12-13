from shared.types import Result
from shared.input import get_input

INPUT_DATA = "day13/input.txt"
SAMPLE_DATA = "day13/sample.txt"

Button = tuple[int, int]
Point = tuple[int, int]
Machine = tuple[Button, Button, Point]


def parse_line(line: str, prefix) -> Point:
    line = line[line.index(prefix) + 1:]
    dx = line[:line.index(',')]
    line = line[line.index(prefix) + 1:]
    dy = line
    return int(dx), int(dy)


def get_machines(lines: list[str]) -> list[Machine]:
    machines = []
    while len(lines) > 0:
        if lines[0] == '':
            lines.pop(0)
        a = parse_line(lines[0], '+')
        b = parse_line(lines[1], '+')
        prize = parse_line(lines[2], '=')
        lines = lines[3:]
        machines.append((a, b, prize))
    return machines


def solve(a: Button, b: Button, prize: Point) -> int:
    """ Solve as a system of two equations. The prize will be winnable if the results are integers

    a[0] * x + b[0] * y = prize[0]
    a[1] * x + b[1] * y = prize[1]

    resulting matrix notation is
    | a[0] b[0]| * | x | = |prize[0]|
    | a[1] b[1]| * | y |   |prize[1]|

    After doing matrix math, that results in the following:
    |  b[1] -b[0] | DOT | prize[0] | *                  1 
    | -a[1]  a[0] |     | prize[1] |   ((a[0]  * b[1]) - (b[0] * a[1]))

    """
    determinate = 1 / (a[0] * b[1] - b[0] * a[1])
    a_presses = round((b[1] * prize[0] - b[0] * prize[1]) * determinate)
    b_presses = round((-a[1] * prize[0] + a[0] * prize[1]) * determinate)
    # Check to make sure the rounded results actually match the target value
    for i in range(2):
        if a_presses * a[i] + b_presses * b[i] != prize[i]:
            return 0
    return a_presses * 3 + b_presses


def move_prize(prize: Point) -> Point:
    SHIFT = 10000000000000
    return prize[0] + SHIFT, prize[1] + SHIFT


def day13() -> Result:
    res = Result()
    input = get_input(INPUT_DATA)
    machines = get_machines(input)
    res.p1, res.p2 = 0, 0
    for a, b, prize in machines:
        res.p1 += solve(a, b, prize)
        res.p2 += solve(a, b, move_prize(prize))
    return res


if __name__ == '__main__':
    result = day13()
    print(f'Day 13 Part 1: {result.p1}')
    print(f'Day 13 Part 2: {result.p2}')
