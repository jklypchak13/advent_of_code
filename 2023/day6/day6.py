import sys


def breaks_record(hold_time, race_time, record):
    return (race_time - hold_time) * hold_time > record


def count_ways(time, record):
    # Binary Search For lowest element
    low, high = 0, time // 2
    current_time = (high + low) // 2
    while breaks_record(current_time - 1, time, record) == breaks_record(current_time + 1, time, record):
        if breaks_record(current_time, time, record):
            high = current_time
        else:
            low = current_time
        current_time = (high + low) // 2
    smallest_time = current_time if breaks_record(current_time, time, record) else current_time + 1

    # Binary Search for highest element
    low, high = time // 2, time
    current_time = (high + low) // 2
    while breaks_record(current_time - 1, time, record) == breaks_record(current_time + 1, time, record):
        if breaks_record(current_time, time, record):
            low = current_time
        else:
            high = current_time

        current_time = (high + low) // 2
    highest_time = current_time if breaks_record(current_time, time, record) else current_time - 1

    # May not need highest time, but could use smallest to determine highest?
    assert highest_time == time - smallest_time
    return highest_time - smallest_time + 1


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('Need args')
        sys.exit(-1)
    data = ''
    with open(sys.argv[1], 'r') as fp:
        data = fp.read()

    lines = data.split('\n')

    samples = []
    for i, (time, record) in enumerate(zip(lines[0].split(), lines[1].split())):
        if i != 0:
            samples.append((int(time), int(record)))

    part_two_time = int(''.join(lines[0].split(':')[1].split()))
    part_two_record = int(''.join(lines[1].split(':')[1].split()))
    total = 1

    for t, r in samples:
        total *= count_ways(t, r)

    print(f'Part One Answer: {total}')
    print(f'Part Two Answer: {count_ways(part_two_time, part_two_record)}')
