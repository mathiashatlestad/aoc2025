"""
Advent of Code 2025 - Day 9
"""

from functools import lru_cache
import sys; from pathlib import Path; sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from utils.aoc import run_solution

def area(p1: tuple[int, int], p2: tuple[int, int]) -> float:
    return (1 + abs(p1[0] - p2[0])) * (1 + abs(p1[1] - p2[1]))


def part1(data: list[tuple[int, int]]) -> int:
    """Solve part 1 of the puzzle."""
    areas = []
    for i, point1 in enumerate(data):
        for j, point2 in enumerate(data):
            if i < j:
                areas.append((area(point1, point2), point1, point2))
    sorted_areas = sorted(areas, key=lambda x: x[0])
    return sorted_areas[-1][0]


def part2(data: list[tuple[int, int]]) -> int:
    """Solve part 2 of the puzzle."""
    n = len(data)
    
    h_segments = []
    v_segments = []
    boundary = set()
    
    for i in range(n):
        x1, y1 = data[i]
        x2, y2 = data[(i + 1) % n]
        
        if x1 == x2:
            v_segments.append((x1, min(y1, y2), max(y1, y2)))
            for y in range(min(y1, y2), max(y1, y2) + 1):
                boundary.add((x1, y))
        else:
            h_segments.append((y1, min(x1, x2), max(x1, x2)))
            for x in range(min(x1, x2), max(x1, x2) + 1):
                boundary.add((x, y1))
        
    @lru_cache(maxsize=None)
    def is_inside(x, y):
        if (x, y) in boundary:
            return True
        count = 0
        for seg_x, y_min, y_max in v_segments:
            if seg_x > x and y_min < y <= y_max:
                count += 1
        return count % 2 == 1
    
    def rect_ok(x1, y1, x2, y2):
        min_x, max_x = min(x1, x2), max(x1, x2)
        min_y, max_y = min(y1, y2), max(y1, y2)
        
        for x in [min_x, max_x]:
            for y in [min_y, max_y]:
                if not is_inside(x, y):
                    return False
        
        for seg_x, seg_y_min, seg_y_max in v_segments:
            if min_x < seg_x < max_x:
                test_y = min_y if min_y < seg_y_min or min_y > seg_y_max else max_y
                if min_y <= test_y <= max_y:
                    if not is_inside(seg_x, test_y):
                        return False
        
        for seg_y, seg_x_min, seg_x_max in h_segments:
            if min_y < seg_y < max_y:
                test_x = min_x if min_x < seg_x_min or min_x > seg_x_max else max_x
                if min_x <= test_x <= max_x:
                    if not is_inside(test_x, seg_y):
                        return False
        
        return True
    
    pairs = []
    for i in range(n):
        for j in range(i + 1, n):
            x1, y1 = data[i]
            x2, y2 = data[j]
            area_val = (abs(x2 - x1) + 1) * (abs(y2 - y1) + 1)
            pairs.append((area_val, x1, y1, x2, y2))
    
    pairs.sort(reverse=True)
    
    for area_val, x1, y1, x2, y2 in pairs:
        if rect_ok(x1, y1, x2, y2):
            return area_val
    
    return 0


if __name__ == '__main__':
    run_solution(part1, part2, transform_input=lambda x: [tuple(map(int, line.split(','))) for line in x.split('\n')])

