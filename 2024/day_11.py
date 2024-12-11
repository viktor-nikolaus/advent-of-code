"""Day 11"""

from common import get_puzzle_input

PUZZLE_INPUT = get_puzzle_input()


def apply_rule(s):
    if s == 0:
        return [1]
    s_str = str(s)
    if len(s_str) % 2 == 0:
        i = int(len(s_str)/2)
        return [int(s_str[0:i]), int(s_str[i:])]
    return [s * 2024]


def blink(stone, blinks):
    new_stones = [stone]
    for _ in range(blinks):
        new_stones = [ns for s in new_stones for ns in apply_rule(s)]
    return new_stones


def blink_list(stones, blinks):
    return [ns for s in stones for ns in blink(s, blinks)]


def remap_stones(stones):
    stones_map = {}
    for s in stones:
        if s not in stones_map:
            stones_map[s] = 0
        stones_map[s] += 1
    return stones_map


def blink_list_2(stones_map, blinks):
    result = stones_map
    for _ in range(blinks):
        new_stones_map = {}
        for s, c in result.items():
            for ns in blink(s, 1):
                if ns not in new_stones_map:
                    new_stones_map[ns] = 0
                new_stones_map[ns] += c
        result = new_stones_map
    return result


def get_stone_count(stones_map):
    return sum(stones_map.values())


stones = [int(s) for s in PUZZLE_INPUT.split(" ")]

print(len(blink_list(stones, 25)))

print(get_stone_count(blink_list_2(remap_stones(stones), 75)))
