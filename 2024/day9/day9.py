from shared.types import Result
from shared.input import get_input

INPUT_DATA = "day9/input.txt"
SAMPLE_DATA = "day9/sample.txt"


class Block:

    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __len__(self):
        return self.end - self.start

    def get_checksum(self, value):
        sum = 0
        for i in range(self.start, self.end):
            sum += i * value
        return sum


def expand_input(line):
    empty_spaces = []
    spaces = []
    value = 0
    free = False
    index = 0
    for c in line:
        count = int(c)
        if free:
            for i in range(count):
                empty_spaces.append(index)
                spaces.append('.')
                index += 1
        else:
            for i in range(count):
                spaces.append(value)
                index += 1
            value += 1
        free = not free
    return spaces, empty_spaces


def shift(spaces, empty_spaces: list[int]):
    index = len(spaces) - 1
    while len(empty_spaces) > 0:
        needs_filled = empty_spaces.pop(0)
        while spaces[index] == '.':
            index -= 1
        if needs_filled > index:
            break
        spaces[needs_filled] = spaces[index]
        spaces[index] = '.'
    return spaces


def get_checksum(line: str):
    count = 0
    for i in range(len(line)):
        c = line[i]
        if c == '.':
            break
        count += i * int(c)
    return count


def move_chunks(input):
    values, empty_spaces = expand_input(input)
    shifted = shift(values, empty_spaces)
    return get_checksum(shifted)


def calculate_blocks(input):
    empty_blocks = []
    file_chunks = {}
    free = False
    index = 0
    value = 0
    for c in input:
        count = int(c)
        block = Block(index, index + count)
        if free:
            empty_blocks.append(block)
        else:
            file_chunks[value] = block
            value += 1
        index += count
        free = not free
    return file_chunks, empty_blocks


def get_files_checksum(files: dict[int, Block]):
    count = 0
    for value, block in files.items():
        count += block.get_checksum(value)
    return count


def find_free_block(file_block, free_blocks):
    for free_block in free_blocks:
        if len(free_block) >= len(file_block) and free_block.start < file_block.start:
            return free_block
    return None


def shift_file(file_block, free_blocks: list[Block]):
    free_block = find_free_block(file_block, free_blocks)
    if free_block is None:
        return
    file_block.end = free_block.start + len(file_block)
    file_block.start = free_block.start
    if len(file_block) == len(free_block):
        free_blocks.remove(free_block)
    else:
        free_block.start = free_block.start + len(file_block)


def move_files(input):
    files, free_blocks = calculate_blocks(input)
    last_file = max(files.keys())
    # Attempt to shift each file to the left
    for i in range(last_file, 0, -1):
        shift_file(files[i], free_blocks)
    sum = get_files_checksum(files)
    return sum


def day9() -> Result:
    res = Result()
    input = get_input(INPUT_DATA)[0]
    res.p1 = move_chunks(input)
    res.p2 = move_files(input)
    return res


if __name__ == '__main__':
    result = day9()
    print(f'Day 9 Part 1: {result.p1}')
    print(f'Day 9 Part 2: {result.p2}')
