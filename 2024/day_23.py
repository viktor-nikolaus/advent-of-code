"""Day 23"""

from common import get_puzzle_input, test_sample_input


def part_1(puzzle_input):
    links = [l.split("-") for l in puzzle_input.split("\n")]
    sets = {}
    for a, b in links:
        if a not in sets:
            sets[a] = set()
        sets[a].add(b)
        if b not in sets:
            sets[b] = set()
        sets[b].add(a)
    # print(sets)
    trio_sets = set()
    for c1, s in sets.items():
        for c2 in s:
            for c3 in s.intersection(sets[c2]):
                key = tuple(sorted([c1, c2, c3]))
                trio_sets.add(key)
    # print(len(trio_sets))
    return len([1 for s in trio_sets if any(c.startswith("t") for c in s)])


def part_2(puzzle_input):
    return ""


def test():
    part_1_sample_result = 7
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
