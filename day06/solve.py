"""
Advent of Code 2025 - Day 6
"""

import sys; from pathlib import Path; sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from utils.aoc import run_solution


def part1(data: list[str]) -> int:
    data = [line.split() for line in data if line]
    count = 0
    for j in range(0, len(data[0])):
        partly = 0
        if data[-1][j] == "*": 
            partly = 1
        for i in range(0, len(data)-1):
            if data[-1][j] == "*":
                partly*=int(data[i][j])
            elif data[-1][j] == "+":
                partly+=int(data[i][j])
        count+=partly

    return count


def part2(data: list[str]) -> int:
    """Solve part 2 of the puzzle."""
    # TODO: Implement solution
    return 0


if __name__ == '__main__':
    run_solution(part1, part2, transform_input=lambda x: x.split('\n'))

