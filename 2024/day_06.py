"""Day 6"""

import re

from common import get_puzzle_input

PUZZLE_INPUT = get_puzzle_input()

dir_map = {
    (0, -1): "^",
    (1, 0): ">",
    (0, 1): "v",
    (-1, 0): "<",
}


def print_map(guard_map):
    print("\n".join(["".join(l) for l in guard_map]))


def find_guard(guard_map):
    for y, l in enumerate(guard_map):
        for x, c in enumerate(l):
            if c == "^":
                return (x, y)
    return (-1, -1)


def is_loop(guard_map):
    guard_facing = (0, -1)
    guard_pos = find_guard(guard_map)
    history = set()

    while True:
        new_guard_pos = (guard_pos[0] + guard_facing[0], guard_pos[1] + guard_facing[1])
        if  new_guard_pos[0] < 0 or new_guard_pos[0] >= len(guard_map[0])\
            or new_guard_pos[1] < 0 or new_guard_pos[1] >= len(guard_map):
            guard_map[guard_pos[1]][guard_pos[0]] = dir_map[guard_facing]
            break
        new_c = guard_map[new_guard_pos[1]][new_guard_pos[0]]
        if new_c == "#":
            guard_facing = (-guard_facing[1], guard_facing[0])
        else:
            guard_map[guard_pos[1]][guard_pos[0]] = dir_map[guard_facing]
            guard_pos = new_guard_pos
            if (guard_pos, guard_facing) in history:
                return (True, guard_map)
            history.add((guard_pos, guard_facing))
    return (False, guard_map)


guard_map = [list(l) for l in PUZZLE_INPUT.split("\n")]
start_pos = find_guard(guard_map)

result_map = is_loop(guard_map)[1]
print(len(re.findall(r"X", "".join(["".join(l) for l in result_map]).replace("^", "X").replace(">", "X").replace("v", "X").replace("<", "X"))))

guard_map = [list(l) for l in PUZZLE_INPUT.split("\n")]
travel_map = [[re.sub(r"[\^>v<]", "X", c) for c in l] for l in result_map]
travel_map[start_pos[1]][start_pos[0]] = "^"
options = []

for y, l in enumerate(travel_map):
    for x, c in enumerate(l):
        if c == "X":
            test_map = [[c for c in l] for l in guard_map]
            test_map[y][x] = "#"
            if is_loop(test_map)[0]:
                options.append((x, y))
print(len(set(options)))
