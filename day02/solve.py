"""
Advent of Code 2025 - Day 2
"""

import sys; from pathlib import Path; sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
import argparse
from utils.aoc import read_input


def part1(data: str) -> int:
    count = 0
    for item in data:
        split = item.split('-')
        first, last = int(split[0]), int(split[1])
        for n in range(first, last+1):
            my_string = str(n)
            midpoint = len(my_string) // 2
            half1 = my_string[:midpoint]
            half2 = my_string[midpoint:]
            if half1 == half2:
                count+=n       
    return count


def part2(data: str) -> int:
    count = 0
    for item in data:
        split = item.split('-')
        first, last = int(split[0]), int(split[1])
        for n in range(first, last+1):
            my_string = str(n)
            is_invalid = False
            for length in range(1, len(my_string) // 2 + 1):
                if len(my_string) % length == 0:  # Length must divide evenly
                    pattern = my_string[:length]
                    repetitions = len(my_string) // length
                    if repetitions >= 2 and pattern * repetitions == my_string:
                        is_invalid = True
                        break
            if is_invalid:
                count += n
    return count










parser = argparse.ArgumentParser(description='Advent of Code solution')
parser.add_argument('-e', '--example', action='store_true', help='Use example.txt instead of input.txt')
args = parser.parse_args()

lines = read_input(args.example).split('\n')[0].split(',')

result1 = part1(lines)
print(f"Part 1: {result1}")

result2 = part2(lines)
print(f"Part 2: {result2}")

