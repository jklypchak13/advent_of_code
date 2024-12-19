from shared.types import Result
from shared.input import get_input
from functools import cache

INPUT_DATA = "day19/input.txt"
SAMPLE_DATA = "day19/sample.txt"


def parse_input(lines: list[str]) -> tuple[tuple[str], list[str]]:
    towels = tuple(lines[0].split(', '))
    return towels, lines[2:]


@cache
def is_possible(target: str, towels: tuple[str]) -> int:
    if target == '':
        return 1
    count = 0
    for towel in towels:
        if not target.startswith(towel):
            continue
        count += is_possible(target[len(towel):], towels)
    return count


def day19() -> Result:
    res = Result()
    lines = get_input(INPUT_DATA)
    towels, targets = parse_input(lines)
    res.p1, res.p2 = 0, 0

    for target in targets:
        result = is_possible(target, towels)
        res.p1 += 1 if result > 1 else 0
        res.p2 += result

    return res


if __name__ == '__main__':
    result = day19()
    print(f'Day 19 Part 1: {result.p1}')
    print(f'Day 19 Part 2: {result.p2}')
