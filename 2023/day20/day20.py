import sys


RX_ON = 0


def load_modules(lines):
    modules = {}
    for line in lines:
        name = line.split(' -> ')[0]
        destinations = line.split(' -> ')[1].split(', ')
        typ = name[0]
        if name == 'broadcaster':
            name = 'bbroadcaster'
        modules[name[1:]] = [typ, destinations, 0]
        if typ == '&':
            modules[name[1:]][2] = {}

    return modules


def load_conjunctions(modules):
    for name in modules:
        if modules[name][0] != '&':
            continue
        for other_name in modules:
            if other_name == name:
                continue
            if name in modules[other_name][1]:
                modules[name][2][other_name] = 0


def process_signal(signal, module, name, src):
    typ, destinations, state = module

    if name == 'rx' and signal == 0:
        RX_ON = True
    res = None
    if typ == '%':
        if signal == 1:
            return []
        if state == 0:
            module[2] = 1
            res = 1
        else:
            module[2] = 0
            res = 0
    elif typ == '&':
        module[2][src] = signal
        if sum(module[2].values()) == len(module[2].values()):
            res = 0
        else:
            res = 1
    else:
        # broadcaster
        res = 0
    result = [(res, destination, name) for destination in destinations]
    return result


def count_signals(modules):
    signals = [(0, 'broadcaster', 'button')]
    low_count = 0
    high_count = 0

    while len(signals) > 0:
        signal, destination, src = signals.pop(0)
        module = modules[destination] if destination in modules else None
        if signal == 0:
            low_count += 1
        else:
            high_count += 1

        if module is not None:
            signals.extend(process_signal(signal, module, destination, src))

    return low_count, high_count


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('Need arguments')
        sys.exit(-1)

    # Get Data
    lines = []
    with open(sys.argv[1], 'r') as fp:
        lines = fp.read().split('\n')

    modules = load_modules(lines)

    load_conjunctions(modules)
    low, high = 0, 0
    for i in range(1000):
        current_low, current_high = count_signals(modules)
        low += current_low
        high += current_high
    print(f'Part One Answer: {low * high}')
    print(f'Part Two Answer: {0}')
