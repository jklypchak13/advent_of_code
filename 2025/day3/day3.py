from aoc_utils.types import Result
from aoc_utils.input import get_input

INPUT_DATA = "day3/input.txt"
SAMPLE_DATA = "day3/sample.txt"

def find_highest(bank, start, end):
    # Scan backwards, finding the highest value that's the furthest to the left
    best = int(bank[end])
    index = end
    for j in range(end-1, start-1, -1):
        current_digit = int(bank[j])
        # Equality, because we want the furthest left max value
        if current_digit >= best:
            best = current_digit
            index = j
    return best, index

def get_joltage(bank, count):
    joltage = 0
    left = 0
    for i in range(count):
        right = len(bank) - (count - i)
        best, index = find_highest(bank, left, right)
        joltage = joltage * 10 + best
        left = index + 1
    return joltage

def day3() -> Result:
    res = Result()
    input_lines = get_input(INPUT_DATA)
    res.p1 = 0
    res.p2 = 0
    for line in input_lines:
        res.p1 += get_joltage(line, 2)
        res.p2 += get_joltage(line, 12)
    return res


if __name__ == '__main__':
    result = day3()
    print(f'Day 3 Part 1: {result.p1}')
    print(f'Day 3 Part 2: {result.p2}')
