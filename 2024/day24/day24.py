from shared.types import Result
from shared.input import get_input

INPUT_DATA = "day24/input.txt"
SAMPLE_DATA = "day24/sample.txt"

def get_starting_state(lines)->dict:
    state = {}
    for line in lines:
        name, value = line.split(': ')
        state[name] = int(value)
    return state

def calculate_state(a,b,op):
    if op == 'XOR':
        return a ^ b
    if op == 'OR':
        return a | b
    return a & b
    

def solve_equations(wire_state, equations:dict[str, tuple]):
    while len(equations) > 0:
        remove = set()
        for key, eq in equations.items():
            a, b, op = eq
            if a in wire_state and b in wire_state:
                wire_state[key] = calculate_state(wire_state[a],wire_state[b],op)
                remove.add(key)
        for key in remove:
            equations.pop(key)
    return wire_state
        

def get_equations(lines):
    equations = {}
    for line in lines:
        values = line.split(' ')
        dest = values[-1]
        a = values[0]
        op = values[1]
        b = values[2]
        equations[dest] = (a, b, op)
    return equations
    
def get_char_int(wire_state, char):
    keys = filter(lambda x: x.startswith(char), wire_state.keys())
    result = ''
    for key in sorted(keys, reverse=True):
        result += str(wire_state[key])
    return int(result, base=2)

def simulate(wire_state, equations):
    wire_state = solve_equations(wire_state, equations)
    return get_char_int(wire_state, 'z')
    
def day24() -> Result:
    res = Result()
    data = ''
    with open(INPUT_DATA, 'r') as fp:
        data = fp.read()
    starting, values = data.split('\n\n')
    wire_state = get_starting_state(starting.split('\n'))
    equations = get_equations(values.split('\n'))
    res.p1 = simulate(wire_state, equations)
    res.p2 = 'Done by manual analysis, good luck :)'

    return res


if __name__ == '__main__':
    result = day24()
    print(f'Day 24 Part 1: {result.p1}')
    print(f'Day 24 Part 2: {result.p2}')
