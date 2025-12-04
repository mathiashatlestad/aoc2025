"""
Advent of Code 2025 - Day 4
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from utils.aoc import run_solution

def can_be_taken(data: list[list[str]], i: int, j: int) -> bool:
    if data[i][j] != "@":
        return False
    
    rows, cols = len(data), len(data[0])
    hits = 0
    
    for i2 in range(max(0, i - 1), min(rows, i + 2)):
        for j2 in range(max(0, j - 1), min(cols, j + 2)):
            if (i2, j2) != (i, j) and data[i2][j2] == "@":
                hits += 1
                if hits >= 4:
                    return False
    
    return True 

def part1(data: list[list[str]]) -> int:
    return sum(
        can_be_taken(data, i, j)
        for i in range(len(data))
        for j in range(len(data[0]))
    )

def part2(data: list[list[str]]) -> int:
    count = 0
    rows, cols = len(data), len(data[0])
    
    to_check = {(i, j) for i in range(rows) for j in range(cols) if can_be_taken(data, i, j)}
    
    while to_check:
        i, j = to_check.pop()
        
        if can_be_taken(data, i, j):
            data[i][j] = "."
            count += 1
            for i2 in range(max(0, i - 1), min(rows, i + 2)):
                for j2 in range(max(0, j - 1), min(cols, j + 2)):
                    if data[i2][j2] == "@":
                        to_check.add((i2, j2))
    
    return count


if __name__ == '__main__':
    run_solution(part1, part2, transform_input=lambda x: [list(line) for line in x.split('\n') if line])

