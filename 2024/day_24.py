"""Day 24"""

from common import get_puzzle_input, test_sample_input


def parse_input(puzzle_input):
    wire_status_dict, _, wire_input_dict = puzzle_input.partition("\n\n")
    wire_status_dict = {wire: int(value) for wire, _, value in [l.partition(": ") for l in wire_status_dict.split("\n")]}
    wire_input_dict = {wire: tuple(input_gate.split(" ")) for input_gate, _, wire in [l.partition(" -> ") for l in wire_input_dict.split("\n")]}
    return (wire_status_dict, wire_input_dict)


def copy_dict(dictionary):
    return dict(dictionary.items())


def calculate(param1, operation, param2):
    match(operation):
        case "AND":
            return param1 & param2
        case "OR":
            return param1 | param2
        case "XOR":
            return param1 ^ param2
    raise Exception(f"Invalid operation: {operation}")


def calculate_output(wire_status_dict, wire_input_dict):
    queue = [w for w in wire_input_dict if w.startswith("z")]
    while len(queue) > 0:
        w = queue[0]
        w_in_1 = wire_input_dict[w][0]
        w_in_2 = wire_input_dict[w][2]
        w_in_op = wire_input_dict[w][1]
        if w_in_1 in wire_status_dict and w_in_2 in wire_status_dict:
            wire_status_dict[w] = calculate(wire_status_dict[w_in_1], w_in_op, wire_status_dict[w_in_2])
            queue.pop(0)
        else:
            if w_in_1 not in queue and w_in_1 not in wire_status_dict:
                queue.insert(0, w_in_1)
            if w_in_2 not in queue and w_in_2 not in wire_status_dict:
                queue.insert(0, w_in_2)
    result = 0
    for w, v in wire_status_dict.items():
        if w.startswith("z"):
            result |= v << int(w[1:])
    return result


def part_1(puzzle_input):
    wire_status_dict, wire_input_dict = parse_input(puzzle_input)
    return calculate_output(copy_dict(wire_status_dict), wire_input_dict)


def part_2(puzzle_input):
    return ""


def test():
    part_1_sample_1_result = 4
    part_1_sample_2_result = 2024
    part_2_sample_result = ""
    result = True
    result &= test_sample_input(1, 1, part_1_sample_1_result, part_1)
    result &= test_sample_input(2, 1, part_1_sample_2_result, part_1)
    result &= test_sample_input(1, 2, part_2_sample_result, part_2)
    return result


def main():
    puzzle_input = get_puzzle_input()
    print("Part 1:", part_1(puzzle_input))
    print("Part 2:", part_2(puzzle_input))


if __name__ == "__main__":
    if test():
        main()
