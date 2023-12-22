import sys


def get_new_ranges(input_range, cond):
    low, high = input_range
    value = int(cond[2:].split(':')[0])
    if '<' in cond:
        # Check if whole range fits criteria
        if low < value and high < value:
            return input_range, None

        # Check if none of the range fits criteria
        if low >= value:
            return None, input_range

        # Split the ranges at the value
        meets_condition = (low, value - 1)
        other = (value, high)

    if '>' in cond:
        # Check if whole range fits criteria
        if low > value and high > value:
            return input_range, None
        # Check if none of the range fits criteria
        if high <= value:
            return None, input_range
        # Split the ranges at the value
        meets_condition = (value + 1, high)
        other = (low, value)
    return meets_condition, other


def sum_table_one(table, _):
    total = 0
    for _, high in table.values():
        total += high
    return total


def sum_table_two(table, _):
    total = 1
    for low, high in table.values():
        total *= high - low + 1
    return total


def build_rule_function(line):

    def process_rule(table, rules):
        res = 0
        current_table = table.copy()
        for cond in line.split(','):
            if '<' in cond or '>' in cond:
                char = cond[0]
                dest = cond.split(':')[1]

                new_range, remaining_range = get_new_ranges(current_table[char], cond)

                if new_range is None:
                    continue
                new_table = current_table.copy()
                new_table[char] = new_range
                res += rules[dest](new_table, rules)

                if remaining_range is None:
                    break
                current_table[char] = remaining_range
            else:
                res += rules[cond](current_table, rules)
        return res
    return process_rule


def parse_rules(lines, part_one=True):
    rules = {}

    for line in lines:
        name = line.split('{')[0]
        conditions = line.split('{')[1][:-1]
        fn = build_rule_function(conditions, )
        rules[name] = fn

    rules['A'] = sum_table_one if part_one else sum_table_two
    rules['R'] = lambda x, y: 0
    return rules


def parse_parts(lines):
    tables = []
    for line in lines:
        table = {}
        line = line[1:-1]
        for assignment in line.split(','):
            letter = assignment.split('=')[0]
            value = assignment.split('=')[1]
            table[letter] = (int(value), int(value))
        tables.append(table)

    return tables


def count_accepted(rules, parts):
    count = 0
    for part in parts:
        current = 'in'
        count += rules[current](part, rules)
    return count


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('Need arguments')
        sys.exit(-1)

    # Get Data
    lines = []
    with open(sys.argv[1], 'r') as fp:
        lines = fp.read().split('\n')

    rule_index = lines.index('')

    part_one_rules = parse_rules(lines[:rule_index], True)
    parts = parse_parts(lines[rule_index + 1:])
    print(f'Part One Answer: {count_accepted(part_one_rules, parts)}')

    part_two_rules = parse_rules(lines[:rule_index], False)
    parts_ranges = [{'x': (1, 4000), 'm': (1, 4000), 'a': (1, 4000), 's': (1, 4000)}]
    print(f"Part Two Answer: {count_accepted(part_two_rules, parts_ranges)}")
