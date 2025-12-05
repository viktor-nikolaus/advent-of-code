"""Day 5"""

from common import get_puzzle_input, test_sample_input


def parse_input(puzzle_input: str):
    fresh_range, ingredient_ids = puzzle_input.split("\n\n")
    fresh_range = [tuple([int(i) for i in r.strip().split("-")]) for r in fresh_range.split("\n")]
    ingredient_ids = [int(i) for i in ingredient_ids.split("\n")]
    return (fresh_range, ingredient_ids)


def part_1(puzzle_input):
    fresh_range, ingredient_ids = parse_input(puzzle_input)

    result = 0
    for i in ingredient_ids:
        if any(i >= r[0] and i <= r[1] for r in fresh_range):
            result += 1

    return result


def part_2(puzzle_input):
    fresh_range, ingredient_ids = parse_input(puzzle_input)

    result = 0

    return result


def test():
    part_1_sample_result = 3
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
