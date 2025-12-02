"""
Advent of Code 2025 - Day 1
"""

import sys; from pathlib import Path; sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from utils.aoc import run_solution


def part1(data: list[str]) -> int:
    """Solve part 1 of the puzzle."""
    startNum = 50
    zeros = 0
    for item in data:
        direction, number = item[0], int(item[1:])
        if direction == "L":
            startNum -= number
        elif direction == "R":
            startNum += number

        if startNum % 100 == 0:
            zeros += 1
    
    return zeros


def part2(data: list[str]) -> int:
    """Solve part 2 of the puzzle."""
    startNum = 50
    zeros = 0
    for item in data:
        direction, number = item[0], int(item[1:])
        for n in range(0, number):
            if direction == "L":
                startNum -= 1
            elif direction == "R":
                startNum += 1

            if startNum % 100 == 0:
                zeros += 1
    return zeros


if __name__ == '__main__':
    run_solution(part1, part2, transform_input=lambda x: x.split('\n'))
