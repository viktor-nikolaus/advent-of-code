"""common"""

import os
import sys


def get_puzzle_input() -> str:
    script_name = os.path.basename(sys.argv[0])
    input_path = os.path.join(os.path.basename(os.path.dirname(sys.argv[0])), "inputs", script_name.partition(".")[0] + ".txt")
    with open(input_path, "r", encoding="utf-8") as file:
        return file.read()
