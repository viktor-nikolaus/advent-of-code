"""Day 7"""

from common import get_puzzle_input, test_sample_input


def parse_input(puzzle_input: str):
    return [[c for c in l] for l in puzzle_input.split("\n")]


def fill_beams(puzzle_input):
    for y in range(len(puzzle_input) - 1):
        for x in range(len(puzzle_input[y])):
            c = puzzle_input[y][x]
            if c == "S" or c == "|":
                match puzzle_input[y+1][x]:
                    case ".":
                        puzzle_input[y+1][x] = "|"
                    case "^":
                        puzzle_input[y+1][x-1] = "|"
                        puzzle_input[y+1][x+1] = "|"


def count_splits(puzzle_input):
    total = 0
    for y in range(1, len(puzzle_input)):
        for x in range(len(puzzle_input[y])):
            c = puzzle_input[y][x]
            if c == "^" and puzzle_input[y-1][x] == "|":
                total += 1
    return total


def part_1(puzzle_input):
    puzzle_input = parse_input(puzzle_input)
    fill_beams(puzzle_input)
    result = count_splits(puzzle_input)

    return result


def fill_beams_count(puzzle_input):
    for y in range(len(puzzle_input)):
        for x in range(len(puzzle_input[y])):
            match puzzle_input[y][x]:
                case "S":
                    puzzle_input[y][x] = 1
                case ".":
                    puzzle_input[y][x] = 0
            
    for y in range(1, len(puzzle_input)):
        width = len(puzzle_input[y])
        for x in range(len(puzzle_input[y])):
            if puzzle_input[y][x] == "^":
                continue
            v = puzzle_input[y-1][x]
            if v == "^":
                v = 0
            if x > 0 and puzzle_input[y][x-1] == "^":
                v += puzzle_input[y-1][x-1]
            if x < width - 1 and puzzle_input[y][x+1] == "^":
                v += puzzle_input[y-1][x+1]
            puzzle_input[y][x] = v


def part_2(puzzle_input):
    puzzle_input = parse_input(puzzle_input)
    fill_beams_count(puzzle_input)
    result = sum(puzzle_input[-1])
    return result


def test():
    part_1_sample_result = 21
    part_2_sample_result = 40
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
