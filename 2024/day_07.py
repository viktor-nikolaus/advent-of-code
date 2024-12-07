"""Day 7"""

from common import get_puzzle_input

PUZZLE_INPUT = get_puzzle_input()

def is_valid_2(res, numbers):
    return is_valid_x(res, numbers, 2)

def is_valid_3(res, numbers):
    return is_valid_x(res, numbers, 3)

def is_valid_x(res, numbers, base):
    for i in range(pow(base, len(numbers) - 1)):
        test = numbers[0]
        for j, n in enumerate(numbers[1:]):
            match (int(i / pow(base, j))) % base:
                case 0:
                    test += n
                case 1:
                    test *= n
                case 2:
                    test = int(f"{test}{n}")
            if test > res:
                test = -1
                break
        if test == res:
            return True
    return False

lines = [(int(l[0]), [int(d) for d in l[1].split(" ")]) for l in [l.split(": ") for l in PUZZLE_INPUT.split("\n")]]

total = sum(l[0] for l in lines if is_valid_2(*l))
print(total)

total = sum(l[0] for l in lines if is_valid_3(*l))
print(total)
