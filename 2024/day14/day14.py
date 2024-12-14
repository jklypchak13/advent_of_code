from shared.types import Result
from shared.input import get_input
from shared.grid import get_adj4, get_adj8
from collections import defaultdict

INPUT_DATA = "day14/input.txt"
SAMPLE_DATA = "day14/sample.txt"

SAMPLE_GRID_SIZE = 11, 7
GRID_SIZE = 101, 103

Point = tuple[int, int]


def parse_value(data: str) -> tuple[int, int]:
    x = int(data.split(',')[0])
    y = int(data.split(',')[1])
    return x, y


class Robot:
    def __init__(self, line: str):
        values = line.split(' ')
        self.pos = parse_value(values[0][2:])
        self.vel = parse_value(values[1][2:])

    def __repr__(self):
        return f'(Position: {self.pos}, Velocity: {self.vel})'

    def take_step(self):
        x, y = self.pos[0] + self.vel[0], self.pos[1] + self.vel[1]
        self.pos = x % GRID_SIZE[0], y % GRID_SIZE[1]

    def get_quadrant(self) -> int:
        mid_x = GRID_SIZE[0] // 2
        mid_y = GRID_SIZE[1] // 2
        x, y = self.pos
        if x < mid_x and y < mid_y:
            return 0
        if x < mid_x and y > mid_y:
            return 1
        if x > mid_x and y < mid_y:
            return 2
        if x > mid_x and y > mid_y:
            return 3
        return 4


def get_positions(robots: list[Robot]) -> set[Point]:
    positions = set()
    for robot in robots:
        positions.add(robot.pos)
    return positions


def check_for_tree(robots: list[Robot]) -> bool:
    # Tried a few other approaches, but waiting until no robots overlap seems to work!
    positions = get_positions(robots)
    if len(robots) == len(positions):
        return True
    return False


def get_safety_score(robots: list[Robot]) -> int:
    positions = [0] * 5
    for robot in robots:
        positions[robot.get_quadrant()] += 1
    score = 1
    for i in range(4):
        score *= positions[i]
    return score


def get_result(robots: list[Robot]) -> Result:
    res = Result()
    for seconds in range(1, 100000):
        for robot in robots:
            robot.take_step()
        if seconds == 100:
            res.p1 = get_safety_score(robots)
        if check_for_tree(robots):
            res.p2 = seconds
            return res
    return res


def day14() -> Result:
    input = get_input(INPUT_DATA)
    robots = []
    for line in input:
        robots.append(Robot(line))
    res = get_result(robots)
    return res


if __name__ == '__main__':
    result = day14()
    print(f'Day 14 Part 1: {result.p1}')
    print(f'Day 14 Part 2: {result.p2}')
