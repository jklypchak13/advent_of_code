from shared.types import Result
from shared.input import get_input_grid, Grid

INPUT_DATA = "day12/input.txt"
SAMPLE_DATA = "day12/sample.txt"

Point = tuple[int, int]
# Represent a border as interior point and exterior point it divides
Boundary = tuple[Point, Point]

DIRECTIONS = [(-1, 0), (1, 0), (0, 1), (0, -1)]


def get_neighbors(position: Point) -> list[Point]:
    neighbors = []
    for dx, dy in DIRECTIONS:
        new_position = position[0] + dx, position[1] + dy
        neighbors.append(new_position)
    return neighbors


def get_connected_component(grid: Grid, root: Point) -> set[Point]:
    visited = set()
    needs_eval = [root]
    while len(needs_eval) > 0:
        current = needs_eval.pop(0)
        if current in visited:
            continue
        visited.add(current)
        potential = get_neighbors(current)
        matching = filter(lambda x: grid[x] == grid[current], potential)
        needs_eval.extend(matching)
    return visited


def compute_components(grid: Grid) -> list[set[Point]]:
    connected_components = []
    needs_eval = set(grid.keys())

    # Remove the first element, and find the connected components
    while len(needs_eval) > 0:
        current = needs_eval.pop()
        component = get_connected_component(grid, current)
        needs_eval = needs_eval.difference(component)
        connected_components.append(component)
    return connected_components


def get_edge_locations(grid: Grid, component: set[Point]) -> set[Boundary]:
    edges = set()
    for point in component:
        value = grid[point]
        neighbors = get_neighbors(point)
        for neighbor in neighbors:
            if value != grid[neighbor]:
                edges.add((point, neighbor))
    return edges


def get_walls(grid: Grid, component: set[Point]) -> set[Boundary]:
    """Get the list of walls around a component. 

        For a horizontal wall, it is represented as the rightmost Boundary
        e.g:              v
                -----------

        For a vertical wall, it is represented as the highest Boundary
        e.g: 
            | <
            |
            |
            |

            so for a square, it would be represented by these
                 v
            ------
           >|    | <
            |    |
            |    |
            |    |
            |    | 
            ------
                 ^
    """
    edges = get_edge_locations(grid, component)
    walls = set()
    for edge in edges:
        inside = edge[0]
        outside = edge[1]
        include = True
        # Check the boundary to the right and above. if either is present, this is doesn't represent a wall
        for dx, dy in [(0, 1), (-1, 0)]:
            new_inside = inside[0] + dx, inside[1] + dy
            new_outside = outside[0] + dx, outside[1] + dy
            if (new_inside, new_outside) in edges:
                include = False
        if include:
            walls.add(edge)
    return walls


def calculate_score(grid: Grid, component: set[Point]) -> int:
    return len(component) * len(get_edge_locations(grid, component))


def calculate_discount_score(grid: Grid, component: set[Point]) -> int:
    return len(component) * len(get_walls(grid, component))


def day12() -> Result:
    res = Result()
    input = get_input_grid(INPUT_DATA)
    components = compute_components(input)
    res.p1, res.p2 = 0, 0
    for component in components:
        res.p1 += calculate_score(input, component)
        res.p2 += calculate_discount_score(input, component)
    return res


if __name__ == '__main__':
    result = day12()
    print(f'Day 12 Part 1: {result.p1}')
    print(f'Day 12 Part 2: {result.p2}')
