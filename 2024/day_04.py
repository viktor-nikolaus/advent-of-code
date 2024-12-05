"""Day 4"""

from common.common import get_puzzle_input

PUZZLE_INPUT = get_puzzle_input()


def find_crossword(grid, x, y, dx, dy, needle):
    max_x = x + (len(needle)-1)*dx
    max_y = y + (len(needle)-1)*dy
    if y >= len(grid) or y < 0 or x >= len(grid[y]) or x < 0:
        return 0
    if max_y >= len(grid) or max_y < 0 or max_x >= len(grid[y]) or max_x < 0:
        return 0
    for i, c in enumerate(needle):
        if grid[y+dy*i][x+dx*i] != c:
            return 0
    return 1


def part1():
    grid = [list(l) for l in PUZZLE_INPUT.split("\n")]
    count = 0
    for y, _ in enumerate(grid):
        for x, _ in enumerate(grid[y]):
            if grid[y][x] == "X":
                count += find_crossword(grid, x, y, 1, 0, "XMAS")
                count += find_crossword(grid, x, y, -1, 0, "XMAS")
                count += find_crossword(grid, x, y, 0, 1, "XMAS")
                count += find_crossword(grid, x, y, 0, -1, "XMAS")
                count += find_crossword(grid, x, y, 1, 1, "XMAS")
                count += find_crossword(grid, x, y, 1, -1, "XMAS")
                count += find_crossword(grid, x, y, -1, 1, "XMAS")
                count += find_crossword(grid, x, y, -1, -1, "XMAS")
    print(count)


def part2():
    grid = [list(l) for l in PUZZLE_INPUT.split("\n")]
    count = 0
    for y, _ in enumerate(grid):
        for x, _ in enumerate(grid[y]):
            if grid[y][x] == "A":
                a = find_crossword(grid, x-1, y-1, 1, 1, "MAS") > 0
                b = find_crossword(grid, x+1, y+1, -1, -1, "MAS") > 0
                c = find_crossword(grid, x-1, y+1, 1, -1, "MAS") > 0
                d = find_crossword(grid, x+1, y-1, -1, 1, "MAS") > 0
                count += 1 if (a or b) and (c or d) else 0
    print(count)


part1()
part2()
