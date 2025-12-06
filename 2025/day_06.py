"""Day 6"""

import re

from common import get_puzzle_input, test_sample_input


def parse_input(puzzle_input: str):
    grid = [re.split(r"[ ]+", l.strip()) for l in puzzle_input.split("\n")]
    grid = [[int(i) for i in l] for l in grid[0:-1]] + [grid[-1]]
    return grid


def part_1(puzzle_input):
    puzzle_input = parse_input(puzzle_input)
    
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
    puzzle_input = parse_input(puzzle_input)

    result = 0

    return result


def test():
    part_1_sample_result = 4277556
    part_2_sample_result = 0
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
