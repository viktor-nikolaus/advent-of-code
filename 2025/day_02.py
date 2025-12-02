"""Day 2"""

import re

from common import get_puzzle_input, test_sample_input


def parse_input(puzzle_input):
    return [tuple([int(i) for i in e.split("-")]) for e in puzzle_input.split(",")]


def part_1(puzzle_input):
    ranges = parse_input(puzzle_input)
    result = 0
    for (s, e) in ranges:
        i = str(s)[0:int(len(str(s))/2)]
        if len(i) == 0:
            i = "1"
        while int(i + i) < s:
            i = str(int(i) + 1)
        while int(i + i) <= e:
            result += int(i + i)
            i = str(int(i) + 1)
    return result


def part_2(puzzle_input):
    ranges = parse_input(puzzle_input)
    result = 0
    for (s, e) in ranges:
        for i in range(s, e + 1):
            m = re.fullmatch(r"^(\d+)\1+$", str(i))
            if m != None:
                result += i
    return result


def test():
    part_1_sample_result = 1227775554
    part_2_sample_result = 4174379265
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
