"""Day 13"""

from common import get_puzzle_input

PUZZLE_INPUT = get_puzzle_input()


def parse_claw_machine(lines):
    b_a = [l[len("Button A: "):] for l in lines if l.startswith("Button A: ")][0].split(", ")
    b_b = [l[len("Button B: "):] for l in lines if l.startswith("Button B: ")][0].split(", ")
    prize = [l[len("Prize: "):] for l in lines if l.startswith("Prize: ")][0].split(", ")
    b_a = {p[0]: int(p[1:]) for p in b_a}
    b_b = {p[0]: int(p[1:]) for p in b_b}
    prize = {p[0]: int(p[2:]) for p in prize}
    b_a = (b_a["X"], b_a["Y"])
    b_b = (b_b["X"], b_b["Y"])
    prize = (prize["X"], prize["Y"])
    return (b_a, b_b, prize)


def part_1():
    total_tokens = 0
    claw_machines = [cm.split("\n") for cm in PUZZLE_INPUT.split("\n\n")]
    for cm in claw_machines:
        b_a, b_b, prize = parse_claw_machine(cm)
        combos = []
        for i in range(101):
            c_b = i
            if prize[0] < (c_b * b_b[0]) or prize[1] < (c_b * b_b[1]):
                continue
            rem = (prize[0] - (c_b * b_b[0]), prize[1] - (c_b * b_b[1]))
            c_a_x = rem[0] / b_a[0]
            c_a_y = rem[1] / b_a[1]
            if c_a_x == c_a_y and c_a_x == int(c_a_x):
                combos.append((int(c_a_x), c_b))
        if len(combos) == 0:
            continue
        print(combos)
        min_tokens = min(c[0] * 3 + c[1] for c in combos)
        total_tokens += min_tokens
    print(total_tokens)


def get_vector_factors(target, vec_a, vec_b):
    # t_x = vec_a_x * c_a + vec_b_x * c_b
    # t_x - vec_b_x * c_b = vec_a_x * c_a
    # (t_x - vec_b_x * c_b) / vec_a_x = c_a
    # (t_y - vec_b_y * c_b) / vec_a_y = c_a

    # (t_x - vec_b_x * c_b) / vec_a_x = (t_y - vec_b_y * c_b) / vec_a_y
    # (t_x - vec_b_x * c_b) * vec_a_y = (t_y - vec_b_y * c_b) * vec_a_x
    # t_x * vec_a_y - vec_b_x * c_b * vec_a_y = t_y * vec_a_x - vec_b_y * c_b * vec_a_x
    # t_x * vec_a_y - t_y * vec_a_x = vec_b_x * c_b * vec_a_y - vec_b_y * c_b * vec_a_x
    # t_x * vec_a_y - t_y * vec_a_x = (vec_b_x * vec_a_y - vec_b_y * vec_a_x) * c_b
    # (t_x * vec_a_y - t_y * vec_a_x) / (vec_b_x * vec_a_y - vec_b_y * vec_a_x) = c_b

    c_b = (target[0] * vec_a[1] - target[1] * vec_a[0]) / (vec_b[0] * vec_a[1] - vec_b[1] * vec_a[0])
    c_a1 = (target[0] - vec_b[0] * c_b) / vec_a[0]
    c_a2 = (target[1] - vec_b[1] * c_b) / vec_a[1]
    if c_a1 != c_a2 or c_a1 % 1.0 != 0.0 or c_b % 1.0 != 0.0:
        return (None, None)
    return (int(c_a1), int(c_b))


def part_2():
    total_tokens = 0
    claw_machines = [cm.split("\n") for cm in PUZZLE_INPUT.split("\n\n")]
    for cm in claw_machines:
        b_a, b_b, prize = parse_claw_machine(cm)
        prize = (prize[0] + 10000000000000, prize[1] + 10000000000000)

        c_a, c_b = get_vector_factors(prize, b_a, b_b)
        if c_a is not None and c_b is not None:
            total_tokens += c_a * 3 + c_b
    print(total_tokens)


part_1()
part_2()
