"""
Advent of Code 2025 - Day 1
"""

import sys; from pathlib import Path; sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
import argparse
from utils.aoc import read_input


def part1(data: str) -> int:
    """Solve part 1 of the puzzle."""
    




    
    return 0


def part2(data: str) -> int:
    """Solve part 2 of the puzzle."""
    # TODO: Implement solution
    return 0

parser = argparse.ArgumentParser(description='Advent of Code solution')
parser.add_argument('-e', '--example', action='store_true', help='Use example.txt instead of input.txt')
args = parser.parse_args()

lines = read_input(args.example).split('\n')

result1 = part1(lines)
print(f"Part 1: {result1}")

result2 = part2(lines)
print(f"Part 2: {result2}")
