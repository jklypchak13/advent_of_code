from shared.types import Result
from shared.input import get_input

INPUT_DATA = "day25/input.txt"
SAMPLE_DATA = "day25/sample.txt"

Heights = list[int,int,int,int,int]

def find_depths(schematic:list[str])->Heights:
    depths = [0] * 5
    for i in range(0, len(schematic[0])):
        count = 0
        for j in range(len(schematic)):
            if schematic[j][i] == '#':
                count += 1
        depths[i] = count - 1
    return depths
            
def parse_schematics(schematics: list[str])->tuple[Heights, Heights]:
    keys, locks = [], []

    for schematic in schematics:
        if schematic[0] == '#':
            locks.append(find_depths(schematic.split('\n')))
        else:
            keys.append(find_depths(schematic.split('\n')))
    return keys, locks
        
def compare(key:Heights, lock:Heights)->bool:
    for a, b in zip(key,lock):
        if a + b >= 6:
            return False
    return True

def day25() -> Result:
    res = Result()
    data = ''
    with open(INPUT_DATA, 'r') as fp:
        data = fp.read()
    schematics = data.split('\n\n')
    keys, locks = parse_schematics(schematics)
    res.p1 = 0
    for key in keys:
        for lock in locks:
            res.p1 += 1 if compare(key, lock) else 0
    res.p2 = 'Merry Christmas'
    return res


if __name__ == '__main__':
    result = day25()
    print(f'Day 25 Part 1: {result.p1}')
    print(f'Day 25 Part 2: {result.p2}')
