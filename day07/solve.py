"""
Advent of Code 2025 - Day 7
"""

import sys; from pathlib import Path; sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from utils.aoc import run_solution
from collections import defaultdict

def part1(data: list[list[str]]) -> int:
    rows = len(data)
    cols = len(data[0])

    start_col = data[0].index('S')
    
    beams = [(1, start_col)] ## Start row, colum for the first beam!
    split_count = 0
    visited = set()
    
    while beams:
        row, col = beams.pop(0)

        if row < 0 or row >= rows or col < 0 or col >= cols:
            continue

        if (row, col) in visited:
            continue

        visited.add((row, col))
        
        cell = data[row][col]
        
        if cell == '^':
            split_count += 1
            beams.append((row, col - 1))
            beams.append((row, col + 1))
        else:
            beams.append((row + 1, col))

    return split_count


def part2(data: list[list[str]]) -> int:
    rows = len(data)
    cols = len(data[0])
    
    start_col = data[0].index('S')
    
    current_row_paths = defaultdict(int)
    current_row_paths[start_col] = 1
    
    total_timelines = 0
    
    for row in range(1, rows):
        next_row_paths = defaultdict(int)
        
        for col, count in current_row_paths.items():
            
            if col < 0 or col >= cols: # Terminating outside the map! 
                total_timelines += count 
                continue
            
            cell = data[row][col]
            
            if cell == '^':
                next_row_paths[col - 1] += count
                next_row_paths[col + 1] += count
            else:
                next_row_paths[col] += count
        
        current_row_paths = next_row_paths

    ## Count for the last row
    for col, count in current_row_paths.items():
        total_timelines += count

    return total_timelines


if __name__ == '__main__':
    run_solution(part1, part2, transform_input=lambda x: [list(line) for line in x.split('\n')])

