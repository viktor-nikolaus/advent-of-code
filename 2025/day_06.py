"""Day 6"""

import re

from common import get_puzzle_input, test_sample_input


def parse_input_1(puzzle_input: str):
    grid = [re.split(r"[ ]+", l.strip()) for l in puzzle_input.split("\n")]
    grid = [[int(i) for i in l] for l in grid[0:-1]] + [grid[-1]]
    return grid


def transpose(grid):
    result = [[grid[y][x] for y in range(len(grid))] for x in range(len(grid[0]))]
    return result


def parse_input_2(puzzle_input: str):
    lines = puzzle_input.split("\n")
    grid = []
    k = 0
    start_k = 0
    for k in range(1, len(lines[0])):
        if lines[-1][k] != " ":
            end_k = k - 1
            subgrid = [l[start_k:end_k] for l in lines]
            subgrid = transpose(subgrid)
            op = subgrid[0][-1]
            subgrid = [int("".join(l[0:-1]).strip()) for l in subgrid] + [op]
            grid.append(subgrid)
            start_k = k
    
    subgrid = [l[start_k:] for l in lines]
    subgrid = transpose(subgrid)
    op = subgrid[0][-1]
    subgrid = [int("".join(l[0:-1]).strip()) for l in subgrid] + [op]
    grid.append(subgrid)

    return grid


def part_1(puzzle_input):
    puzzle_input = parse_input_1(puzzle_input)
    result = 0
    for x in range(len(puzzle_input[0])):
        operation = puzzle_input[-1][x]
        total = 0 if operation == "+" else 1
        for y in range(len(puzzle_input) - 1):
            i = puzzle_input[y][x]
            match operation:
                case "+":
                    total += i
                case "*":
                    total *= i
        result += total

    return result


def part_2(puzzle_input):
    puzzle_input = parse_input_2(puzzle_input)
    result = 0
    for l in puzzle_input:
        operation = l[-1]
        total = 0 if operation == "+" else 1
        for i in l[0:-1]:
            match operation:
                case "+":
                    total += i
                case "*":
                    total *= i
        result += total

    return result


def test():
    part_1_sample_result = 4277556
    part_2_sample_result = 3263827
    result = True
    result &= test_sample_input(1, 1, part_1_sample_result, part_1)
    result &= test_sample_input(1, 2, part_2_sample_result, part_2)
    return result


def main():
    puzzle_input = get_puzzle_input()
    print("Part 1:", part_1(puzzle_input))
    print("Part 2:", part_2(puzzle_input))


if __name__ == "__main__":
    if test():
        main()
