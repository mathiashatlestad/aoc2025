import sys; from pathlib import Path; sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from utils.aoc import run_solution
import re
import pulp


def parse_machine(line):
    target = [c == '#' for c in re.search(r'\[([.#]+)\]', line).group(1)]
    buttons = [[int(x) for x in m.split(',')] for m in re.findall(r'\(([0-9,]+)\)', line)]
    joltages = [int(x) for x in re.search(r'\{([0-9,]+)\}', line).group(1).split(',')]
    return target, buttons, joltages


def solve_lights(target, buttons):
    prob = pulp.LpProblem("Lights", pulp.LpMinimize)
    x = [pulp.LpVariable(f"b{i}", cat='Binary') for i in range(len(buttons))]
    
    prob += pulp.lpSum(x)
    
    for i, is_on in enumerate(target):
        affected = [j for j, button in enumerate(buttons) if i in button]
        if not affected:
            if is_on:
                return None
            continue
        
        y = pulp.LpVariable(f"aux_{i}", lowBound=0, cat='Integer')
        prob += pulp.lpSum(x[j] for j in affected) == 2 * y + (1 if is_on else 0)
    
    prob.solve(pulp.PULP_CBC_CMD(msg=0))
    return int(sum(v.varValue for v in x)) if prob.status == pulp.LpStatusOptimal else None


def solve_joltage(joltages, buttons):
    prob = pulp.LpProblem("Joltage", pulp.LpMinimize)
    x = [pulp.LpVariable(f"b{i}", lowBound=0, cat='Integer') for i in range(len(buttons))]
    
    prob += pulp.lpSum(x)
    
    for i, target in enumerate(joltages):
        constraint = [x[j] for j, button in enumerate(buttons) if i in button]
        if constraint:
            prob += pulp.lpSum(constraint) == target
        elif target != 0:
            return None
    
    prob.solve(pulp.PULP_CBC_CMD(msg=0))
    return int(sum(v.varValue for v in x)) if prob.status == pulp.LpStatusOptimal else None


def part1(data):
    return sum(solve_lights(*parse_machine(line)[:2]) or 0 for line in data if line.strip())


def part2(data):
    return sum(solve_joltage(joltages, buttons) or 0 
               for _, buttons, joltages in (parse_machine(line) for line in data if line.strip()))


if __name__ == '__main__':
    run_solution(part1, part2, transform_input=lambda x: x.split('\n'))

