from shared.types import Result
from shared.input import get_input

INPUT_DATA = "day23/input.txt"
SAMPLE_DATA = "day23/sample.txt"

Group = tuple[int, ...]
Graph = dict[str, list[str]]


def add_edge(graph:Graph, n1:str, n2:str)->Graph:
    if n1 not in graph:
        graph[n1] = []
    if n2 not in graph:
        graph[n2] = []
    graph[n1].append(n2)
    graph[n2].append(n1)
    return graph

def get_connected_groups(graph:Graph, n:int=None)->list[Group]:
    needs_eval = [ (node,) for node in graph.keys()]

    group = None
    while len(needs_eval) > 0:
        # Peak at the front. if it's a group of n, return
        if n is not None and len(needs_eval[0]) == n:
            return needs_eval

        group = needs_eval.pop(0)
        current = group[-1]

        for neighbor in graph[current]:
            # Make sure that the neighbor comes after me (to avoid duplicate groups)
            if neighbor <= current:
                continue
            # Check to make sure neighbor is connected to every node
            connected = True
            for node in group:
                if node not in graph[neighbor]:
                    connected = False
            if connected:
                needs_eval.append(group + (neighbor,))
    return [group]

def get_t_groups(groups:list[Group])->list[Group]:
    return [group for group in groups if any(filter(lambda x: x.startswith('t'), group))]

def create_graph(lines:list[str])->Graph:
    graph = {}
    for line in lines:
        n1, n2 = line.split('-')
        graph = add_edge(graph, n1, n2)
    return graph

def day23() -> Result:
    res = Result()
    lines = get_input(INPUT_DATA)
    graph = create_graph(lines)

    three_groups = get_connected_groups(graph, 3)
    res.p1 = len(get_t_groups(three_groups))
    res.p2 = ','.join(get_connected_groups(graph)[0])
        
    return res


if __name__ == '__main__':
    result = day23()
    print(f'Day 23 Part 1: {result.p1}')
    print(f'Day 23 Part 2: {result.p2}')
