"""
Advent of Code 2025 - Day 8
"""

import sys; from pathlib import Path; sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from utils.aoc import run_solution
from collections import defaultdict


def euclidean_distance(p1: tuple[int, int, int], p2: tuple[int, int, int]) -> float:
    return ((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2 + (p1[2] - p2[2])**2)**0.5


def part1(data: list[tuple[int, int, int]]) -> int:
    distances = []
    for i, point1 in enumerate(data):
        for j, point2 in enumerate(data):
            if i < j:
                distances.append((euclidean_distance(point1, point2), point1, point2))
    sorted_distances = sorted(distances, key=lambda x: x[0])

    point_to_circuit = {}
    num_connections = 10 if len(data) <= 20 else 1000 ## Hardcoded to match example and real

    for i in range(num_connections):
        point1 = sorted_distances[i][1]
        point2 = sorted_distances[i][2]

        if point1 not in point_to_circuit and point2 not in point_to_circuit:
            point_to_circuit[point1] = point1 # First point is circuitID!
            point_to_circuit[point2] = point1
        elif point1 in point_to_circuit and point2 not in point_to_circuit:
            point_to_circuit[point2] = point_to_circuit[point1]           
        elif point2 in point_to_circuit and point1 not in point_to_circuit:
            point_to_circuit[point1] = point_to_circuit[point2]     
        else:
            circuit_to_keep = point_to_circuit[point1]
            circuit_to_replace = point_to_circuit[point2]
            if circuit_to_keep != circuit_to_replace:
                for point in list(point_to_circuit.keys()):
                    if point_to_circuit[point] == circuit_to_replace:
                        point_to_circuit[point] = circuit_to_keep

    circuits = defaultdict(list)
    for point, circuit_id in point_to_circuit.items():
        circuits[circuit_id].append(point)

    circuits_by_size = sorted(circuits.values(), key=lambda x: len(x), reverse=True)
    return len(circuits_by_size[0]) * len(circuits_by_size[1]) * len(circuits_by_size[2])


def part2(data: list[tuple[int, int, int]]) -> int:
    distances = []
    for i, point1 in enumerate(data):
        for j, point2 in enumerate(data):
            if i < j:
                distances.append((euclidean_distance(point1, point2), point1, point2))
    sorted_distances = sorted(distances, key=lambda x: x[0])

    point_to_circuit = {}

    for _, point1, point2 in sorted_distances:
        made_connection = False
        
        if point1 not in point_to_circuit and point2 not in point_to_circuit:
            point_to_circuit[point1] = point1 # First point is circuitID!
            point_to_circuit[point2] = point1
            made_connection = True
        elif point1 in point_to_circuit and point2 not in point_to_circuit:
            point_to_circuit[point2] = point_to_circuit[point1]
            made_connection = True
        elif point2 in point_to_circuit and point1 not in point_to_circuit:
            point_to_circuit[point1] = point_to_circuit[point2]
            made_connection = True
        else:
            circuit_to_keep = point_to_circuit[point1]
            circuit_to_replace = point_to_circuit[point2]
            if circuit_to_keep != circuit_to_replace:
                for point in list(point_to_circuit.keys()):
                    if point_to_circuit[point] == circuit_to_replace:
                        point_to_circuit[point] = circuit_to_keep
                made_connection = True
        
        if made_connection and len(point_to_circuit) == len(data):
            if len(set(point_to_circuit.values())) == 1:
                return point1[0] * point2[0]
    
    return 0


if __name__ == '__main__':
    run_solution(part1, part2, transform_input=lambda x: [tuple(map(int, line.split(','))) for line in x.split('\n')])

