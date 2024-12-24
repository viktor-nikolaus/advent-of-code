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


def test_bit(wire_input_dict, bit, max_bit):
    max_error = 0
    for y in range(4):
        for x in range(4):
            wire_status_dict = {f"x{b:02d}": 0 for b in range(max_bit)}\
                            | {f"y{b:02d}": 0 for b in range(max_bit)}
            wire_status_dict[f"x{bit:02d}"] = (x >> 1) & 0b1
            wire_status_dict[f"y{bit:02d}"] = (y >> 1) & 0b1
            if bit > 0:
                wire_status_dict[f"x{bit-1:02d}"] = x & 0b1
                wire_status_dict[f"y{bit-1:02d}"] = y & 0b1
            x_v = x << bit >> 1
            y_v = y << bit >> 1
            out = calculate_output(wire_status_dict, wire_input_dict)
            max_error = max(max_error, abs(out - x_v - y_v))
    return max_error


def get_all_wires(wire_input_dict, wire):
    wires = [wire]
    p = 0
    while p < len(wires):
        if wires[p] not in wire_input_dict:
            p += 1
            continue
        a, _, b = wire_input_dict[wires[p]]
        if a not in wires:
            wires.append(a)
        if b not in wires:
            wires.append(b)
        p += 1
    return set(wires)


def is_loop(wire_input_dict, test_wires):
    wires = set()
    for w in test_wires:
        w_in_1, _, w_in_2 = wire_input_dict[w]
        wires.update(get_all_wires(wire_input_dict, w_in_1))
        wires.update(get_all_wires(wire_input_dict, w_in_2))
    return any(w in wires for w in test_wires)


def create_swap_dict(wire_input_dict, swap):
    new_dict = dict(wire_input_dict.items())
    new_dict[swap[0]], new_dict[swap[1]] = (new_dict[swap[1]], new_dict[swap[0]])
    return new_dict


def test_swap(wire_input_dict, wire1, wire2, max_b):
    test_wire_input_dict = create_swap_dict(wire_input_dict, (wire1, wire2))
    if is_loop(test_wire_input_dict, [wire1, wire2]):
        return False
    total_error = 0
    max_input_b = max(int(w[1:]) for w in wire_input_dict if w.startswith("z"))
    for b in range(max_b + 1):
        total_error += test_bit(test_wire_input_dict, b, max_input_b)
    return total_error


def get_wire_string(wire_input_dict, wire):
    if wire not in wire_input_dict:
        return wire
    w1, op, w2 = wire_input_dict[wire]
    w2, w1 = sorted([get_wire_string(wire_input_dict, w1), get_wire_string(wire_input_dict, w2)])
    return f"({w1} {op} {w2})"


def part_1(puzzle_input):
    wire_status_dict, wire_input_dict = parse_input(puzzle_input)
    return calculate_output(copy_dict(wire_status_dict), wire_input_dict)


# TODO: needs cleanup
def part_2(puzzle_input):
    _, wire_input_dict = parse_input(puzzle_input)

    # manually checked for swaps in output
    swap_configuration = {("z22", "hwq"), ("z08", "thm"), ("z29", "gbs"), ("wss", "wrm")}
    # for s in swap_configuration:
    #     wire_input_dict = create_swap_dict(wire_input_dict, s)

    # for w in sorted((w for w in wire_input_dict if w.startswith("z"))):
    #     print(f"{w} = " + get_wire_string(wire_input_dict, w))
    # exit()
    # error_wires = {}
    # possible_swaps = {tuple(sorted([a, b])) for a in error_wires for b in error_wires if a != b}
    # possible_swaps = {s for s in possible_swaps if not is_loop(wire_input_dict, s)}
    # possible_swap_configurations = {(a, b, c, d) for a in possible_swaps for b in possible_swaps for c in possible_swaps for d in possible_swaps if len(set(a + b + c + d)) == 8}
    # possible_swap_configurations = {sc for sc in possible_swap_configurations if ("wrm", "wss") in sc and ("bfq", "grd") in sc}
    possible_swap_configurations = [swap_configuration]
    max_b = max(int(w[1:]) for w in wire_input_dict if w.startswith("z"))
    for sc in possible_swap_configurations:
        print(sc)
        wid_copy = dict(wire_input_dict.items())
        for s in sc:
            wid_copy = create_swap_dict(wid_copy, s)
        correct = True
        for b in range(max_b):
            if test_bit(wid_copy, b, max_b) > 0:
                correct = False
                break
        if correct:
            print("Found", sc)
            return ",".join(sorted([w for s in sc for w in s]))
    exit()

    # safe_wires = set()
    # error_wires = {}
    # error = 0
    # max_b = max(int(w[1:]) for w in wire_input_dict if w.startswith("z"))
    # for b in range(max_b):
    #     z_wire = f"z{b:02d}"
    #     new_error = test_bit(wire_input_dict, b, max_b)
    #     if new_error == error:
    #         safe_wires.update(get_all_wires(wire_input_dict, z_wire))
    #     else:
    #         print("Error Bit: ", b)
    #         test_wires = get_all_wires(wire_input_dict, z_wire) - safe_wires
    #         test_wires = [w for w in test_wires if not w.startswith("x") and not w.startswith("y")]
    #         error_wires[new_error - error] = test_wires
    #     error = new_error

    # swaps = []
    # for e in sorted([e for e in error_wires if e > 0]):
    #     l1 = error_wires[e]
    #     l2 = error_wires[-e]
    #     possible_swaps = {s for s in {(a, b) for a in l1 for b in l2} if not is_loop(wire_input_dict, list(s))}
    #     swap_error_dict = {s: test_swap(wire_input_dict, *s, max_b) for s in possible_swaps}
    #     swaps.append(min(swap_error_dict.items(), key=lambda e: e[1])[0])

    # wire_input_dict_copy = dict(wire_input_dict)
    # for s in swaps:
    #     wire_input_dict_copy = create_swap_dict(wire_input_dict_copy, s)
    # for b in range(max_b):
    #     error = test_bit(wire_input_dict_copy, b, max_b)
    #     print(error)
    # print(swaps)
    exit()

    return ""


def test():
    part_1_sample_1_result = 4
    part_1_sample_2_result = 2024
    result = True
    result &= test_sample_input(1, 1, part_1_sample_1_result, part_1)
    result &= test_sample_input(2, 1, part_1_sample_2_result, part_1)
    return result


def main():
    puzzle_input = get_puzzle_input()
    print("Part 1:", part_1(puzzle_input))
    print("Part 2:", part_2(puzzle_input))


if __name__ == "__main__":
    if test():
        main()
