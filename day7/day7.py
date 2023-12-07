import sys


def get_cards():
    cards = [f'{i}' for i in range(10)]
    cards.extend(['T', 'J', 'Q', 'K', 'A'])
    return cards


def get_part_two_cards():
    cards = ['J']
    cards.extend([f'{i}' for i in range(10)])
    cards.extend(['T', 'Q', 'K', 'A'])
    return cards


def score_hand(hand, jokers=False):
    counts = {}
    for char in hand:
        if char not in counts:
            counts[char] = 0
        counts[char] += 1
    score = 0

    joker_count = 0
    if jokers and 'J' in counts.keys() and len(counts.keys()) > 1:
        joker_count = counts['J']
        counts['J'] = 0

    values = sorted(counts.values())
    values[len(values) - 1] += joker_count
    for count in values:
        score += count ** 2
    return score


def load_hands(lines, jokers=False):
    result = {}
    for line in lines:
        hand = line.split(' ')[0]
        bet = line.split(' ')[1]
        score = 0
        if jokers:
            score = score_hand(hand, jokers)
        else:
            score = score_hand(hand, jokers)
        if score not in result:
            result[score] = []
        result[score].append((hand, bet))
    return result


def get_total(hands, cards):
    # Comparator for sorting cards
    def hand_key(x):
        res = 0
        for c in x[0]:
            res += res * len(cards) + cards.index(c)
        return res

    total_hands = 1
    score = 0

    for base in sorted(hands.keys()):
        values = hands[base]
        while len(values):
            current = min(values, key=hand_key)
            values.remove(current)
            score += total_hands * int(current[1])
            total_hands += 1
    return score


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('Need arguments')
        sys.exit(-1)

    # Get Data
    data = ''
    with open(sys.argv[1], 'r') as fp:
        data = fp.read()
    lines = data.split('\n')

    p1_cards = get_cards()
    p2_cards = get_part_two_cards()
    print(f'Part 1 Answer: {get_total(load_hands(lines, jokers=False), p1_cards)}')
    print(f'Part 2 Answer: {get_total(load_hands(lines, jokers=True), p2_cards)}')
