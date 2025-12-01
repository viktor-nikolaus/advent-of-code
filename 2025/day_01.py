"""Day 1"""

from common import get_puzzle_input, test_sample_input


def part_1(puzzle_input):
    index = 50
    result = 0
    for l in puzzle_input.strip().split("\n"):
        sign = -1 if l[0] == "L" else 1
        val = int(l[1:]) * sign
        index += val
        index = (index + 100) % 100
        if index == 0:
            result += 1
    return result


def part_2(puzzle_input):
    return ""


def test():
    part_1_sample_result = 3
    part_2_sample_result = ""
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
