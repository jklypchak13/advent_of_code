import sys


def get_score(wins):
    score = 0
    if (wins > 0):
        score = 1
    for j in range(wins - 1):
        score *= 2
    return score


def make_set(string):
    result = set()
    for value in string.split(' '):
        if value != '':
            result.add(value)
    return result


def get_win_count(line):
    # Remove card label
    line = line.split(': ')[1]

    # Get the two sets of numbers
    winning_numbers = make_set(line.split('|')[0])
    my_numbers = make_set(line.split('|')[1])

    return len(my_numbers.intersection(winning_numbers))


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('Need arguments')
        sys.exit(-1)

    # Get Data
    data = []
    with open(sys.argv[1], 'r') as fp:
        data = fp.readlines()

    part_one_answer, part_two_answer = 0, 0
    multiplier = [1 for i in range(len(data))]
    for i, line in enumerate(data):
        wins = get_win_count(line.strip())
        part_one_answer += get_score(wins)

        # Copy the next WINS tickets
        for offset in range(wins):
            if i + offset + 1 < len(multiplier):
                multiplier[i + offset + 1] += multiplier[i]

    part_two_answer = sum(multiplier)

    print(f'Part One Answer: {part_one_answer}')
    print(f'Part Two Answer: {part_two_answer}')
