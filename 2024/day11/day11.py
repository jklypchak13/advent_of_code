from shared.types import Result
from shared.input import get_input
from collections import defaultdict
from functools import cache

INPUT_DATA = "day11/input.txt"
SAMPLE_DATA = "day11/sample.txt"

StoneCounts = defaultdict[str, int]


@cache
def transform_stone(stone: str) -> tuple[str]:
    if stone == '0':
        return ('1',)
    if len(stone) % 2 == 0:
        return (str(int(stone[0:len(stone) // 2])), str(int(stone[len(stone) // 2:])))
    return (str(int(stone) * 2024),)


def step_stones(stones: StoneCounts) -> StoneCounts:
    new_stones = defaultdict(int)
    for stone in stones:
        count = stones[stone]
        transformed = transform_stone(stone)

        # For each new stone, we will get one for each of those values in our original list
        for new_stone in transformed:
            new_stones[new_stone] += count
    return new_stones


def take_steps(stones: StoneCounts, step_count: int) -> int:
    for _ in range(step_count):
        stones = step_stones(stones)
    return sum(stones.values())


def day11() -> Result:
    res = Result()
    input = get_input(INPUT_DATA)[0].split(' ')

    # Store the number of each stone that exists
    stones = defaultdict(int)
    for stone in input:
        stones[stone] += 1
    res.p1 = take_steps(stones, 25)
    res.p2 = take_steps(stones, 75)
    return res


if __name__ == '__main__':
    result = day11()
    print(f'Day 11 Part 1: {result.p1}')
    print(f'Day 11 Part 2: {result.p2}')
