from aoc_utils.types import Result
from aoc_utils.input import get_input

INPUT_DATA = "day5/input.txt"
SAMPLE_DATA = "day5/sample.txt"

def parse_input(lines:list[str]):
    split = lines.index('')
    range_values = lines[:split]
    values = [int(value) for value in lines[split+1:]]
    ranges = []
    for value in range_values:
        start, end = value.split('-')
        ranges.append((int(start),int(end)))

    return ranges, values

def is_fresh(value, ranges):
    for rng in ranges:
        if in_range(value, rng):
            return True
    return False

def count_fresh(ranges, values):
    count = 0
    for value in values:
        if is_fresh(value, ranges):
            count += 1
    return count

def in_range(value, range_value):
    return range_value[0] <= value <= range_value[1]

def merge_ranges(ranges):
    ranges = sorted(ranges)
    merged = []

    current_start, current_end = ranges[0]
    for start, end in ranges[1:]:
        if start <= current_end:
            current_end = max(end, current_end)
        else:
            merged.append((current_start, current_end))
            current_start, current_end = start, end

    merged.append((current_start, current_end))
    return merged

def count_ranges(ranges):
    total = 0
    for start, end in ranges:
        total += (end - start + 1)
    return total

def day5() -> Result:
    res = Result()
    input_lines = get_input(INPUT_DATA)
    ranges, values = parse_input(input_lines)

    # Clean up the ranges
    ranges = merge_ranges(ranges)

    res.p1 = count_fresh(ranges, values)
    res.p2 = count_ranges(ranges)
    return res


if __name__ == '__main__':
    result = day5()
    print(f'Day 5 Part 1: {result.p1}')
    print(f'Day 5 Part 2: {result.p2}')
