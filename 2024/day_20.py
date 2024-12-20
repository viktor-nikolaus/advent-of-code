"""Day 20"""

from common import (find_first_position, get_puzzle_input, grid_at, parse_grid,
                    print_grid, solve_maze, test_sample_input)


def count_shortcuts(save_time_dict, min_time_saved):
    return sum(c for t, c in save_time_dict.items() if t >= min_time_saved)


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
                        shortcuts.add((n_pos_1, n_pos_2, n_val_2 - n_val_1))
                    else:
                        shortcuts.add((n_pos_2, n_pos_1, n_val_1 - n_val_2))
    # print(shortcuts)
    save_time_dict = {}
    for t in sorted([t-2 for _, _, t in shortcuts]):
        if t not in save_time_dict:
            save_time_dict[t] = 0
        save_time_dict[t] += 1
    return save_time_dict


def part_2(puzzle_input):
    return ""


def test():
    part_1_sample_result = {2: 14, 4: 14, 6: 2, 8: 4, 10: 2, 12: 3, 20: 1, 36: 1, 38: 1, 40: 1, 64: 1}
    part_2_sample_result = ""
    result = True
    result &= test_sample_input(1, 1, part_1_sample_result, part_1)
    result &= test_sample_input(1, 2, part_2_sample_result, part_2)
    return result


def main():
    puzzle_input = get_puzzle_input()
    print("Part 1:", count_shortcuts(part_1(puzzle_input), 100))
    print("Part 2:", part_2(puzzle_input))


if __name__ == "__main__":
    if test():
        main()
