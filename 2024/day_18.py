"""Day 18"""

from common import copy_grid, get_puzzle_input, test_sample_input


def create_maze(size, walls):
    return [[("#" if (x, y) in walls else ".") for x in range(size[0])] for y in range(size[1])]


def solve_maze(grid, start):
    maze = copy_grid(grid)
    maze[start[1]][start[0]] = 0
    queue = [start]
    while len(queue) > 0:
        x, y = queue.pop(0)
        val = maze[y][x]
        for n_x, n_y in [(x+dx, y+dy) for dx, dy in [(1, 0), (0, 1), (-1, 0), (0, -1)]]:
            if 0 <= n_y < len(maze) and\
                0 <= n_x < len(maze[0]):
                n_val = maze[n_y][n_x]
                if n_val == "#":
                    continue
                if n_val == ".":
                    maze[n_y][n_x] = val + 1
                    queue.append((n_x, n_y))
                    continue
                if isinstance(n_val, int) and int(n_val) > val + 1:
                    maze[n_y][n_x] = val + 1
                    queue.append((n_x, n_y))
                    continue
    return maze


def part_1(puzzle_input, size, fallen_bytes):
    fb_positions = [(int(x), int(y)) for x, _, y in [l.partition(",") for l in puzzle_input.split("\n")]]
    grid = create_maze(size, fb_positions[0:fallen_bytes])
    # print_grid(grid)
    start = (0,0)
    end = (size[0] - 1, size[1] - 1)
    maze = solve_maze(grid, start)
    # print_grid(solve_maze(grid, start))
    return maze[end[1]][end[0]]


def part_2(puzzle_input, size, min_fallen_bytes):
    fb_positions = [(int(x), int(y)) for x, _, y in [l.partition(",") for l in puzzle_input.split("\n")]]
    max_fallen_bytes = len(fb_positions)
    while min_fallen_bytes != max_fallen_bytes:
        fallen_bytes = int((max_fallen_bytes + min_fallen_bytes)/2)
        maze = create_maze(size, fb_positions[0:fallen_bytes])
        maze = solve_maze(maze, (0, 0))
        if maze[size[1] - 1][size[0] - 1] == ".":
            max_fallen_bytes = fallen_bytes
        else:
            min_fallen_bytes = fallen_bytes + 1
    return fb_positions[max_fallen_bytes - 1]


def test():
    part_1_sample_result = 22
    part_2_sample_result = (6, 1)
    test_sample_input(1, 1, part_1_sample_result, part_1, [(7, 7), 12])
    test_sample_input(1, 2, part_2_sample_result, part_2, [(7, 7), 12])


def main():
    puzzle_input = get_puzzle_input()
    print("Part 1:", part_1(puzzle_input, (71, 71), 1024))
    print("Part 2:", part_2(puzzle_input, (71, 71), 1024))


if __name__ == "__main__":
    test()
    main()
