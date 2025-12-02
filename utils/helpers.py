"""Helper functions for Advent of Code puzzles."""

import argparse
import inspect
import time
from pathlib import Path
from typing import Callable, Any


def read_input(use_example: bool = False) -> str:
    """Read the input file for the calling day's folder.
    
    Automatically detects which day folder is calling this function
    and reads from that day's input.txt or example.txt file.
    
    Args:
        use_example: If True, reads from example.txt instead of input.txt
    
    Returns:
        The contents of the input file as a string
    """
    # Get the caller's file path - walk up the stack to find the first non-utils file
    for frame_info in inspect.stack()[1:]:
        caller_path = Path(frame_info.filename)
        if 'utils' not in caller_path.parts:
            break
    
    # Find input.txt or example.txt in the same directory as the caller
    filename = "example.txt" if use_example else "input.txt"
    input_path = caller_path.parent / filename
    return input_path.read_text().strip()


def run_solution(
    part1_func: Callable[[Any], int],
    part2_func: Callable[[Any], int],
    transform_input: Callable[[str], Any]
) -> None:
    """Run an Advent of Code solution with standard argument parsing.
    
    Handles argument parsing, input reading, and running both parts.
    
    Args:
        part1_func: Function to solve part 1
        part2_func: Function to solve part 2
        transform_input: Optional function to transform the raw input string
    """
    parser = argparse.ArgumentParser(description='Advent of Code solution')
    parser.add_argument('-e', '--example', action='store_true', help='Use example.txt instead of input.txt')
    args = parser.parse_args()
    
    raw_input = read_input(args.example)
    data = transform_input(raw_input)
    
    start = time.perf_counter()
    result1 = part1_func(data)
    elapsed1 = time.perf_counter() - start
    print(f"Part 1: {result1} - ({elapsed1*1000:.0f} ms)")
    
    start = time.perf_counter()
    result2 = part2_func(data)
    elapsed2 = time.perf_counter() - start
    print(f"Part 2: {result2} - ({elapsed2*1000:.0f} ms)")
