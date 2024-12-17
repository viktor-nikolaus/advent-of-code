"""common"""

import os
import sys


def get_puzzle_input() -> str:
    script_name = os.path.basename(sys.argv[0])
    input_path = os.path.join(os.path.basename(os.path.dirname(sys.argv[0])), "inputs", script_name.partition(".")[0] + ".txt")
    with open(input_path, "r", encoding="utf-8") as file:
        return file.read()


def get_puzzle_sample_input(i) -> str:
    script_name = os.path.basename(sys.argv[0])
    input_path = os.path.join(os.path.basename(os.path.dirname(sys.argv[0])), "inputs", script_name.partition(".")[0] + ".sample" + str(i) + ".txt")
    with open(input_path, "r", encoding="utf-8") as file:
        return file.read()


def test_sample_input(sample_i, part_i, expected, processor):
    puzzle_sample_input = get_puzzle_sample_input(sample_i)
    result = processor(puzzle_sample_input)
    success = expected == result
    print(f"Sample {sample_i} Part {part_i}: " + ("Correct" if success else f"Wrong\n  expected: {expected}\n  actual: {result}"))


def parse_grid(string) -> list:
    return [list(l) for l in string.split("\n")]


def find_first_position(needle, grid) -> tuple[int, int]:
    return next(iter([(x, y) for y, l in enumerate(grid) for x, c in enumerate(l) if c == needle]), None)


def copy_grid(grid) -> list:
    return [list(l) for l in grid]


def print_grid(grid, margin_x = 0) -> None:
    max_cell_length = max(len(str(c)) for l in grid for c in l) + margin_x
    for l in grid:
        for c in l:
            c_str = str(c)
            print((" " * (max_cell_length - len(c_str))) + c_str, end="")
        print()
    print()


def iter_grid(grid):
    for y, l in enumerate(grid):
        for x, c in enumerate(l):
            yield ((x, y), c)


def grid_at(grid, pos):
    if 0 <= pos[1] < len(grid) and 0 <= pos[0] < len(grid[0]):
        return grid[pos[1]][pos[0]]
    return None


def grid_set(grid, pos, val):
    if 0 <= pos[1] < len(grid) and 0 <= pos[0] < len(grid[0]):
        grid[pos[1]][pos[0]] = val
