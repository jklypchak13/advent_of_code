from shared.types import Result
from shared.input import get_input
from shared.grid import Grid
from functools import cache

INPUT_DATA = "day21/input.txt"
SAMPLE_DATA = "day21/sample.txt"
NUMPAD = Grid(lambda: '', '789\n456\n123\n 0A'.split('\n'))
KEYPAD = Grid(lambda: '', ' ^A\n<v>'.split('\n'))
DIR_MAP = {
    (-1, 0): '^',
    (1, 0): 'v',
    (0, -1): '<',
    (0, 1): '>',
}
Point = tuple[int,int]

def find_char(grid:Grid, character:str)-> Point:
    for pos, value in grid.items():
        if value == character:
            return pos

def shortest_path(start_char:str, end_char:str, use_numpad:bool)->list[str]:
    grid = NUMPAD if use_numpad else KEYPAD
    paths = []
    path_len = float('infinity')

    start_pos = find_char(grid, start_char)
    end_pos = find_char(grid, end_char)
    needs_eval = [(start_pos, '')]
    while len(needs_eval):
        current, path = needs_eval.pop(0)

        # Doing BFS, so once we try a longer path we can stop
        if len(path) > path_len:
            return paths
        
        if current == end_pos:
            path_len = len(path)
            paths.append(path + 'A')
        
        for dx, dy in DIR_MAP.keys():
            neighbor = current[0] + dx, current[1] + dy
            if neighbor not in grid or grid[neighbor] == ' ':
                continue
            needs_eval.append((neighbor, path + DIR_MAP[dx,dy]))
    return paths

@cache
def find_shortest_path(line:str, steps:int, num_pad:bool)->int:
    res = 0
    line = "A" + line
    for i in range(len(line)-1):
        paths = shortest_path(line[i], line[i+1], num_pad)
        if steps == 0:
            res += len(min(paths, key=len))
        else:
            best = float('infinity')
            for path in paths:
                length = find_shortest_path(path, steps-1, False)
                best = min(best, length)
            res += best
    return res

def get_numeric_value(data:str):
    return int(data[:-1])
    
    
def day21() -> Result:
    res = Result()
    input = get_input(INPUT_DATA)
    res.p1, res.p2 = 0, 0
    for line in input:
        res.p1 += find_shortest_path(line, 2, True)  * get_numeric_value(line)
        res.p2 += find_shortest_path(line, 25, True) * get_numeric_value(line)
    return res


if __name__ == '__main__':
    result = day21()
    print(f'Day 21 Part 1: {result.p1}')
    print(f'Day 21 Part 2: {result.p2}')
