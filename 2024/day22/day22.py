from collections import defaultdict
from shared.types import Result
from shared.input import get_input

INPUT_DATA = "day22/input.txt"
SAMPLE_DATA = "day22/sample.txt"

Sequence = tuple[int,int,int,int]

def take_step(secret:int)->int:
    PRUNE = 16777216
    secret = (secret ^ (secret * 64)) % PRUNE
    secret = (secret ^ (secret // 32)) % PRUNE
    secret = (secret ^ (secret *2048 )) % PRUNE
    return secret

def simulate_trader(secret:int)->tuple[int, dict[Sequence, int]]:
    sequence_profits = {}
    changes = []
    for _ in range(2000):
        new_secret = take_step(secret)
        changes.append(new_secret % 10 - secret % 10)
        if len(changes) >= 4:
            seq = tuple(changes[-4:])
            if seq not in sequence_profits:
                sequence_profits[seq] = new_secret % 10
        secret = new_secret
    return secret, sequence_profits

def day22() -> Result:
    res = Result()
    lines = get_input(INPUT_DATA)

    res.p1 = 0
    total_profits = defaultdict(int)
    for line in lines:
        secret = int(line)
        secret_number, profits = simulate_trader(secret)
        res.p1 += secret_number
        for sequence, profit in profits.items():
            total_profits[sequence] += profit
    res.p2 = max(total_profits.values())

    return res


if __name__ == '__main__':
    result = day22()
    print(f'Day 22 Part 1: {result.p1}')
    print(f'Day 22 Part 2: {result.p2}')
