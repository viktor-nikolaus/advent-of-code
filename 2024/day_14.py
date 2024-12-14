"""Day 14"""

from common import get_puzzle_input

PUZZLE_INPUT = get_puzzle_input()


def parse_input(puzzle_input):
    result = []
    for l in puzzle_input.split("\n"):
        p, _, v = l.partition(" ")
        p = p.partition("=")[2].partition(",")
        v = v.partition("=")[2].partition(",")
        p = (int(p[0]), int(p[2]))
        v = (int(v[0]), int(v[2]))
        result.append((p, v))
    return result


def get_safety_factor(robot_positions):
    q1 = sum(1 for r in robot_positions if r[0] < (WIDTH - 1) / 2 and r[1] < (HEIGHT - 1) / 2)
    q2 = sum(1 for r in robot_positions if r[0] > (WIDTH - 1) / 2 and r[1] < (HEIGHT - 1) / 2)
    q3 = sum(1 for r in robot_positions if r[0] < (WIDTH - 1) / 2 and r[1] > (HEIGHT - 1) / 2)
    q4 = sum(1 for r in robot_positions if r[0] > (WIDTH - 1) / 2 and r[1] > (HEIGHT - 1) / 2)
    return q1 * q2 * q3 * q4


def print_map(robot_positions):
    for y in range(HEIGHT):
        for x in range(WIDTH):
            c = len([r for r in robot_positions if r == (x, y)])
            print(str(c) if c > 0 else ".", end="")
        print()


def create_easter_egg_positions():
    result = []
    result.append(((WIDTH - 1) / 2, 0))
    for y in range(1, HEIGHT - 1):
        result.append(((WIDTH - 1) / 2 - y, y))
        result.append(((WIDTH - 1) / 2 + y, y))
    result.append(((WIDTH - 1) / 2, HEIGHT - 1))
    return result


def do_positions_match(robot_positions, easter_egg_positions):
    return all(r in easter_egg_positions for r in robot_positions) and\
        all(e in robot_positions for e in easter_egg_positions)


def ggt(a, b):
    m = a if a < b else b
    t = a + b - m
    while t > 0:
        t -= m
        if 0 < t < m:
            m, t = (t, m)
    return m


def kgv(a, b):
    return int(a * b / ggt(a, b))


def get_cycle_time(v):
    ct_x = abs(WIDTH * v[1])
    ct_y = abs(HEIGHT * v[0])
    return kgv(ct_x, ct_y)


def get_robot_pos(robot, time):
    return ((robot[0][0] + robot[1][0] * time) % WIDTH, (robot[0][1] + robot[1][1] * time) % HEIGHT)


def is_easter_egg(dt):
    positions = {get_robot_pos(r, dt) for r in ROBOTS}
    pos_str = "\n".join(["".join(c) for c in [["1" if (x, y) in positions else "0" for x in range(WIDTH)] for y in range(HEIGHT)]])
    return "1111111111" in pos_str


def part_1():
    dt = 100 # seconds
    robot_positions = [get_robot_pos(r, dt) for r in ROBOTS]
    #print_map(robot_positions)
    print(get_safety_factor(robot_positions))


def part_2():
    dt = 0
    easter_egg = False
    while not easter_egg:
        dt += 1
        easter_egg = is_easter_egg(dt)
    print(dt)


WIDTH = 101
HEIGHT = 103
# WIDTH = 11
# HEIGHT = 7
ROBOTS = parse_input(PUZZLE_INPUT)

# print_map([get_robot_pos(r, 8270) for r in ROBOTS])
# exit()

part_1()
part_2()
