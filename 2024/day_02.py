"""Day 2"""

from common import get_puzzle_input

PUZZLE_INPUT = get_puzzle_input()

def is_report_safe(levels):
    inc = True
    dec = True
    safe = True
    for i in range(1, len(levels)):
        diff = abs(levels[i] - levels[i - 1])
        if diff < 1 or diff > 3:
            safe = False
        if levels[i] > levels[i - 1]:
            dec = False
        if levels[i] < levels[i - 1]:
            inc = False
        if not safe or (not dec and not inc):
            break
    return safe and (dec or inc)

safe_levels = 0
for line in PUZZLE_INPUT.split("\n"):
    if len(line) == 0:
        continue
    levels = [int(l) for l in line.split(" ")]
    if is_report_safe(levels):
        safe_levels += 1
print(safe_levels)

safe_levels = 0
for line in PUZZLE_INPUT.split("\n"):
    if len(line) == 0:
        continue
    levels = [int(l) for l in line.split(" ")]
    safe = is_report_safe(levels)
    if safe:
        safe_levels += 1
    else:
        for i in range(len(levels)):
            sub_levels = [l for j, l in enumerate(levels) if j != i]
            if is_report_safe(sub_levels):
                safe_levels += 1
                break
print(safe_levels)
