from aoc_utils.types import Result
from aoc_utils.input import get_input
from collections import defaultdict

INPUT_DATA = "day7/input.txt"
SAMPLE_DATA = "day7/sample.txt"

def count_timelines(lines):
    start = lines[0].index('S')
    splits = 0
    prev_active_particles = defaultdict(int)
    prev_active_particles[start] = 1
    for row in lines[1:]:
        new_active_particles = defaultdict(int)
        for i, current in enumerate(row):
            if i not in prev_active_particles:
                continue
            particle_count = prev_active_particles[i]
            if current == '.':
                new_active_particles[i] += particle_count
            elif current == '^':
                splits += 1
                new_active_particles[i-1] += particle_count
                new_active_particles[i+1] += particle_count
        prev_active_particles = new_active_particles
    return splits, sum(prev_active_particles.values())

def day7() -> Result:
    res = Result()
    lines = get_input(INPUT_DATA)
    res.p1, res.p2 = count_timelines(lines)
    return res


if __name__ == '__main__':
    result = day7()
    print(f'Day 7 Part 1: {result.p1}')
    print(f'Day 7 Part 2: {result.p2}')
