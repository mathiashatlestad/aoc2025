"""Helper functions for Advent of Code puzzles."""

from pathlib import Path


def read_input(day: int) -> str:
    """Read the input file for a given day.
    
    Args:
        day: The day number (1-25)
        
    Returns:
        The contents of the input file as a string
    """
    input_path = Path(__file__).parent.parent / "inputs" / f"day{day:02d}.txt"
    return input_path.read_text().strip()


def read_input_lines(day: int) -> list[str]:
    """Read the input file for a given day as a list of lines.
    
    Args:
        day: The day number (1-25)
        
    Returns:
        A list of lines from the input file
    """
    return read_input(day).split('\n')


def read_input_numbers(day: int) -> list[int]:
    """Read the input file for a given day as a list of integers.
    
    Args:
        day: The day number (1-25)
        
    Returns:
        A list of integers from the input file
    """
    return [int(line) for line in read_input_lines(day)]


def read_input_grid(day: int) -> list[list[str]]:
    """Read the input file for a given day as a 2D grid.
    
    Args:
        day: The day number (1-25)
        
    Returns:
        A 2D list representing the grid
    """
    return [list(line) for line in read_input_lines(day)]
