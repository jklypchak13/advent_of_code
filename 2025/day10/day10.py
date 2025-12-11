from aoc_utils.types import Result
from aoc_utils.input import get_input
import numpy as np
from scipy.optimize import linprog
from functools import cache

INPUT_DATA = "day10/input.txt"
SAMPLE_DATA = "day10/sample.txt"

def parse_line(line):
    first_end = line.index(']') + 1
    switches = line[:first_end]
    line = line[first_end+1:]
    second_end = line.index('{')-1
    buttons = line[:second_end]
    joltage = line[second_end+1:]
    switches = switches[1:-1]
    target = tuple([0 if c == '.' else 1 for c in switches])
    joltage = joltage[1:-1]
    joltage_target = tuple(int(value) for value in joltage.split(','))
    ret_buttons = []
    button_values = buttons.split(' ')
    for button in button_values:
        values = button[1:-1]
        ret_buttons.append(tuple([int(value) for value in values.split(',')]))
    return target, ret_buttons, joltage_target


def apply_button(state, option):
    for idx in option:
        if state[idx] == 1:
            state = state[0:idx] +  (0,) + state[idx+1:]
        else:
            state = state[0:idx] +  (1,) + state[idx+1:]
    return state

@cache
def min_buttons_pressed(state, target, buttons):
    if state == target:
        return 0

    # No buttons left to press
    if len(buttons) == 0:
        return len(state) + len(target)

    #Try to press the button
    new_state = apply_button(state, buttons[0])
    best_with_press = min_buttons_pressed(new_state, target, buttons[1:])

    #Try to not press the button
    best_with_no_press = min_buttons_pressed(state, target, buttons[1:])

    return min(best_with_press+1, best_with_no_press)


def solve_line_toggle(line):
    target, options, _ = parse_line(line)
    state = tuple(0 for _ in target)
    options = tuple(options)
    return min_buttons_pressed(state, target, options)

def create_matrix(buttons, rows):
    a = np.zeros([rows, len(buttons)])
    for i, button in enumerate(buttons):
        for idx in button:
            a[idx,i] = 1
    return a

def solve_line_joltage(line):
    _, options, target = parse_line(line)
    buttons = create_matrix(options, len(target))
    res = linprog([1] * buttons.shape[1], A_eq=buttons, b_eq=target, bounds=(0,None), method="highs", integrality=True)
    return round(res.fun)

def day10() -> Result:
    res = Result()
    input_lines = get_input(INPUT_DATA)
    res.p1 = 0
    res.p2 = 0
    for line in input_lines:
        res.p1 += solve_line_toggle(line)
        res.p2 += solve_line_joltage(line)
    return res


if __name__ == '__main__':
    result = day10()
    print(f'Day 10 Part 1: {result.p1}')
    print(f'Day 10 Part 2: {result.p2}')
