"""Day 15"""

from common import get_puzzle_input

PUZZLE_INPUT = get_puzzle_input()

PUZZLE_MAP, _, ROBOT_MOVES = PUZZLE_INPUT.partition("\n\n")
PUZZLE_MAP = [list(l) for l in PUZZLE_MAP.split("\n")]
ROBOT_MOVES = ROBOT_MOVES.replace("\n", "")


def swap(puzzle_map, pos1, pos2):
    puzzle_map[pos1[1]][pos1[0]], puzzle_map[pos2[1]][pos2[0]] = (puzzle_map[pos2[1]][pos2[0]], puzzle_map[pos1[1]][pos1[0]])


def move(puzzle_map, pos, vec):
    new_pos = (pos[0] + vec[0], pos[1] + vec[1])
    match(puzzle_map[new_pos[1]][new_pos[0]]):
        case "O":
            move(puzzle_map, new_pos, vec)
        case "[":
            if vec[1] == 0:
                move(puzzle_map, new_pos, vec)
            else:
                move(puzzle_map, new_pos, vec)
                move(puzzle_map, (new_pos[0] + 1, new_pos[1]), vec)
        case "]":
            if vec[1] == 0:
                move(puzzle_map, new_pos, vec)
            else:
                move(puzzle_map, new_pos, vec)
                move(puzzle_map, (new_pos[0] - 1, new_pos[1]), vec)
    swap(puzzle_map, pos, new_pos)


def can_move(current_map, pos, vec):
    width = len(current_map[0])
    height = len(current_map)
    new_pos = (pos[0] + vec[0], pos[1] + vec[1])
    if 0 <= new_pos[0] < width and 0 <= new_pos[1] < height:
        match(current_map[new_pos[1]][new_pos[0]]):
            case "#":
                return False
            case ".":
                return True
            case "O":
                return can_move(current_map, new_pos, vec)
            case "[":
                if vec[1] == 0:
                    return can_move(current_map, new_pos, vec)
                return can_move(current_map, new_pos, vec)\
                    and can_move(current_map, (new_pos[0] + 1, new_pos[1]), vec)
            case "]":
                if vec[1] == 0:
                    return can_move(current_map, new_pos, vec)
                return can_move(current_map, new_pos, vec)\
                    and can_move(current_map, (new_pos[0] - 1, new_pos[1]), vec)
    return False


def find_robot(puzzle_map):
    return [(x, y) for y, l in enumerate(puzzle_map) for x, c in enumerate(l) if c == "@"][0]


def adjust_map_for_part_2(puzzle_map):
    for y, l in enumerate(puzzle_map):
        for x, c in enumerate(l):
            match(c):
                case "#":
                    puzzle_map[y][x] = "##"
                case "O":
                    puzzle_map[y][x] = "[]"
                case ".":
                    puzzle_map[y][x] = ".."
                case "@":
                    puzzle_map[y][x] = "@."
    puzzle_map = [list("".join(l)) for l in puzzle_map]
    return puzzle_map


def part_1():
    current_map = [list(l) for l in PUZZLE_MAP]
    robot_pos = find_robot(current_map)
    for m in ROBOT_MOVES:
        vec = (0, 0)
        match(m):
            case "^":
                vec = (0, -1)
            case "v":
                vec = (0, 1)
            case "<":
                vec = (-1, 0)
            case ">":
                vec = (1, 0)
        if can_move(current_map, robot_pos, vec):
            move(current_map, robot_pos, vec)
            robot_pos = (robot_pos[0] + vec[0], robot_pos[1] + vec[1])
    #print("\n".join(["".join(l) for l in current_map]))
    print(sum(y * 100 + x for y, l in enumerate(current_map) for x, c in enumerate(l) if c == "O"))


def part_2():
    current_map = [list(l) for l in PUZZLE_MAP]
    current_map = adjust_map_for_part_2(current_map)
    robot_pos = find_robot(current_map)
    for m in ROBOT_MOVES:
        vec = (0, 0)
        match(m):
            case "^":
                vec = (0, -1)
            case "v":
                vec = (0, 1)
            case "<":
                vec = (-1, 0)
            case ">":
                vec = (1, 0)
        if can_move(current_map, robot_pos, vec):
            move(current_map, robot_pos, vec)
            robot_pos = (robot_pos[0] + vec[0], robot_pos[1] + vec[1])

    #print("\n".join(["".join(l) for l in current_map]))
    print(sum(y * 100 + x for y, l in enumerate(current_map) for x, c in enumerate(l) if c == "["))


part_1()
part_2()
