"""
Advent of Code 2025 - Day 1
"""

from pathlib import Path


def read_input() -> str:
    """Read the input file for this day."""
    input_path = Path(__file__).parent / "input.txt"
    return input_path.read_text().strip()


def part1(data: str) -> int:
    """Solve part 1 of the puzzle."""
    lines = data.split('\n')
    # TODO: Implement solution
    return 0


def part2(data: str) -> int:
    """Solve part 2 of the puzzle."""
    lines = data.split('\n')
    # TODO: Implement solution
    return 0


def main():
    data = read_input()
    
    result1 = part1(data)
    print(f"Part 1: {result1}")
    
    result2 = part2(data)
    print(f"Part 2: {result2}")


if __name__ == "__main__":
    main()
