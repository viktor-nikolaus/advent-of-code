"""Day 8"""

import math

from common import get_puzzle_input, test_sample_input


def parse_input(puzzle_input: str):
    return [tuple([int(i) for i in l.split(",")]) for l in puzzle_input.split("\n")]


def get_sorted_distances(boxes):
    distances = {}
    for i in range(len(boxes)):
        for j in range(i + 1, len(boxes)):
            k = (i, j)
            delta = (boxes[i][0] - boxes[j][0],
                     boxes[i][1] - boxes[j][1],
                     boxes[i][2] - boxes[j][2])
            distances[k] = (delta[0] * delta[0]
                          + delta[1] * delta[1]
                          + delta[2] * delta[2])
    distances = sorted(distances.items(), key=lambda e: e[1])
    return distances


def connect_boxes(circuits, k):
    cl = [c for c in circuits if k[0] in c or k[1] in c]
    if len(cl) == 0:
        c = set(k)
        circuits.append(c)
    elif len(cl) == 1:
        c = cl[0]
        c.add(k[0])
        c.add(k[1])
    else: # > 1
        cn = set()
        for c in cl:
            circuits.remove(c)
            cn = cn.union(c)
        circuits.append(cn)


def part_1(puzzle_input, num_connections):
    boxes = parse_input(puzzle_input)
    distances = get_sorted_distances(boxes)
    circuits = []
    n = 0
    for k, d in distances:
        connect_boxes(circuits, k)
        n += 1
        if n >= num_connections:
            break
    result = 1
    circuits = sorted(circuits, key=lambda c: len(c), reverse=True)
    for c in circuits[0:3]:
        result *= len(c)

    return result


def part_2(puzzle_input):
    boxes = parse_input(puzzle_input)
    distances = get_sorted_distances(boxes)
    circuits = []
    for k, d in distances:
        connect_boxes(circuits, k)
        if len(circuits) == 1 and len(circuits[0]) == len(boxes):
            return boxes[k[0]][0] * boxes[k[1]][0]
    return -1


def test():
    part_1_sample_result = 40
    part_2_sample_result = 25272
    result = True
    result &= test_sample_input(1, 1, part_1_sample_result, part_1, [10])
    result &= test_sample_input(1, 2, part_2_sample_result, part_2)
    return result


def main():
    puzzle_input = get_puzzle_input()
    print("Part 1:", part_1(puzzle_input, 1000))
    print("Part 2:", part_2(puzzle_input))


if __name__ == "__main__":
    if test():
        main()
