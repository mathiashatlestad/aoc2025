"""
Advent of Code 2025 - Day 5
"""

import sys; from pathlib import Path; sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from utils.aoc import run_solution

def parse_data(data: str) -> int:
    lines = data.split('\n')
    ingredients = []
    ranges = []
    for line in lines:
        if not line:
            continue
        if "-" in line:
            splitted = line.split('-')
            ranges.append((int(splitted[0]), int(splitted[1])))
        else:
            ingredients.append(int(line))
    return (ingredients, ranges)        


def isInRange(ingredient, ranges):
    for range in ranges:
        if ingredient >= range[0] and ingredient <= range[1]:
            return True
    return False    


def part1(data: tuple[list[int], list[tuple[int][int]]]) -> int:
    count = 0
    for ingeredient in data[0]:
        if isInRange(ingeredient, data[1]):
            count+=1

    return count


def part2(data: tuple[list[int], list[tuple[int][int]]]) -> int:
    sorted_ranges = sorted(data[1], key=lambda x: x[0])
    
    merged_ranges = []
    for current in sorted_ranges:
        if not merged_ranges or current[0] > merged_ranges[-1][1] + 1:
            merged_ranges.append(current)
        else:
            last = merged_ranges[-1]
            merged_ranges[-1] = (last[0], max(last[1], current[1]))
    
    count = 0
    for rng in merged_ranges:
        count += rng[1] - rng[0] + 1
    return count


if __name__ == '__main__':
    run_solution(part1, part2, transform_input=lambda x: parse_data(x))

