"""
Advent of Code 2025 - Day 3
"""

import sys; from pathlib import Path; sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from utils.aoc import run_solution

def find_jolts(arr, nums) -> int:
    result_str = ""
    remaining = nums
    start_pos = 0

    for _ in range(nums):
        max_tuple = max(
            (t for t in arr if start_pos <= t[1] <= len(arr) - remaining),
            key=lambda t: t[0],
            default=None
        )
        
        if max_tuple:
            result_str += max_tuple[0]
            start_pos = max_tuple[1] + 1
            remaining -= 1
    
    return int(result_str)


def part1(data: list[list[tuple]]) -> int:
    return sum(find_jolts(arr, 2) for arr in data)


def part2(data: list[list[tuple]]) -> int:
    return sum(find_jolts(arr, 12) for arr in data)


if __name__ == '__main__':
    run_solution(part1, part2, transform_input=lambda x: [[(ch, i) for i, ch in enumerate(line)] for line in x.split('\n')])

