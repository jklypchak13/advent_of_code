from aoc_utils.types import Result
from aoc_utils.input import get_input
from itertools import combinations
import math
from collections import defaultdict

INPUT_DATA = "day8/input.txt"
SAMPLE_DATA = "day8/sample.txt"

def calc_distance(first, second):
    return sum((a-b) ** 2 for a,b in zip(first, second))

def make_junction(value):
    return tuple([int(val) for val in value])

def create_edges(junctions):
    edges = []
    for first, second in combinations(junctions, 2):
        edges.append((calc_distance(first,second), first, second))
    return sorted(edges)

class UnionFind:

    def __init__(self, elements):
        self.parents = {element:element for element in elements}
        self.ranks = {element: 0 for element in elements}
        self.connect_components = len(elements)

    def get_parent(self, element):
        if self.parents[element] != element:
            self.parents[element] = self.get_parent(self.parents[element])
        return self.parents[element]

    def merge(self, first, second):
        p1 = self.get_parent(first)
        p2 = self.get_parent(second)
        if p1 == p2:
            return False
        self.connect_components -= 1
        if self.ranks[p1] > self.ranks[p2]:
            self.parents[p1] = p2
        elif self.ranks[p1] < self.ranks[p2]:
            self.parents[p2] = p1
        else:
            self.parents[p1] = p2
            self.ranks[p2] += 1
        return True

    def get_component_sizes(self):
        component_sizes = defaultdict(int)
        for value in self.parents:
            parent = self.get_parent(value)
            component_sizes[parent] += 1
        return component_sizes

def create_minimum_spanning_tree(edges, union:UnionFind):
    connected_components = union.connect_components
    for _, first, second in edges:
        if union.merge(first, second):
            connected_components -= 1
        if connected_components == 1:
            return first, second
    return None, None

def day8() -> Result:
    res = Result()
    input_lines = get_input(INPUT_DATA)
    junctions = list(map(make_junction, [line.split(',') for line in input_lines]))
    union = UnionFind(junctions)
    edges = create_edges(junctions)
    create_minimum_spanning_tree(edges[0:1000], union)
    sizes = sorted(union.get_component_sizes().values(), reverse=True)
    res.p1 = sizes[0] * sizes[1] * sizes[2]

    first, second = create_minimum_spanning_tree(edges[1000:], union)
    res.p2 = first[0] * second[0]
    return res


if __name__ == '__main__':
    result = day8()
    print(f'Day 8 Part 1: {result.p1}')
    print(f'Day 8 Part 2: {result.p2}')
