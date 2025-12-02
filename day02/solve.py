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
            str_len = len(my_string)
            midpoint = str_len // 2
            if my_string[:midpoint] == my_string[midpoint:]:
                count += n       
    return count


def part2(data: str) -> int:
    count = 0
    for item in data:
        split = item.split('-')
        first, last = int(split[0]), int(split[1])
        for n in range(first, last+1):
            my_string = str(n)
            str_len = len(my_string)
            for length in range(1, str_len // 2 + 1):
                if str_len % length == 0:
                    pattern = my_string[:length]
                    if my_string == pattern * (str_len // length):
                        count += n
                        break
    return count


parser = argparse.ArgumentParser(description='Advent of Code solution')
parser.add_argument('-e', '--example', action='store_true', help='Use example.txt instead of input.txt')
args = parser.parse_args()

lines = read_input(args.example).split('\n')[0].split(',')

result1 = part1(lines)
print(f"Part 1: {result1}")

result2 = part2(lines)
print(f"Part 2: {result2}")

