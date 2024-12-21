"""Day 21"""

from common import get_puzzle_input, test_sample_input


def generate_directions(start, end, illegal_positions):
    dx = end[0] - start[0]
    dy = end[1] - start[1]
    sequences = set()
    if (start[0] + dx, start[1]) not in illegal_positions:
        sequences.add((">" if dx > 0 else "<") * abs(dx) + ("v" if dy > 0 else "^") * abs(dy))
    if (start[0], start[1] + dy) not in illegal_positions:
        sequences.add(("v" if dy > 0 else "^") * abs(dy) + (">" if dx > 0 else "<") * abs(dx))
    if len(sequences) > 1:
        max_cost = max(DIRECTION_KEY_COST[s[0]] for s in sequences)
        sequences = {s for s in sequences if DIRECTION_KEY_COST[s[0]] == max_cost}
    return list(sorted(sequences))[0]


NUMERIC_KEYPAD = [
    ["7", "8", "9"],
    ["4", "5", "6"],
    ["1", "2", "3"],
    [None, "0", "A"]
]

NUMERIC_KEYPAD_POSITIONS = {c: (x, y) for y, l in enumerate(NUMERIC_KEYPAD) for x, c in enumerate(l)}

DIRECTIONAL_KEYPAD = [
    [None, "^", "A"],
    ["<", "v", ">"]
]

DIRECTIONAL_KEYPAD_POSITIONS = {c: (x, y) for y, l in enumerate(DIRECTIONAL_KEYPAD) for x, c in enumerate(l)}

DIRECTION_KEY_COST = {
    "A": 0,
    "^": 1.5,
    ">": 1,
    "v": 2,
    "<": 3
}

DIRECTION_POINTS_TO_SEQUENCE_MAPPING = {(start, end): generate_directions(start, end, [DIRECTIONAL_KEYPAD_POSITIONS[None]]) for s_key, start in DIRECTIONAL_KEYPAD_POSITIONS.items() for e_key, end in DIRECTIONAL_KEYPAD_POSITIONS.items() if s_key is not None and e_key is not None}


def convert_to_input_sequence(key_positions, output):
    empty_position = key_positions[None]
    current_key = "A"
    directions = []
    for c in output:
        cur_pos = key_positions[current_key]
        tar_pos = key_positions[c]
        if key_positions == DIRECTIONAL_KEYPAD_POSITIONS:
            cur_directions = DIRECTION_POINTS_TO_SEQUENCE_MAPPING[(cur_pos, tar_pos)] + "A"
        else:
            cur_directions = generate_directions(cur_pos, tar_pos, [empty_position]) + "A"
        directions.append(cur_directions)
        current_key = c
    return "".join(directions)


def split_sequence_and_count(input_sequence):
    sequence_groups = {}
    for s in input_sequence.split("A")[0:-1]:
        s += "A"
        if s not in sequence_groups:
            sequence_groups[s] = 0
        sequence_groups[s] += 1
    return sequence_groups


def part_1(puzzle_input):
    complexity_sum = 0
    for code in puzzle_input.split("\n"):
        # print("Initial", code)
        input1 = convert_to_input_sequence(NUMERIC_KEYPAD_POSITIONS, code)
        # print("Robot 1", input1)
        input2 = convert_to_input_sequence(DIRECTIONAL_KEYPAD_POSITIONS, input1)
        # print("Robot 2", input2)
        input3 = convert_to_input_sequence(DIRECTIONAL_KEYPAD_POSITIONS, input2)
        # print("Robot 3", input3)
        complexity_sum += int(code[0:-1]) * len(input3)
    return complexity_sum


def part_2(puzzle_input, robots):
    complexity_sum = 0
    for code in puzzle_input.split("\n"):
        input_sequence = convert_to_input_sequence(NUMERIC_KEYPAD_POSITIONS, code)
        input_sequences = split_sequence_and_count(input_sequence)
        for _ in range(robots):
            new_input_sequences = {}
            for s, sc in input_sequences.items():
                subsequence = convert_to_input_sequence(DIRECTIONAL_KEYPAD_POSITIONS, s)
                g = split_sequence_and_count(subsequence)
                for i, c in g.items():
                    if i not in new_input_sequences:
                        new_input_sequences[i] = 0
                    new_input_sequences[i] += c * sc
            input_sequences = new_input_sequences
        f = int(code[0:-1])
        complexity_sum += f * sum(len(k) * v for k, v in input_sequences.items())
    return complexity_sum


def test():
    part_1_sample_result = 126384
    part_2_sample_result = 154115708116294
    result = True
    result &= test_sample_input(1, 1, part_1_sample_result, part_1)
    result &= test_sample_input(1, 2, part_1_sample_result, part_2, [2])
    result &= test_sample_input(1, 2, part_2_sample_result, part_2, [25])
    return result


def main():
    puzzle_input = get_puzzle_input()
    print("Part 1:", part_1(puzzle_input))
    print("Part 2:", part_2(puzzle_input, 25))


if __name__ == "__main__":
    if test():
        main()
