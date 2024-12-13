"""Day 13"""

from common import get_puzzle_input

PUZZLE_INPUT = get_puzzle_input()


def part_1():
    total_tokens = 0
    claw_machines = [cm.split("\n") for cm in PUZZLE_INPUT.split("\n\n")]
    for cm in claw_machines:
        b_a = [l[len("Button A: "):] for l in cm if l.startswith("Button A: ")][0].split(", ")
        b_b = [l[len("Button B: "):] for l in cm if l.startswith("Button B: ")][0].split(", ")
        prize = [l[len("Prize: "):] for l in cm if l.startswith("Prize: ")][0].split(", ")
        b_a = {p[0]: int(p[1:]) for p in b_a}
        b_b = {p[0]: int(p[1:]) for p in b_b}
        prize = {p[0]: int(p[2:]) for p in prize}
        b_a = (b_a["X"], b_a["Y"])
        b_b = (b_b["X"], b_b["Y"])
        prize = (prize["X"], prize["Y"])

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
        min_tokens = min(c[0] * 3 + c[1] for c in combos)
        total_tokens += min_tokens
    print(total_tokens)


# defect
def part_2():
    total_tokens = 0
    claw_machines = [cm.split("\n") for cm in PUZZLE_INPUT.split("\n\n")]
    for cm in claw_machines:
        b_a = [l[len("Button A: "):] for l in cm if l.startswith("Button A: ")][0].split(", ")
        b_b = [l[len("Button B: "):] for l in cm if l.startswith("Button B: ")][0].split(", ")
        prize = [l[len("Prize: "):] for l in cm if l.startswith("Prize: ")][0].split(", ")
        b_a = {p[0]: int(p[1:]) for p in b_a}
        b_b = {p[0]: int(p[1:]) for p in b_b}
        prize = {p[0]: int(p[2:]) for p in prize}
        b_a = (b_a["X"], b_a["Y"])
        b_b = (b_b["X"], b_b["Y"])
        prize = (prize["X"], prize["Y"])
        prize = (prize[0] + 10000000000000, prize[1] + 10000000000000)

        if prize[0] * b_a[1] / b_a[0] == prize[1] and prize[0] / b_a[0] == int(prize[0] / b_a[0]):
            total_tokens += 3 * int(prize[0] / b_a[0])
            continue
        if prize[0] * b_b[1] / b_b[0] == prize[1] and prize[0] / b_b[0] == int(prize[0] / b_b[0]):
            total_tokens += int(prize[0] / b_b[0])
            continue
        diff_a_y = prize[1] - prize[0] * b_a[1] / b_a[0]
        diff_b_y = prize[1] - prize[0] * b_b[1] / b_b[0]
        if diff_a_y * diff_b_y > 0:
            continue
        c_a = 1
        c_b = 1
        errors = set()
        while True:
            vec = (b_a[0] * c_a + b_b[0] * c_b, b_a[1] * c_a + b_b[1] * c_b)
            diff = prize[1] - prize[0] * vec[1] / vec[0]
            if diff == 0:
                f = prize[0] / vec[0]
                total_tokens += c_a * 3 * f + c_b * f
                break
            if diff in errors:
                break
            errors.add(diff)
            if diff > 0:
                if b_a[1] / b_a[0] > b_b[1] / b_b[0]:
                    c_a += 1
                else:
                    c_b += 1
    print(total_tokens)


part_1()
part_2()
