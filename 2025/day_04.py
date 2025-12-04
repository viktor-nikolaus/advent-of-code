"""Day 4"""

from common import get_puzzle_input, test_sample_input


def parse_input(puzzle_input: str):
    return [[c for c in l] for l in puzzle_input.split("\n")]


def print_map(puzzle_map):
    print("\n".join(["".join([str(c) for c in l]) for l in puzzle_map]))


def update_map(puzzle_map, x, y, func):
    if y >= 0 and y < len(puzzle_map) and x >= 0 and x < len(puzzle_map[y]):
        puzzle_map[y][x] = func(puzzle_map[y][x])


DIRECTIONS = [(-1, -1), ( 0, -1), ( 1, -1),
              (-1,  0),           ( 1,  0),
              (-1,  1), ( 0,  1), ( 1,  1)]


def part_1(puzzle_input):
    puzzle_map = parse_input(puzzle_input)
    counter_map = [[0 for _ in l] for l in puzzle_map]
    for y in range(len(puzzle_map)):
        for x in range(len(puzzle_map[y])):
            if puzzle_map[y][x] == "@":
                for dx, dy in DIRECTIONS:
                    update_map(counter_map, x + dx, y + dy, lambda i: i + 1)
    
    result = 0
    for y in range(len(puzzle_map)):
        for x in range(len(puzzle_map[y])):
            if puzzle_map[y][x] == "@" and counter_map[y][x] < 4:
                result += 1
    
    return result


def part_2(puzzle_input):
    puzzle_map = parse_input(puzzle_input)
    result = 0
    return result


def test():
    part_1_sample_result = 13
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
