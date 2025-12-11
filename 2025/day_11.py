"""Day 11"""

from common import get_puzzle_input, test_sample_input


def parse_input(puzzle_input: str):
    lines = [l.split(":") for l in puzzle_input.split("\n")]
    return {l[0]: set(l[1].strip().split(" ")) for l in lines}


def part_1(puzzle_input):
    puzzle_input = parse_input(puzzle_input)
    queue = ["you"]
    result = 0
    while len(queue) > 0:
        device = queue.pop(0)
        if device == "out":
            result += 1
        elif device in puzzle_input:
            for d in puzzle_input[device]:
                queue.append(d)

    return result


def part_2(puzzle_input):
    puzzle_input = parse_input(puzzle_input)

    result = 0

    return result


def test():
    part_1_sample_result = 5
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
