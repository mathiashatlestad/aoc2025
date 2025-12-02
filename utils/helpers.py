"""Helper functions for Advent of Code puzzles."""

import inspect
from pathlib import Path


def read_input() -> str:
    """Read the input file for the calling day's folder.
    
    Automatically detects which day folder is calling this function
    and reads from that day's input.txt file.
    
    Returns:
        The contents of the input file as a string
    """
    # Get the caller's file path
    caller_frame = inspect.stack()[1]
    caller_path = Path(caller_frame.filename)
    
    # Find input.txt in the same directory as the caller
    input_path = caller_path.parent / "input.txt"
    return input_path.read_text().strip()


def read_input_legacy(day: int) -> str:
    """Read the input file for a given day (legacy function).
    
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
