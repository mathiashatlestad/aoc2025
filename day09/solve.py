"""
Advent of Code 2025 - Day 9
"""

import sys; from pathlib import Path; sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from utils.aoc import run_solution

def area(p1: tuple[int, int], p2: tuple[int, int]) -> float:
    return (1 + abs(p1[0] - p2[0])) * (1 + abs(p1[1] - p2[1]))

def part1(data: list[tuple[int, int]]) -> int:
    areas = []
    for i, point1 in enumerate(data):
        for j, point2 in enumerate(data):
            if i < j:
                areas.append((area(point1, point2), point1, point2))
    sorted_areas = sorted(areas, key=lambda x: x[0])
    return sorted_areas[-1][0]


def part2(data: list[str]) -> int:
    """Solve part 2 of the puzzle."""
    # TODO: Implement solution
    return 0

if __name__ == '__main__':
    run_solution(part1, part2, transform_input=lambda x: [tuple(map(int, line.split(','))) for line in x.split('\n')])

