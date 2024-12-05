"""Day 5"""

from common.common import get_puzzle_input

PUZZLE_INPUT = get_puzzle_input()

[rules, updates] = PUZZLE_INPUT.split("\n\n")
rules = [(int(e[0]), int(e[1])) for e in [l.split("|") for l in rules.split("\n")]]
updates = [[int(u) for u in l.split(",")] for l in updates.split("\n")]

def is_update_valid(update, rules):
    for i, p in enumerate(update):
        before = update[0:i] if i>0 else []
        after = update[i+1:] if i+1<len(update) else []
        if any(r[1] in before for r in [r for r in rules if r[0] == p]):
            return False
        if any(r[0] in after for r in [r for r in rules if r[1] == p]):
            return False
    return True

def fix_update(update, rules):
    rel_rules = [r for r in rules if r[0] in update and r[1] in update]
    p_dict = {p: {"before": [r[0] for r in rel_rules if r[1] == p], "after": [r[1] for r in rel_rules if r[0] == p]} for p in update}
    sorted_update = list(reversed(sorted(update, key=lambda p: len(p_dict[p]["after"]))))
    return list(sorted(sorted_update, key=lambda p: len(p_dict[p]["before"])))

def get_middle_page(update):
    return update[int(len(update) / 2)]

total = 0
for update in updates:
    if is_update_valid(update, rules):
        total += get_middle_page(update)
print(total)

total = 0
for update in updates:
    if not is_update_valid(update, rules):
        total += get_middle_page(fix_update(update, rules))
print(total)
