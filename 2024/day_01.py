"""Day 1"""

from common.common import get_puzzle_input

PUZZLE_INPUT = get_puzzle_input()

lines = [l.split("   ") for l in PUZZLE_INPUT.strip().split("\n")]
left = list(sorted([int(l[0]) for l in lines]))
right = list(sorted([int(l[1]) for l in lines]))

distance = 0
for i in range(len(left)):
    distance += abs(left[i] - right[i])
print(distance)

score = 0
for n in left:
    i_score = 0
    for m in right:
        if n == m:
            i_score += n
    score += i_score
print(score)
