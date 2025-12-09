"""Day 9"""

from common import get_puzzle_input, test_sample_input


def parse_input(puzzle_input: str):
    return [tuple([int(c) for c in l.split(",")]) for l in puzzle_input.split("\n")]


def part_1(puzzle_input):
    puzzle_input = parse_input(puzzle_input)
    areas = {}
    for a_i in range(len(puzzle_input)):
        for b_i in range(a_i + 1, len(puzzle_input)):
            a = puzzle_input[a_i]
            b = puzzle_input[b_i]
            areas[(a_i, b_i)] = abs(a[0] - b[0] + 1) * abs(a[1] - b[1] + 1)
    result = max(areas.values())

    return result


def part_2(puzzle_input):
    puzzle_input = parse_input(puzzle_input)

    result = 0

    return result


def test():
    part_1_sample_result = 50
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
