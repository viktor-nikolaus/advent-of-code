"""Day 2"""

from common import get_puzzle_input, test_sample_input


def parse_input(puzzle_input: str):
    return [[int(i) for i in l] for l in puzzle_input.split("\n")]


def part_1(puzzle_input):
    battery_banks = parse_input(puzzle_input)
    result = 0
    for bank in battery_banks:
        max_battery = max(bank)
        max_bat_index = bank.index(max_battery)
        remaining_batteries = bank[max_bat_index + 1:]
        flip = False
        if len(remaining_batteries) == 0:
            flip = True
            remaining_batteries = bank[0:max_bat_index]
        second_battery = max(remaining_batteries)
        if flip:
            joltage = second_battery * 10 + max_battery
        else:
            joltage = max_battery * 10 + second_battery
        result += joltage
    return result


def part_2(puzzle_input):
    return 0


def test():
    part_1_sample_result = 357
    part_2_sample_result = 0
    result = True
    result &= test_sample_input(1, 1, part_1_sample_result, part_1)
    result &= test_sample_input(1, 2, part_2_sample_result, part_2)
    return result


def main():
    puzzle_input = get_puzzle_input()
    print("Part 1:", part_1(puzzle_input))
    print("Part 2:", part_2(puzzle_input))


if __name__ == "__main__":
    if test():
        main()
