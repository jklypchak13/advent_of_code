from aoc_utils.types import Result
from aoc_utils.input import get_input

from functools import cache

INPUT_DATA = "day11/input.txt"
SAMPLE_DATA = "day11/sample.txt"
SAMPLE_DATA_2 = "day11/sample2.txt"

class Graph:

    def __init__(self, lines):
        self.graph = {}
        self.init_graph(lines)

    def init_graph(self, lines):
        for line in lines:
            node, edges = line.split(': ')
            edges = tuple(edges.split(' '))
            self.graph[node] = edges
        # Output has no edges
        self.graph['out'] = []

    @cache
    def count_paths(self, start, dest):
        if start == dest:
            return 1
        return sum(self.count_paths(node, dest) for node in self.graph[start])

def count_paths_with_stops(graph:Graph, nodes:list[str]):
    total = 1
    for i in range(len(nodes)-1):
        start, dest = nodes[i], nodes[i+1]
        total *= graph.count_paths(start, dest)
    return total

def count_svr_paths(graph:Graph):
    return count_paths_with_stops(graph, ['svr', 'fft', 'dac', 'out']) + count_paths_with_stops(graph, ['svr', 'dac', 'fft', 'out'])

def day11() -> Result:
    res = Result()
    graph = Graph(get_input(INPUT_DATA))
    res.p1 = graph.count_paths('you', 'out')
    res.p2 = count_svr_paths(graph)
    return res

if __name__ == '__main__':
    result = day11()
    print(f'Day 11 Part 1: {result.p1}')
    print(f'Day 11 Part 2: {result.p2}')
