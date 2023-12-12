import sys


def get_cards_jokers():
    cards = ['J']
    cards.extend([f'{i}' for i in range(10)])
    cards.extend(['T', 'Q', 'K', 'A'])
    return {card: i for i, card in enumerate(cards)}


def get_cards():
    cards = [f'{i}' for i in range(10)]
    cards.extend(['T', 'J', 'Q', 'K', 'A'])
    return {card: i for i, card in enumerate(cards)}


def get_rank(hand, jokers):
    counts = {c: hand.count(c) for c in set(hand)}

    joker_count = 0
    if jokers and 'J' in counts.keys() and len(counts.keys()) > 1:
        joker_count = counts['J']
        counts['J'] = 0
    values = sorted(counts.values())
    values[len(values) - 1] += joker_count

    if 5 in values:
        return 6
    if 4 in values:
        return 5
    if 3 in values and 2 in values:
        return 4
    if 3 in values:
        return 3
    if values.count(2) == 2:
        return 2
    if 2 in values:
        return 1
    return 0


def score_hand(hand, jokers=False):
    cards = get_cards_jokers() if jokers else get_cards()
    score = get_rank(hand, jokers)
    for card in hand:
        score = score * len(cards) + cards[card]
    return score


def get_total(hands, jokers=False):
    score = 0
    for i, hand in enumerate(sorted(hands, key=lambda hand: score_hand(hand[0], jokers))):
        score += (i + 1) * hand[1]
    return score


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('Need arguments')
        sys.exit(-1)

    # Get Data
    lines = []
    with open(sys.argv[1], 'r') as fp:
        lines = fp.read().split('\n')

    hands = [(line.split(' ')[0], int(line.split(' ')[1])) for line in lines]

    p1_cards = get_cards()
    p2_cards = get_cards_jokers()

    print(f'Part One Answer: {get_total(hands)}')
    print(f'Part Two Answer: {get_total(hands, jokers=True)}')
