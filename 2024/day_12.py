"""Day 12"""

from common import get_puzzle_input

PUZZLE_INPUT = get_puzzle_input()


def in_bounds(puzzle_map, point):
    return point[0] >= 0 and point[1] >= 0 and point[0] < len(puzzle_map[0]) and point[1] < len(puzzle_map)


def get_region(puzzle_map, x, y, points=None):
    if points is None:
        points = set()
    code = puzzle_map[y][x]
    points.add((x, y))
    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        point = (x + dx, y + dy)
        if in_bounds(puzzle_map, point):
            if puzzle_map[point[1]][point[0]] == code and point not in points:
                get_region(puzzle_map, point[0], point[1], points)
    region = {}
    region["points"] = points
    return region


def get_regions(puzzle_map):
    map_copy = [list(l) for l in puzzle_map]
    regions = []
    for y, _ in enumerate(map_copy):
        for x, _ in enumerate(map_copy[y]):
            if map_copy[y][x] != ".":
                region = get_region(map_copy, x, y)
                remove_region(map_copy, region)
                regions.append(region)
    return regions


def remove_region(puzzle_map, region):
    for x, y in region["points"]:
        puzzle_map[y][x] = "."


def calculate_perimeter(region):
    perimeter = 0
    for point in region["points"]:
        perimeter += 4
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            if (point[0] + dx, point[1] + dy) in region["points"]:
                perimeter -= 1
    region["perimeter"] = perimeter
    return region


def calculate_sides(region):
    min_x = min(p[0] for p in region["points"])
    max_x = max(p[0] for p in region["points"])
    min_y = min(p[1] for p in region["points"])
    max_y = max(p[1] for p in region["points"])
    s_x = max_x - min_x + 1
    s_y = max_y - min_y + 1
    fence_map = [[" " for _ in range(s_x * 2 + 1)] for _ in range(s_y * 2 + 1)]
    for p in region["points"]:
        fp = ((p[0] - min_x) * 2 + 1, (p[1] - min_y) * 2 + 1)
        fence_map[fp[1]][fp[0]] = "X"
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            if (p[0] + dx, p[1] + dy) not in region["points"]:
                fence_map[fp[1] + dy][fp[0] + dx] = "+"
    for y, l in enumerate(fence_map):
        for x, c in enumerate(l):
            if (y % 2 == 1) and (x % 2 == 1):
                continue
            if c == " ":
                f = 0
                for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    n_p = (x + dx, y + dy)
                    if in_bounds(fence_map, n_p) and fence_map[n_p[1]][n_p[0]] == "+":
                        f += 1
                if f >= 2:
                    fence_map[y][x] = "+"
    corners = 0
    for y, l in enumerate(fence_map):
        for x, c in enumerate(l):
            if c == "+":
                f_n = in_bounds(fence_map, (x, y-1)) and fence_map[y-1][x] == "+"
                f_s = in_bounds(fence_map, (x, y+1)) and fence_map[y+1][x] == "+"
                f_e = in_bounds(fence_map, (x+1, y)) and fence_map[y][x+1] == "+"
                f_w = in_bounds(fence_map, (x-1, y)) and fence_map[y][x-1] == "+"
                corners += 1 if (f_n or f_s) and (f_e or f_w) else 0
                if f_n and f_s and f_e and f_w:
                    corners += 1
    #print("\n".join("".join(l) for l in fence_map))
    #exit()
    region["sides"] = corners
    return region


puzzle_map = [list(l) for l in PUZZLE_INPUT.split("\n")]
regions = get_regions(puzzle_map)
regions = [calculate_perimeter(region) for region in regions]
#for region in regions:
#    print(f"{region['perimeter']} * {len(region['points'])} = {region['perimeter'] * len(region['points'])}")
print(sum(region["perimeter"] * len(region["points"]) for region in regions))

regions = [calculate_sides(region) for region in regions]
print(sum(region["sides"] * len(region["points"]) for region in regions))
