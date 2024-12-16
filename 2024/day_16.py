"""Day 16"""

from common import (copy_grid, find_first_position, get_puzzle_input,
                    parse_grid, print_grid)

PUZZLE_INPUT = get_puzzle_input()
PUZZLE_GRID = parse_grid(PUZZLE_INPUT)
START = find_first_position("S", PUZZLE_GRID)
END = find_first_position("E", PUZZLE_GRID)

grid = copy_grid(PUZZLE_GRID)
grid[START[1]][START[0]] = 0
queue = [(START, (1, 0))] # (position, direction)
while len(queue) > 0:
    position, direction = queue.pop(0)
    for cur_dir in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
        cost = grid[position[1]][position[0]] + 1
        if cur_dir == direction:
            pass # no rotation cost
        elif (-cur_dir[0], -cur_dir[1]) == direction:
            continue # never going back
        else:
            cost += 1000 # rotating 90 deg
        new_pos = (position[0] + cur_dir[0], position[1] + cur_dir[1])
        if 0 <= new_pos[0] < len(grid[0]) and 0 <= new_pos[1] < len(grid):
            new_pos_value = grid[new_pos[1]][new_pos[0]]
            if new_pos_value == "#":
                continue
            if new_pos_value in [".", "S", "E"]:
                grid[new_pos[1]][new_pos[0]] = cost
                queue = [q for q in queue if q[0] != new_pos]
                queue.append((new_pos, cur_dir))
                continue
            if isinstance(new_pos_value, int) and new_pos_value > cost:
                grid[new_pos[1]][new_pos[0]] = cost
                queue = [q for q in queue if q[0] != new_pos]
                queue.append((new_pos, cur_dir))
                continue

print(grid[END[1]][END[0]])
