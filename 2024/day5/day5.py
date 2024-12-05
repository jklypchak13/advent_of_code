""" Probably could have done something cool with a comparator using the instructions, but this was my first crack at it"""

from shared.types import Result
from shared.input import get_input

INPUT_DATA = "day5/input.txt"
SAMPLE_DATA = "day5/sample.txt"

Rule = tuple[int, int]
Sample = list[int]


def process_input(lines: list[str]) -> tuple[list[Rule], list[Sample]]:
    split = lines.index('')
    instructions = []
    for line in lines[:split]:
        values = line.split('|')
        instructions.append((int(values[0]), int(values[1])))
    samples = []
    for line in lines[split + 1:]:
        samples.append([int(val) for val in line.split(',')])
    return instructions, samples


def breaks_instruction(instruction: Rule, sample: Sample) -> bool:
    first, last = instruction
    if first in sample and last in sample:
        return sample.index(first) > sample.index(last)
    return False


def valid_sample(instructions: list[Rule], sample: Sample) -> bool:
    for instruction in instructions:
        if breaks_instruction(instruction, sample):
            return False
    return True


def fix_instruction(instruction: Rule, sample: Sample) -> bool:
    first, last = instruction
    if not breaks_instruction(instruction, sample):
        return False
    a = sample.index(first)
    b = sample.index(last)
    sample[a] = last
    sample[b] = first
    return True


def fix_sample(instructions: list[Rule], sample: Sample) -> Sample:
    change_count = 0
    for instruction in instructions:
        if fix_instruction(instruction, sample):
            change_count += 1
    if change_count > 0:
        return fix_sample(instructions, sample)
    return sample


def day5() -> Result:
    res = Result()
    input = get_input(INPUT_DATA)

    instructions, samples = process_input(input)
    res.p1 = 0
    res.p2 = 0

    for sample in samples:
        if valid_sample(instructions, sample):
            res.p1 += sample[len(sample) // 2]
        else:
            fixed = fix_sample(instructions, sample)
            res.p2 += fixed[len(fixed) // 2]
    return res


if __name__ == '__main__':
    result = day5()
    print(f'Day 5 Part 1: {result.p1}')
    print(f'Day 5 Part 2: {result.p2}')
