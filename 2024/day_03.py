"""Day 3"""

import re

from common import get_puzzle_input

PUZZLE_INPUT = get_puzzle_input()

def reduce(func, start, values):
    res = start
    for v in values:
        res = func(res, v)
    return res

matches = re.findall(r"mul\((\d{1,3}),(\d{1,3})\)", PUZZLE_INPUT)
print(reduce(lambda a, b: a+b, 0, [int(m[0]) * int(m[1]) for m in matches]))

adj_input = PUZZLE_INPUT
en = True
res = 0
while len(adj_input) > 0:
    if adj_input.startswith("do()"):
        en = True
    elif adj_input.startswith("don't()"):
        en = False
    elif adj_input.startswith("mul(") and en:
        m = re.match(r"^mul\((\d{1,3}),(\d{1,3})\)", adj_input[0:30])
        if m is not None:
            res += int(m[1]) * int(m[2])
    adj_input = adj_input[1:]
print(res)
