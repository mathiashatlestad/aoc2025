# Advent of Code 2025

My solutions for [Advent of Code 2025](https://adventofcode.com/2025) in Python.

## Project Structure

```
aoc2025/
├── day01/           # Day 1 puzzle
│   ├── input.txt    # Puzzle input
│   └── solve.py     # Solution (both parts)
├── day02/           # Day 2 puzzle
│   ├── input.txt
│   └── solve.py
├── ...
├── utils/           # Helper functions and utilities
│   ├── helpers.py   # Common helper functions
├── template.py      # Template for new day solutions
├── requirements.txt # Python dependencies
└── README.md        # This file
```

## Setup

1. Create and activate virtual environment:
```bash
python3 -m venv .venv
source .venv/bin/activate  # On macOS/Linux
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

### Creating a New Day Solution

**Option 1: Use the generator script (recommended)**
```bash
python new_day.py        # Creates the next day automatically
python new_day.py 5      # Creates a specific day (day05)
```

**Option 2: Manual setup**
```bash
mkdir day01
cp template.py day01/solve.py
touch day01/input.txt
```

Then add your puzzle input to `day01/input.txt`

3. Implement the `part1()` and `part2()` functions in `day01/solve.py`

4. Run your solution:
```bash
python day01/solve.py
```

### Helper Functions

Each `solve.py` file includes a `read_input()` function that reads from the local `input.txt` file. You can also use the `utils/helpers.py` module for common operations like parsing grids, numbers, etc.

## Progress

| Day | Part 1 | Part 2 |
| --- | ------ | ------ |
| 1   | ⬜      | ⬜      |
| 2   | ⬜      | ⬜      |
| 3   | ⬜      | ⬜      |
| 4   | ⬜      | ⬜      |
| 5   | ⬜      | ⬜      |
| ... | ...    | ...    |

Legend: ⬜ Not started | 🟡 In progress | ✅ Complete