
from get_days import get_days

functions = get_days()
for i in range(len(functions)):
    res = functions[i]()
    print('-' * 10)
    print(f'Day {i+1} Part 1: {res.p1}')
    print(f'Day {i+1} Part 2: {res.p2}')
    print('-' * 10)
