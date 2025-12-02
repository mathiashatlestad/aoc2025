"""
Advent of Code 2025 - Day 1
"""

import sys; from pathlib import Path; sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
import argparse
from utils.aoc import read_input


def part1(data: str) -> int:
    """Solve part 1 of the puzzle."""
    startNum = 50
    zeros = 0
    for item in data:
        direction, number = item[0], int(item[1:])
        if direction == "L":
            startNum-=number
        elif direction == "R":
            startNum+=number

        if startNum % 100 == 0:
            zeros+=1
    
    return zeros


def part2(data: str) -> int:
    """Solve part 1 of the puzzle."""
    startNum = 50
    zeros = 0
    for item in data:
        direction, number = item[0], int(item[1:])
        for n in range(0, number):
            if direction == "L":
                startNum-=1
            elif direction == "R":
                startNum+=1

            if startNum % 100 == 0:
                zeros+=1
    return zeros


parser = argparse.ArgumentParser(description='Advent of Code solution')
parser.add_argument('-e', '--example', action='store_true', help='Use example.txt instead of input.txt')
args = parser.parse_args()

lines = read_input(args.example).split('\n')

result1 = part1(lines)
print(f"Part 1: {result1}")

result2 = part2(lines)
print(f"Part 2: {result2}")
