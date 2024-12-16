"""common"""

import os
import sys


def get_puzzle_input() -> str:
    script_name = os.path.basename(sys.argv[0])
    input_path = os.path.join(os.path.basename(os.path.dirname(sys.argv[0])), "inputs", script_name.partition(".")[0] + ".txt")
    with open(input_path, "r", encoding="utf-8") as file:
        return file.read()


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
