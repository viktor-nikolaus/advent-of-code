"""Day 8"""

from common import get_puzzle_input

PUZZLE_INPUT = get_puzzle_input()

PUZZLE_MAP = [list(l) for l in PUZZLE_INPUT.split("\n")]
SIZE = (len(PUZZLE_MAP[0]), len(PUZZLE_MAP))

antennas = {}
for y in range(SIZE[1]):
    for x in range(SIZE[0]):
        c = PUZZLE_MAP[y][x]
        if '0' <= c <= '9' or 'a' <= c <= 'z' or 'A' <= c <= 'Z':
            if c not in antennas:
                antennas[c] = []
            antennas[c].append((x, y))

antinodes = []
for signal, positions in antennas.items():
    for a in positions:
        for b in positions:
            if a == b:
                continue
            da = (a[0] - b[0], a[1] - b[1])
            db = (b[0] - a[0], b[1] - a[1])
            antinodes.append((a[0] + da[0], a[1] + da[1]))
            antinodes.append((b[0] + db[0], b[1] + db[1]))
antinodes = list({n for n in antinodes if 0 <= n[0] < SIZE[0] and 0 <= n[1] < SIZE[1]})
print(len(antinodes))

antinodes = []
for signal, positions in antennas.items():
    for a in positions:
        for b in positions:
            if a == b:
                continue
            da = (a[0] - b[0], a[1] - b[1])
            an = a
            while 0 <= an[0] < SIZE[0] and 0 <= an[1] < SIZE[1]:
                antinodes.append(an)
                an = (an[0] - da[0], an[1] - da[1])
            while 0 <= an[0] < SIZE[0] and 0 <= an[1] < SIZE[1]:
                antinodes.append(an)
                an = (an[0] + da[0], an[1] + da[1])
antinodes = list({n for n in antinodes if 0 <= n[0] < SIZE[0] and 0 <= n[1] < SIZE[1]})
print(len(antinodes))
