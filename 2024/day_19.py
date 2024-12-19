"""Day 19"""

from common import get_puzzle_input, test_sample_input


def parse_input(puzzle_input):
    available, _, requests = puzzle_input.partition("\n\n")
    available = set(available.split(", "))
    requests = requests.split("\n")
    return (available, requests)


def is_possible(available, request):
    if len(request) == 0:
        return True
    for a in available:
        if request.startswith(a) and is_possible(available, request[len(a):]):
            return True
    return False


def is_necessary(option, options, request):
    return not is_possible([o for o in options if o != option], request)


def get_possibilities(available, request, cache):
    if len(request) == 0:
        return 1
    if request in cache:
        return cache[request]
    options = set(sorted([a for a in available if a in request], key=len, reverse=True))
    c = 0
    for o in options:
        if request.startswith(o):
            c += get_possibilities(options, request[len(o):], cache)
    cache[request] = c
    return c


def part_1(puzzle_input):
    available, requests = parse_input(puzzle_input)
    return len([r for r in requests if is_possible(available, r)])


def part_2(puzzle_input):
    cache = {}
    available, requests = parse_input(puzzle_input)
    return sum(get_possibilities(available, r, cache) for r in requests if is_possible(available, r))


def test():
    part_1_sample_result = 6
    part_2_sample_result = 16
    result = True
    result &= test_sample_input(1, 1, part_1_sample_result, part_1)
    result &= test_sample_input(1, 2, part_2_sample_result, part_2)
    return result


def main():
    puzzle_input = get_puzzle_input()
    print("Part 1:", part_1(puzzle_input))
    print("Part 2:", part_2(puzzle_input))


if __name__ == "__main__":
    if test():
        main()
