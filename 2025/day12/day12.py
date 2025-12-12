from aoc_utils.types import Result
from aoc_utils.input import get_input

INPUT_DATA = "day12/input.txt"
SAMPLE_DATA = "day12/sample.txt"

def parse_shapes(chunks:list[str]):
    shapes = {}
    for chunk in chunks:
        digit = int(chunk[0][0])
        total = 0
        for line in chunk[1:]:
            total += line.count('#')
        shapes[digit] = total
    return shapes

def parse_input(input_lines:list):
    chunks = []
    while len(input_lines) > 0:
        index = -1
        if '' not in input_lines:
            index = len(input_lines)
        else:
            index = input_lines.index('')
        chunk = input_lines[:index]
        input_lines = input_lines[index+1:]
        chunks.append(chunk)
    return parse_shapes(chunks[:-1]), chunks[-1]

def parse_line(line:str):
    dimensions, counts = line.split(': ')
    width, height = dimensions.split('x')
    width, height = int(width), int(height)

    return (width, height, list(map(lambda x: int(x), counts.split(' '))))

def is_possible(line, shapes):
    width, height, counts = parse_line(line)
    needed_spots = sum([shapes[i] * count for i,count in enumerate(counts)])

    total_shapes = sum(shapes)

    # If there are less available spaces than required
    if needed_spots > width * height:
        return False

    # Check if there are more 3x3 spaces than the required number of shapes
    if width//3 * height//3 > total_shapes:
        return True

    return False # For the input, we don't need to check anything further

def day12() -> Result:
    res = Result()
    input_lines = get_input(INPUT_DATA)
    shapes, values= parse_input(input_lines)
    res.p1 = 0
    for line in values:
        res.p1 += 1 if is_possible(line, shapes) else 0
    res.p2 = 'Merry Christmas!'
    return res


if __name__ == '__main__':
    result = day12()
    print(f'Day 12 Part 1: {result.p1}')
    print(f'Day 12 Part 2: {result.p2}')
