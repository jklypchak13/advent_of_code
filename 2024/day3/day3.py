from shared.types import Result
from shared.input import get_input
from shared.parser.interpret import interpret_tokens
from shared.parser.tokenizer import Tokenizer
import re

INPUT_DATA = "day3/input.txt"
SAMPLE_DATA = "day3/sample.txt"


def process_instructions(data, regex: re.Pattern):
    total = 0
    active = True
    hits = regex.findall(data)
    for hit in hits:
        if hit == 'do()':
            active = True
        elif hit == "don't()":
            active = False
        elif active:
            digits = hit[4:-1].split(',')
            total += int(digits[0]) * int(digits[1])
    return total


def day3() -> Result:
    res = Result()
    input = ''.join(get_input(INPUT_DATA))
    tokenizer = Tokenizer(input)
    res.p1 = interpret_tokens(tokenizer)
    tokenizer.reset()
    res.p2 = interpret_tokens(tokenizer, True)
    return res


if __name__ == '__main__':
    result = day3()
    print(f'Day 3 Part 1: {result.p1}')
    print(f'Day 3 Part 2: {result.p2}')
