
def get_input(path: str):
    lines = []
    with open(path, 'r') as fp:
        lines = fp.read().split('\n')
    return lines
