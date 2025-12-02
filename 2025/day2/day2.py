from aoc_utils.types import Result
from aoc_utils.input import get_input

INPUT_DATA = "day2/input.txt"
SAMPLE_DATA = "day2/sample.txt"

def sum_p1_invalid_ids(start, end):
    total = 0
    for value in range(start,end+1):
        str_value = str(value)
        n = len(str_value)
        if str_value[0:n//2] == str_value[n//2:]:
            total += value
    return total

def contains_sequences(value):
    n = len(value)
    for i in range(1, n//2+1):
        # Optimization, check if n can be composed only of sequences of length i
        if n % i != 0:
            return False
        sub_string = value[:i]
        if sub_string * (n//i) == value:
            return True
    return False

def sum_p2_invalid_ids(start, end):
    total = 0
    for value in range(start, end+1):
        if contains_sequences(str(value)):
            total += value
    return total

def day2() -> Result:
    res = Result()
    input_values = get_input(INPUT_DATA)
    line = input_values[0]
    ranges = [(int(value.split('-')[0]), int(value.split('-')[1])) for value in line.split(',')]
    res.p1 = 0
    res.p2 = 0
    for start,end in ranges:
        res.p1 += sum_p1_invalid_ids(start, end)
        res.p2 += sum_p2_invalid_ids(start, end)
    return res


if __name__ == '__main__':
    result = day2()
    print(f'Day 2 Part 1: {result.p1}')
    print(f'Day 2 Part 2: {result.p2}')