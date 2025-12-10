"""Day 10"""

from common import get_puzzle_input, test_sample_input


def parse_lights(text: str):
    if not text.startswith("[") or not text.endswith("]"):
        raise ValueError()
    return tuple([int(c == "#") for c in text[1:-1]])


def parse_buttons(texts: list[str]):
    buttons = []
    for text in texts:
        if not text.startswith("(") or not text.endswith(")"):
            raise ValueError()
        buttons.append(tuple([int(c) for c in text[1:-1].split(",")]))
    return buttons


def parse_joltage(text: str):
    if not text.startswith("{") or not text.endswith("}"):
        raise ValueError()
    return tuple([int(c) for c in text[1:-1].split(",")])


def parse_input(puzzle_input: str):
    configs = [l.split(" ") for l in puzzle_input.split("\n")]
    configs = [(parse_lights(c[0]), parse_buttons(c[1:-1]), parse_joltage(c[-1])) for c in configs]
    return configs


def convert_button_to_binary(button: list[int], length: int):
    return tuple([int(i in button) for i in range(length)])


def xor(a: tuple[int], b: tuple[int]):
    if len(a) != len(b):
        raise ValueError()
    return tuple([int(a[i] != b[i]) for i in range(len(a))])


def get_minimum_buttons(machine):
    lights, buttons, joltage = machine
    buttons = [convert_button_to_binary(b, len(lights)) for b in buttons]
    memo = {convert_button_to_binary([], len(lights)): []}
    memo.update({b: [i] for i, b in enumerate(buttons)})
    while lights not in memo:
        for state in list(memo.keys()):
            for b_i, button in enumerate(buttons):
                new_state = xor(state, button)
                if new_state not in memo:
                    memo[new_state] = memo[state].copy()
                    memo[new_state].append(b_i)
    return memo[lights]


def part_1(puzzle_input):
    machines = parse_input(puzzle_input)
    result = 0
    for m in machines:
        result += len(get_minimum_buttons(m))

    return result


def part_2(puzzle_input):
    puzzle_input = parse_input(puzzle_input)

    result = 0

    return result


def test():
    part_1_sample_result = 7
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
