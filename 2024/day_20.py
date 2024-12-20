"""Day 20"""

from common import (copy_grid, find_first_position, get_puzzle_input, grid_at,
                    iter_grid, parse_grid, print_grid, solve_maze,
                    test_sample_input)


def create_saved_time_dict(shortcuts):
    save_time_dict = {}
    for start, end, t in sorted(shortcuts, key=lambda x: x[2]):
        if t not in save_time_dict:
            save_time_dict[t] = set()
        save_time_dict[t].add((start, end))
    return {k: len(v) for k, v in save_time_dict.items()}


def count_shortcuts(save_time_dict, min_time_saved):
    return sum(c for t, c in save_time_dict.items() if t >= min_time_saved)


def generate_cheat_diamond(picoseconds):
    size = picoseconds * 2 + 1
    center = picoseconds
    grid = [[v if v <= picoseconds else -1 for v in [abs(center - x) + abs(center - y) for x in range(size)]] for y in range(size)]
    return grid


def apply_cheat(grid, pos, cheat_grid):
    val = grid_at(grid, pos)
    shortcuts = set()
    radius = int((len(cheat_grid) - 1) / 2)
    for c_pos, c_val in iter_grid(cheat_grid):
        if c_val < 0:
            continue
        n_pos = (pos[0] - radius + c_pos[0], pos[1] - radius + c_pos[1])
        n_val = grid_at(grid, n_pos)
        if n_val is None or n_val == "#":
            continue
        shortcuts.add((pos, n_pos, n_val - val - c_val))
    return shortcuts


def part_1(puzzle_input):
    grid = parse_grid(puzzle_input)
    start = find_first_position("S", grid)
    end = find_first_position("E", grid)
    grid[end[1]][end[0]] = "."
    grid = solve_maze(grid, start)
    # print_grid(grid, 1)
    shortcuts = set()
    for y in range(1, len(grid) - 1):
        for x in range(1, len(grid[0]) - 1):
            v = grid_at(grid, (x, y))
            if v != "#":
                continue
            for dx, dy in [(1, 0), (0, 1)]:
                n_pos_1 = (x + dx, y + dy)
                n_val_1 = grid_at(grid, n_pos_1)
                n_pos_2 = (x - dx, y - dy)
                n_val_2 = grid_at(grid, n_pos_2)
                if n_val_1 != "#" and n_val_2 != "#":
                    if n_val_1 < n_val_2:
                        shortcuts.add((n_pos_1, n_pos_2, n_val_2 - n_val_1 - 2))
                    else:
                        shortcuts.add((n_pos_2, n_pos_1, n_val_1 - n_val_2 - 2))
    # print(shortcuts)
    return create_saved_time_dict(shortcuts)


def part_2(puzzle_input, picoseconds, min_save):
    grid = parse_grid(puzzle_input)
    start = find_first_position("S", grid)
    end = find_first_position("E", grid)
    grid[end[1]][end[0]] = "."
    grid = solve_maze(grid, start)
    # print_grid(grid, 1)
    cheat_diamond = generate_cheat_diamond(picoseconds)
    # print_grid(cheat_diamond)
    shortcuts = set()
    for pos, val in iter_grid(grid):
        if val == "#":
            continue
        for s in apply_cheat(grid, pos, cheat_diamond):
            if s[2] >= min_save:
                shortcuts.add(s)
    return create_saved_time_dict(shortcuts)


def test():
    part_1_sample_result = {2: 14, 4: 14, 6: 2, 8: 4, 10: 2, 12: 3, 20: 1, 36: 1, 38: 1, 40: 1, 64: 1}
    part_2_sample_result = {50: 32, 52: 31, 54: 29, 56: 39, 58: 25, 60: 23, 62: 20, 64: 19, 66: 12, 68: 14, 70: 12, 72: 22, 74: 4, 76: 3}
    result = True
    result &= test_sample_input(1, 1, part_1_sample_result, part_1)
    result &= test_sample_input(1, 2, part_2_sample_result, part_2, [20, 50])
    return result


def main():
    puzzle_input = get_puzzle_input()
    print("Part 1:", count_shortcuts(part_1(puzzle_input), 100))
    print("Part 2:", count_shortcuts(part_2(puzzle_input, 20, 100), 100))


if __name__ == "__main__":
    if test():
        main()
