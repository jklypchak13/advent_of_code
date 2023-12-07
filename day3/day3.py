

import sys
from typing import List

DIGITS = [f'{i}' for i in range(0, 10)]


def check_neighbors(data: List[List[str]], row, column):
    for i in range(-1, 2):
        for j in range(-1, 2):
            x, y = row + i, column + j
            if 0 <= x < len(data) and 0 <= y < len(data[0]):
                if data[x][y] != '.' and data[x][y] not in DIGITS:
                    return True
    return False


def check_neighbors_gears(data: List[List[str]], row, column):
    gears = set()
    for i in range(-1, 2):
        for j in range(-1, 2):
            x, y = row + i, column + j
            if 0 <= x < len(data) and 0 <= y < len(data[0]):
                if data[x][y] == '*':
                    gears.add((x, y))
    return gears


def get_part_numbers_in_line(data, line, i):
    total = 0
    col = 0
    numbers_gears = []
    all_gears = []
    while col < len(line):
        if line[col] in DIGITS:
            gears = set()
            current_num = 0
            is_valid = False
            while col < len(line) and line[col] in DIGITS:
                current_num = current_num * 10 + int(line[col])
                is_valid = is_valid or check_neighbors(data, i, col)
                gears = gears.union(check_neighbors_gears(data, i, col))
                col += 1
            if is_valid:
                total += current_num
            numbers_gears.append((current_num, gears))
        elif line[col] == '*':
            all_gears.append((i, col))
            col += 1
        else:
            col += 1
    return total, numbers_gears, all_gears


def total_parts(data):
    total = 0
    gears = []
    numbers_gears = []
    for i, line in enumerate(data):
        res, current_numbers_gears, current_gears = get_part_numbers_in_line(data, line, i)
        total += res
        gears.extend(current_gears)
        numbers_gears.extend(current_numbers_gears)

    product = 0
    for gear in gears:
        numbers = []
        current_product = 1
        for number, gear_set in numbers_gears:
            for current_gear in gear_set:
                if current_gear[0] == gear[0] and current_gear[1] == gear[1]:
                    numbers.append(number)
                    current_product *= number
        if len(numbers) == 2:
            product += current_product

    return total, product


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('Need arguments')
        sys.exit(-1)

    # Get Data
    data = []
    with open(sys.argv[1], 'r') as fp:
        data = fp.readlines()

    clean_data = []
    for line in data:
        clean_data.append(line.strip())

    part_one_answer, part_two_answer = 0, 0

    part_one_answer, part_two_answer = total_parts(clean_data)
    print(f'Part 1 Answer: {part_one_answer}')
    print(f'Part 2 Answer: {part_two_answer}')
