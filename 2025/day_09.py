"""Day 9"""

from common import get_puzzle_input, test_sample_input


def parse_input(puzzle_input: str):
    return [tuple([int(c) for c in l.split(",")]) for l in puzzle_input.split("\n")]


def get_area(point_a, point_b):
    return (abs(point_a[0] - point_b[0]) + 1) * (abs(point_a[1] - point_b[1]) + 1)


def part_1(puzzle_input):
    puzzle_input = parse_input(puzzle_input)
    areas = {}
    for a_i in range(len(puzzle_input)):
        for b_i in range(a_i + 1, len(puzzle_input)):
            a = puzzle_input[a_i]
            b = puzzle_input[b_i]
            areas[(a_i, b_i)] = get_area(a, b)
    result = max(areas.values())

    return result


def part_2(puzzle_input):
    puzzle_input = parse_input(puzzle_input)
    n = len(puzzle_input)
    result = 1

    sub_points = []
    for i in range(n):
        j = (i + 1) % n
        p = puzzle_input[i]
        q = puzzle_input[j]
        r = ((p[0] + q[0]) / 2.0, (p[1] + q[1]) / 2.0)
        sub_points.append(r)

    for a_i in range(n):
        for b_i in range(n):
            if a_i == b_i:
                continue
            if (a_i - b_i) % 2 != 0:
                continue
            a = puzzle_input[a_i]
            b = puzzle_input[b_i]
            min_x = min(a[0], b[0])
            max_x = max(a[0], b[0])
            min_y = min(a[1], b[1])
            max_y = max(a[1], b[1])
            intersecting_points = [p for p in puzzle_input if p[0] > min_x and p[0] < max_x and p[1] > min_y and p[1] < max_y]
            if len(intersecting_points) > 0:
                continue
            intersecting_points = [p for p in sub_points if p[0] > min_x and p[0] < max_x and p[1] > min_y and p[1] < max_y]
            if len(intersecting_points) > 0:
                continue
            area = get_area(a, b)
            if area > result:
                result = area

    return result


def test():
    part_1_sample_result = 50
    part_2_sample_result = 24
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
