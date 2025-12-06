from aoc_utils.types import Result
from aoc_utils.input import get_input

INPUT_DATA = "day6/input.txt"
SAMPLE_DATA = "day6/sample.txt"


def get_values(line:str):
    values = line.split()
    return values

def get_column(i, lines):
    value = ''
    for line in lines:
        if i >= len(line):
            continue
        value += line[i]
    return value

def calculate_column(operation, column):
    start = int(column[0])

    for value in column[1:]:
        value = int(value)
        if operation == '+':
            start += value
        else:
            start *= value
    return start

def process_operation(operation, lines, i):
    column = get_column(i, lines)
    value = 1 if operation == '*' else 0
    while column.strip() != '':
        number = int(column)
        if operation == '*':
            value *= number
        else:
            value += number
        i += 1
        column = get_column(i, lines)
    return i+1, value

def vertical_number_operations(lines, operations:list[str]):
    index = 0
    total = 0
    while len(operations) > 0:
        operation = operations.pop(0)
        index, result = process_operation(operation, lines, index)
        total += result
    return total

def day6() -> Result:
    res = Result()

    # Parse input
    input_lines = get_input(INPUT_DATA)
    operations = get_values(input_lines[-1])
    lines = input_lines[:-1]


    columns = [[value] for value in get_values(input_lines[0])]
    for line in input_lines[1:-1]:
        new_values = get_values(line)
        for value, column in zip(new_values, columns):
            column.append(value)
    res.p1 = 0
    for operation, column in zip(operations, columns):
        res.p1 += calculate_column(operation, column)

    res.p2 = vertical_number_operations(lines, operations)
    return res


if __name__ == '__main__':
    result = day6()
    print(f'Day 6 Part 1: {result.p1}')
    print(f'Day 6 Part 2: {result.p2}')
