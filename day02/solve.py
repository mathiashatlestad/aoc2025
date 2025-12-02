"""
Advent of Code 2025 - Day 2
"""

import sys; from pathlib import Path; sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from utils.aoc import run_solution


def is_repeating_once(s: str) -> bool:
    str_len = len(s)
    if str_len % 2 != 0:
        return False
    midpoint = str_len // 2
    return s[:midpoint] == s[midpoint:]


def has_repeating_pattern(s: str) -> bool:
    str_len = len(s)
    for length in range(1, str_len // 2 + 1):
        if str_len % length == 0:
            pattern = s[:length]
            if s == pattern * (str_len // length):
                return True
    return False


def part1(data: list[str]) -> int:
    count = 0
    for item in data:
        first, last = map(int, item.split('-'))
        for n in range(first, last + 1):
            my_string = str(n)
            if is_repeating_once(my_string):
                count += n       
    return count


def part2(data: list[str]) -> int:
    count = 0
    for item in data:
        first, last = map(int, item.split('-'))
        for n in range(first, last + 1):
            my_string = str(n)
            if has_repeating_pattern(my_string):
                count += n
    return count


if __name__ == '__main__':
    run_solution(
        part1,
        part2,
        transform_input=lambda x: x.split('\n')[0].split(',')
    )

