"""Day 11"""

from common import get_puzzle_input, test_sample_input


def parse_input(puzzle_input: str):
    lines = [l.split(":") for l in puzzle_input.split("\n")]
    return {l[0]: set(l[1].strip().split(" ")) for l in lines}


def part_1(puzzle_input):
    puzzle_input = parse_input(puzzle_input)
    queue = ["you"]
    result = 0
    while len(queue) > 0:
        device = queue.pop(0)
        if device == "out":
            result += 1
        elif device in puzzle_input:
            for d in puzzle_input[device]:
                queue.append(d)

    return result


def get_connected_devices(connections, root_device):
    connected_devices = set()
    queue = [root_device]
    while len(queue) > 0:
        device = queue.pop(0)
        if device not in connected_devices:
            connected_devices.add(device)
            queue.append(device)
            if device in connections:
                for d in connections[device]:
                    queue.append(d)
    return connected_devices


def reverse_connections(connections):
    rev_connections = {}
    for device in connections:
        for conn in connections[device]:
            if conn not in rev_connections:
                rev_connections[conn] = set()
            rev_connections[conn].add(device)
    return rev_connections


def part_2(puzzle_input):
    puzzle_input = parse_input(puzzle_input)
    rev_connections = reverse_connections(puzzle_input)
    devices_connected_to_svr = get_connected_devices(puzzle_input, "svr")
    devices_connected_to_fft = get_connected_devices(puzzle_input, "fft")\
        .union(get_connected_devices(rev_connections, "fft"))
    devices_connected_to_dac = get_connected_devices(puzzle_input, "dac")\
        .union(get_connected_devices(rev_connections, "dac"))
    connected_devices = devices_connected_to_svr\
        .intersection(devices_connected_to_fft)\
        .intersection(devices_connected_to_dac)

    for device in list(puzzle_input.keys()):
        if device not in connected_devices:
            del puzzle_input[device]
        else:
            for conn in list(puzzle_input[device]):
                if conn not in connected_devices:
                    puzzle_input[device].remove(conn)

    rev_connections = reverse_connections(puzzle_input)
    count_map = {"out": 1}
    queue = ["out"]
    processed = set()
    while len(queue) > 0:
        queue.sort(key=lambda d: len([c for c in puzzle_input[d] if c not in processed]) if d in puzzle_input else 0)
        device = queue.pop(0)
        processed.add(device)
        if device in rev_connections:
            for conn in rev_connections[device]:
                if conn not in count_map:
                    count_map[conn] = 0
                count_map[conn] += count_map[device]
                while conn in queue:
                    queue.remove(conn)
                queue.append(conn)
    return count_map["svr"]


def test():
    part_1_sample_result = 5
    part_2_sample_result = 2
    result = True
    result &= test_sample_input(1, 1, part_1_sample_result, part_1)
    result &= test_sample_input(2, 2, part_2_sample_result, part_2)
    return result


def main():
    puzzle_input = get_puzzle_input()
    print("Part 1:", part_1(puzzle_input))
    print("Part 2:", part_2(puzzle_input))


if __name__ == "__main__":
    if test():
        main()
