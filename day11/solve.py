"""
Advent of Code 2025 - Day 11
"""

from functools import lru_cache
import sys; from pathlib import Path; sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from utils.aoc import run_solution


def part1(data: list[str]) -> int:
    graph = {}
    for line in data:
        if not line:
            continue
        device, outputs = line.split(': ')
        graph[device] = outputs.split()
    
    @lru_cache(maxsize=None)
    def count_paths(current):
        if current == "out":
            return 1
        if current not in graph:
            return 0
        return sum(count_paths(neighbor) for neighbor in graph[current])
    
    return count_paths("you")


def part2(data: list[str]) -> int:
    graph = {}
    for line in data:
        if not line:
            continue
        device, outputs = line.split(': ')
        graph[device] = outputs.split()
    
    @lru_cache(maxsize=None)
    def count_paths(current, required):
        if current == "out":
            return 1 if len(required) == 2 else 0
        if current not in graph:
            return 0
        
        total = 0
        for neighbor in graph[current]:
            new_required = required | {neighbor} if neighbor in ["dac", "fft"] else required
            total += count_paths(neighbor, new_required)
        return total
    
    return count_paths("svr", frozenset())


if __name__ == '__main__':
    run_solution(part1, part2, transform_input=lambda x: x.split('\n'))

