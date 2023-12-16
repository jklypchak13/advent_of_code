import sys


def hash(ins):
    current_value = 0
    for c in ins:
        current_value += ord(c)
        current_value *= 17
        current_value = current_value % 256
    return current_value


def process_deletion(buckets, key):
    bucket = buckets[hash(key)]
    for i in range(len(bucket)):
        if bucket[i][0] == key:
            bucket.pop(i)
            return


def process_insertion(buckets, key, value):
    bucket = buckets[hash(key)]
    for i in range(len(bucket)):
        if bucket[i][0] == key:
            bucket[i] = (key, value)
            return
    bucket.append((key, value))


def part_two(instructions):
    buckets = []
    for _ in range(256):
        buckets.append([])

    for instruction in instructions:
        if '-' in instruction:
            process_deletion(buckets, instruction.split('-')[0])
        else:
            data = instruction.split('=')
            process_insertion(buckets, data[0], data[1])
    total = 0
    for start, box in enumerate(buckets):
        for i, (_, value) in enumerate(box):
            print(_, box)
            total += (start + 1) * (i + 1) * int(value)
    return total


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('Need arguments')
        sys.exit(-1)

    # Get Data
    data = []
    with open(sys.argv[1], 'r') as fp:
        data = fp.read().split(',')

    total = 0
    for ins in data:
        total += hash(ins)
    part_two_total = part_two(data)
    print(f'Part One Answer: {total}')
    print(f'Part Two Answer: {part_two_total}')
