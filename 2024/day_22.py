"""Day 22"""

from common import get_puzzle_input, test_sample_input


def mix_and_prune(number, other):
    return (int(number) ^ int(other)) & 0xFFFFFF


def generate_secret_number(number, iterations):
    secret_number = number
    for _ in range(iterations):
        new_secret_number = secret_number
        new_secret_number = mix_and_prune(new_secret_number, new_secret_number << 6)
        new_secret_number = mix_and_prune(new_secret_number, new_secret_number >> 5)
        new_secret_number = mix_and_prune(new_secret_number, new_secret_number << 11)
        secret_number = new_secret_number
    return secret_number


def part_1(puzzle_input, iterations):
    return sum(generate_secret_number(int(l), iterations) for l in puzzle_input.split("\n"))


def part_2(puzzle_input):
    return ""


def test():
    part_1_sample_result = 37327623
    part_2_sample_result = ""
    result = True
    result &= test_sample_input(1, 1, part_1_sample_result, part_1, [2000])
    result &= test_sample_input(1, 2, part_2_sample_result, part_2)
    return result


def main():
    puzzle_input = get_puzzle_input()
    print("Part 1:", part_1(puzzle_input, 2000))
    print("Part 2:", part_2(puzzle_input))


if __name__ == "__main__":
    if test():
        main()
