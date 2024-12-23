"""Day 23"""

from common import get_puzzle_input, test_sample_input


def extract_links(puzzle_input):
    links = [l.split("-") for l in puzzle_input.split("\n")]
    sets = {}
    for a, b in links:
        if a not in sets:
            sets[a] = set()
        sets[a].add(b)
        if b not in sets:
            sets[b] = set()
        sets[b].add(a)
    return sets


def part_1(puzzle_input):
    sets = extract_links(puzzle_input)
    trio_sets = set()
    for c1, s in sets.items():
        for c2 in s:
            for c3 in s.intersection(sets[c2]):
                key = tuple(sorted([c1, c2, c3]))
                trio_sets.add(key)
    # print(len(trio_sets))
    return len([1 for s in trio_sets if any(c.startswith("t") for c in s)])


def part_2(puzzle_input):
    links = extract_links(puzzle_input)
    groups = []
    for c1, s in links.items():
        for c2 in s:
            common_groups = [g for g in groups if c1 in g and c2 in g]
            potential_groups_1 = [g for g in groups if c1 in g and c2 not in g]
            potential_groups_2 = [g for g in groups if c2 in g and c1 not in g]
            if len(common_groups) == 0:
                groups.append(set([c1, c2]))
            for g in potential_groups_1:
                if all(c3 in links[c2] for c3 in g):
                    g.add(c2)
            for g in potential_groups_2:
                if all(c3 in links[c1] for c3 in g):
                    g.add(c1)
    return ",".join(sorted(max(groups, key=len)))


def test():
    part_1_sample_result = 7
    part_2_sample_result = "co,de,ka,ta"
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
