# Advent of Code 2025

Solutions for [Advent of Code 2025](https://adventofcode.com/2025).

## Setup

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Usage

Create a new day:
```bash
python new_day.py        # Creates the next day automatically
python new_day.py 5      # Creates a specific day (day05)
```

Each day folder contains:
- `solve.py` - Solution with `part1()` and `part2()` functions
- `input.txt` - Puzzle input
- `example.txt` - Example input for testing

Run a solution:
```bash
python dayXX/solve.py
```