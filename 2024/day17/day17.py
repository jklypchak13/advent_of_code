from shared.types import Result
from shared.input import get_input
from enum import IntEnum

INPUT_DATA = "day17/input.txt"
SAMPLE_DATA = "day17/sample.txt"


class OPCode(IntEnum):
    ADV = 0
    BXL = 1
    BST = 2
    JNZ = 3
    BXC = 4
    OUT = 5
    BDV = 6
    CDV = 7


def parse_input(lines: list[str]) -> tuple[list[int], list[int]]:
    a = int(lines[0].split(': ')[1])
    b = int(lines[1].split(': ')[1])
    c = int(lines[2].split(': ')[1])

    program = lines[4].split(': ')[1]
    program = [int(value) for value in program.split(',')]

    return [a, b, c], program


def get_combo_operand(registers: list[int], operand: int) -> int:
    if operand <= 3:
        return operand
    return registers[operand - 4]


def get_literal_operand(_, operand: int) -> int:
    return operand


def perform_opcode(registers: list[int], opcode: int, operand: int, output: list[int]) -> int:
    match opcode:
        case OPCode.ADV:
            registers[0] = registers[0] // (2**operand)
        case OPCode.BXL:
            registers[1] = registers[1] ^ operand
            pass
        case OPCode.BST:
            registers[1] = operand % 8
            pass
        case OPCode.JNZ:
            if registers[0] != 0:
                return operand
        case OPCode.BXC:
            registers[1] = registers[1] ^ registers[2]
        case OPCode.OUT:
            output.append(operand % 8)
        case OPCode.BDV:
            registers[1] = registers[0] // (2**operand)
        case OPCode.CDV:
            registers[2] = registers[0] // (2**operand)
    return -1


def execute_program(registers: list[int], instructions: list[int]) -> list[int]:
    GET_OPERAND_MAP = {
        OPCode.ADV: get_combo_operand,
        OPCode.BXL: get_literal_operand,
        OPCode.BST: get_combo_operand,
        OPCode.JNZ: get_literal_operand,
        OPCode.BXC: get_literal_operand,
        OPCode.OUT: get_combo_operand,
        OPCode.BDV: get_combo_operand,
        OPCode.CDV: get_combo_operand,
    }
    output = []
    ip = 0
    while ip < len(instructions):
        opcode, operand = instructions[ip], instructions[ip + 1]
        value = GET_OPERAND_MAP[opcode](registers, operand)
        ret = perform_opcode(registers, opcode, value, output)
        ip += 2
        if ret != -1:
            ip = ret
    return output


def get_best_a(program: list[int], position: int, current_a: int) -> int:
    # By manual inspection, each loop iteration mostly looks at the last 3 bits, and then looping is done by dividing by 8
    for attempt in range(8):
        output = execute_program([current_a * 8 + attempt, 0, 0], program)
        if output == program[position:]:
            if position == 0:
                return current_a * 8 + attempt
            res = get_best_a(program, position - 1, current_a * 8 + attempt)
            if res is not None:
                return res
    return None


def find_a_for_program(program):
    return get_best_a(program, len(program) - 1, 0)


def day17() -> Result:
    res = Result()
    lines = get_input(INPUT_DATA)
    registers, program = parse_input(lines)

    result = execute_program(registers, program)
    res.p1 = ','.join([str(val) for val in result])

    res.p2 = find_a_for_program(program)

    return res


if __name__ == '__main__':
    result = day17()
    print(f'Day 17 Part 1: {result.p1}')
    print(f'Day 17 Part 2: {result.p2}')
