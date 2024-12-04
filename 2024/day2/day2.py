from shared.types import Result
from shared.input import get_input

INPUT_DATA = "day2/input.txt"
SAMPLE_DATA = "day2/sample.txt"


def parse_report(line: str) -> list[int]:
    return [int(val) for val in line.split(' ')]


def is_safe(report: list[int]) -> bool:
    sign = (report[0] - report[1]) >= 0
    for i in range(len(report) - 1):
        diff = report[i] - report[i + 1]
        # Check if the difference is in the acceptable range, and that we are still matching the direction of change
        if abs(diff) < 1 or abs(diff) > 3 or (sign != (diff >= 0)):
            return False
    return True


def count_safe(lines: list[str]) -> bool:
    count = 0
    for line in lines:
        report = parse_report(line)
        if is_safe(report):
            count += 1
    return count


def safe_with_error(report: list[int]) -> bool:
    for i in range(len(report)):
        # Try to remove the ith element
        temp = report[0:i]
        temp.extend(report[i + 1:])
        if is_safe(temp):
            return True
    return False


def count_safe_with_error(lines: list[str]) -> bool:
    count = 0
    for line in lines:
        report = parse_report(line)
        if is_safe(report) or safe_with_error(report):
            count += 1
    return count


def day2() -> Result:
    res = Result()
    input = get_input(INPUT_DATA)

    res.p1 = count_safe(input)
    res.p2 = count_safe_with_error(input)
    return res


if __name__ == '__main__':
    result = day2()
    print(f'Day 2 Part 1: {result.p1}')
    print(f'Day 2 Part 2: {result.p2}')
