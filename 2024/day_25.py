"""Day 25"""

from common import get_puzzle_input, test_sample_input


def parse_input(puzzle_input):
    locks = []
    keys = []
    for block in puzzle_input.split("\n\n"):
        lines = block.split("\n")
        measures = [0, 0, 0, 0, 0]
        for i in range(5):
            for h, l in list(enumerate(lines))[1:]:
                if l[i] != lines[0][i]:
                    measures[i] = h - 1
                    break
        if lines[0][0] == "#":
            locks.append(tuple(measures))
        else:
            keys.append(tuple(5 - m for m in measures))
    return (locks, keys)


def build_minimum(measurements):
    return tuple(min(m[i] for m in measurements) for i in range(5))


def is_longer(measurement, threshold):
    for i, h in enumerate(measurement):
        if h > threshold[i]:
            return True
    return False


def no_overlap(lock, key):
    for i, h in enumerate(lock):
        if h + key[i] > 5:
            return False
    return True


def part_1(puzzle_input):
    locks, keys = parse_input(puzzle_input)
    min_lock = build_minimum(locks)
    min_key = build_minimum(keys)
    max_lock = tuple(5 - m for m in min_key)
    max_key = tuple(5 - m for m in min_lock)
    locks = [l for l in locks if not is_longer(l, max_lock)]
    keys = [k for k in keys if not is_longer(k, max_key)]
    unique_fits = 0
    for lock in locks:
        for key in keys:
            if no_overlap(lock, key):
                unique_fits += 1
    return unique_fits


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
