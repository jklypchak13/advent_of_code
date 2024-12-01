from shared.types import Result
from shared.input import get_input

INPUT_DATA = "day1/input.txt"
SAMPLE_DATA = "day1/sample.txt"


def read_input(lines: list[str]) -> tuple[list, list]:
    a = []
    b = []
    for line in lines:
        values = line.split('   ')
        a.append(int(values[0]))
        b.append(int(values[1]))
    return a, b


def get_distance(a: list[int], b: list[int]) -> int:
    a = sorted(a)
    b = sorted(b)
    distance = 0
    for i, j in zip(a, b):
        dist = abs(j - i)
        distance += dist
    return distance


def get_similarity_score(a: list[int], b: list[int]) -> int:
    counts = {}
    score = 0
    for value in a:
        if value in counts:
            score += value * counts[value]
        else:
            counts[value] = b.count(value)
            score += value * counts[value]
    return score


def day1() -> Result:
    res = Result()
    input = get_input(INPUT_DATA)
    a, b = read_input(input)
    res.p1 = get_distance(a, b)
    res.p2 = get_similarity_score(a, b)
    return res


if __name__ == '__main__':
    result = day1()
    print(f'Day 1 Part 1: {result.p1}')
    print(f'Day 1 Part 2: {result.p2}')
