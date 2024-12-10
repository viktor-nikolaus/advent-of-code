"""Day 10"""

from common import get_puzzle_input

PUZZLE_INPUT = get_puzzle_input()


def get_trail_ends(topo_map, pos):
    cur_val = topo_map[pos[1]][pos[0]]
    if cur_val == 9:
        return [pos]
    trail_ends = []
    if 0 < pos[0]:
        if cur_val + 1 == topo_map[pos[1]][pos[0] - 1]:
            trail_ends += get_trail_ends(topo_map, (pos[0] - 1, pos[1]))
    if pos[0] < len(topo_map[0]) - 1:
        if cur_val + 1 == topo_map[pos[1]][pos[0] + 1]:
            trail_ends += get_trail_ends(topo_map, (pos[0] + 1, pos[1]))
    if 0 < pos[1]:
        if cur_val + 1 == topo_map[pos[1] - 1][pos[0]]:
            trail_ends += get_trail_ends(topo_map, (pos[0], pos[1] - 1))
    if pos[1] < len(topo_map) - 1:
        if cur_val + 1 == topo_map[pos[1] + 1][pos[0]]:
            trail_ends += get_trail_ends(topo_map, (pos[0], pos[1] + 1))
    return list(set(trail_ends))


def get_trail_score(topo_map, pos):
    cur_val = topo_map[pos[1]][pos[0]]
    if cur_val == 9:
        return 1
    trail_score = 0
    if 0 < pos[0]:
        if cur_val + 1 == topo_map[pos[1]][pos[0] - 1]:
            trail_score += get_trail_score(topo_map, (pos[0] - 1, pos[1]))
    if pos[0] < len(topo_map[0]) - 1:
        if cur_val + 1 == topo_map[pos[1]][pos[0] + 1]:
            trail_score += get_trail_score(topo_map, (pos[0] + 1, pos[1]))
    if 0 < pos[1]:
        if cur_val + 1 == topo_map[pos[1] - 1][pos[0]]:
            trail_score += get_trail_score(topo_map, (pos[0], pos[1] - 1))
    if pos[1] < len(topo_map) - 1:
        if cur_val + 1 == topo_map[pos[1] + 1][pos[0]]:
            trail_score += get_trail_score(topo_map, (pos[0], pos[1] + 1))
    return trail_score


topo_map = [[int(c) for c in list(l)] for l in PUZZLE_INPUT.split("\n")]

trailheads = []
for y, l in enumerate(topo_map):
    for x, c in enumerate(l):
        if c == 0:
            trailheads.append((x, y))

total = 0
for th in trailheads:
    score = len(get_trail_ends(topo_map, th))
    total += score
print(total)

total = 0
for th in trailheads:
    score = get_trail_score(topo_map, th)
    total += score
print(total)
