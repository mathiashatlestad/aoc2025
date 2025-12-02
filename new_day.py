#!/usr/bin/env python3
"""
Script to create a new Advent of Code day folder with template files.
Usage: python new_day.py [day_number]
If no day number is provided, creates the next available day.
"""

import sys
from pathlib import Path
import shutil


def get_next_day() -> int:
    """Find the next available day number."""
    project_root = Path(__file__).parent
    existing_days = [
        int(d.name.replace('day', ''))
        for d in project_root.iterdir()
        if d.is_dir() and d.name.startswith('day') and d.name[3:].isdigit()
    ]
    return max(existing_days, default=0) + 1


def create_day(day_number: int) -> None:
    """Create a new day folder with template files."""
    if not 1 <= day_number <= 25:
        print(f"Error: Day number must be between 1 and 25, got {day_number}")
        sys.exit(1)
    
    project_root = Path(__file__).parent
    day_folder = project_root / f"day{day_number:02d}"
    
    if day_folder.exists():
        print(f"Error: {day_folder.name} already exists!")
        sys.exit(1)
    
    # Create the folder
    day_folder.mkdir()
    
    # Copy template to solve.py
    template_file = project_root / "template.py"
    solve_file = day_folder / "solve.py"
    
    if template_file.exists():
        # Read template and update the day number in the docstring
        content = template_file.read_text()
        content = content.replace("Day X", f"Day {day_number}")
        solve_file.write_text(content)
    else:
        print("Warning: template.py not found, creating basic solve.py")
        solve_file.write_text('"""Advent of Code 2025 - Day {day_number}"""\n\n# TODO: Implement solution\n')
    
    # Create empty input.txt
    input_file = day_folder / "input.txt"
    input_file.write_text("# Add your puzzle input here\n")
    
    print(f"✅ Created {day_folder.name}/")
    print(f"   - solve.py")
    print(f"   - input.txt")
    print(f"\nNext steps:")
    print(f"1. Add your puzzle input to {day_folder.name}/input.txt")
    print(f"2. Implement the solution in {day_folder.name}/solve.py")
    print(f"3. Run: python {day_folder.name}/solve.py")


def main():
    if len(sys.argv) > 1:
        try:
            day_number = int(sys.argv[1])
        except ValueError:
            print(f"Error: Invalid day number '{sys.argv[1]}'. Must be an integer.")
            sys.exit(1)
    else:
        day_number = get_next_day()
        print(f"Creating day {day_number}...")
    
    create_day(day_number)


if __name__ == "__main__":
    main()
