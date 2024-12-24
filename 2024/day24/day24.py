from shared.types import Result

INPUT_DATA = "day24/input.txt"
SAMPLE_DATA = "day24/sample.txt"

Gate = tuple[int, int, str]

def get_starting_gates(lines:list[str])->dict[str, Gate]:
    state = {}
    for line in lines:
        name, value = line.split(': ')
        state[name] = int(value)
    return state

def calculate_state(a:int,b:int,op:str)->int:
    if op == 'XOR':
        return a ^ b
    if op == 'OR':
        return a | b
    return a & b
    

def add_gates(gates:dict[str, Gate], lines:list[str])->dict[str, Gate]:
    for line in lines:
        values = line.split(' ')
        dest = values[-1]
        a = values[0]
        op = values[1]
        b = values[2]
        gates[dest] = (a, b, op)
    return gates

def solve(gates:dict[str, Gate], gate:str)->int:
    if type(gates[gate]) == int:
        return gates[gate]
    a, b, op = gates[gate]
    return calculate_state(solve(gates, a), solve(gates, b), op)
    
def find_char(gates:dict[str, Gate], char:str='z')->int:
    result = {}
    for gate in gates:
        if not gate.startswith(char):
            continue
        result[gate] = solve(gates, gate)
    res = ''
    for gate in sorted(result.keys())[::-1]:
        res += str(result[gate])
    return int(res, base=2)

def print_gate(gates, gate:str, depth=0, maxdepth=4):
    if depth > maxdepth:
        return
    line = ' ' * depth
    current = gates[gate]
    if type(current) == int:
        line += gate
        print(line)
        return
    line += f'{gate} = '
    a,b,op = current
    line += f'{a} {op} {b}'
    print(line)
    print_gate(gates, a, depth+1)
    print_gate(gates, b, depth+1)

def find_bad_bit(gates:dict[str, Gate])->int:
    x = find_char(gates, 'x')
    y = find_char(gates, 'y')
    z = find_char(gates, 'z')
    actual = bin(z)
    expected = bin(x + y)
    for i in range(len(actual)-1, -1, -1):
        if actual[i] != expected[i]:
            return len(actual)-1 - i
    return -1


def find_non_xor_outputs(gates:dict[str, Gate])->list[Gate]:
    result = []
    for gate in gates:
        if not gate.startswith('z'):
            continue
        if 'XOR' not in gates[gate]:
            result.append(gate)
    return result
    
def debug_bit(gates:dict[str, Gate], bit:int ):
    print_gate(gates, f'z{bit-1}')
    print('---')
    print_gate(gates, f'z{bit}')
    print('---')
    print_gate(gates, f'z{bit+1}')
    
def day24() -> Result:
    res = Result()
    data = ''
    with open(INPUT_DATA, 'r') as fp:
        data = fp.read()
    starting, values = data.split('\n\n')
    gates = get_starting_gates(starting.split('\n'))
    gates = add_gates(gates, values.split('\n'))
    res.p1 = find_char(gates, 'z')
    swaps = [
        ('qdg', 'z12'),
        ('z19', 'vvf'),
        ('dck', 'fgn'),
        ('nvh', 'z37')
    ]
    # Apply swaps found so far
    for a,b in swaps:
        gates[a], gates[b] = gates[b], gates[a]

    bad_bit = find_bad_bit(gates)

    # not_xor = find_non_xor_outputs(gates)
    # print(f'None XOR output gates : {not_xor}')
    # print(f'First Incorrect bit: {bad_bit}')
    # debug_bit(gates, 23)

    if bad_bit == -1:
        swapped_gates = []
        for swap in swaps:
            swapped_gates.append(swap[0])
            swapped_gates.append(swap[1])
        res.p2 = ','.join(sorted(swapped_gates))

    return res



if __name__ == '__main__':
    result = day24()
    print(f'Day 24 Part 1: {result.p1}')
    print(f'Day 24 Part 2: {result.p2}')
