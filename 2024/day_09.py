"""Day 9"""

from common import get_puzzle_input

PUZZLE_INPUT = get_puzzle_input()


def create_filesystem(input):
    filesystem = []
    is_file = True
    file_id = 0
    for c in input:
        if is_file:
            filesystem.append({"id": file_id, "length": int(c)})
            file_id += 1
        else:
            filesystem.append({"id": -1, "length": int(c)})
        is_file = not is_file
    return filesystem


def part_1(filesystem):
    space_pointer = 1
    data_pointer = len(filesystem) - 1
    while space_pointer < data_pointer:
        fs_space = filesystem[space_pointer]
        fs_data = filesystem[data_pointer]
        if fs_space["id"] == -1 and fs_data["id"] >= 0:
            if fs_space["length"] > fs_data["length"]:
                filesystem.insert(space_pointer, {"id": fs_data["id"], "length": fs_data["length"]})
                fs_space["length"] -= fs_data["length"]
                fs_data["id"] = -1
                space_pointer += 1
            elif fs_space["length"] < fs_data["length"]:
                fs_space["id"] = fs_data["id"]
                fs_data["length"] -= fs_space["length"]
                space_pointer += 1
            else: # equal length
                fs_space["id"] = fs_data["id"]
                fs_data["length"] -= fs_space["length"]
                space_pointer += 1
                data_pointer -= 1
        else:
            if fs_space["id"] >= 0:
                space_pointer += 1
            if fs_data["id"] < 0:
                data_pointer -= 1


def part_2(filesystem):
    data_pointer = len(filesystem) - 1
    while data_pointer > 0:
        fs_data = filesystem[data_pointer]
        if fs_data["id"] >= 0:
            for space_pointer in range(data_pointer):
                fs_space = filesystem[space_pointer]
                if fs_space["id"] >= 0:
                    continue
                if fs_space["length"] < fs_data["length"]:
                    continue
                if fs_space["length"] > fs_data["length"]:
                    filesystem.insert(space_pointer, {"id": fs_data["id"], "length": fs_data["length"]})
                    fs_space["length"] -= fs_data["length"]
                    fs_data["id"] = -1
                    data_pointer += 1
                    break
                else: # equal length
                    fs_space["id"] = fs_data["id"]
                    fs_data["id"] = -1
                    break
            data_pointer -= 1
        else:
            data_pointer -= 1


def filesystem_checksum(filesystem):
    fs_checksum = 0
    pos = 0
    for e in filesystem:
        for _ in range(e["length"]):
            if e["id"] >= 0:
                fs_checksum += pos * e["id"]
            pos += 1
    return fs_checksum


def print_filesystem(filesystem):
    for e in filesystem:
        print((str(e["id"]) if e["id"] >= 0 else ".") * e["length"], end="")
    print()


filesystem = create_filesystem(PUZZLE_INPUT)
part_1(filesystem)
filesystem = [e for e in filesystem if e["id"] >= 0 and e["length"] > 0]
fs_checksum = filesystem_checksum(filesystem)
print(fs_checksum)

filesystem = create_filesystem(PUZZLE_INPUT)
part_2(filesystem)
filesystem = [e for e in filesystem if e["length"] > 0]
fs_checksum = filesystem_checksum(filesystem)
print(fs_checksum)
