"""Day 22"""

from common import get_puzzle_input, test_sample_input


def mix_and_prune(number, other):
    return (int(number) ^ int(other)) & 0xFFFFFF


def generate_secret_number(number, iterations):
    secret_number = number
    for _ in range(iterations):
        new_secret_number = secret_number
        new_secret_number = mix_and_prune(new_secret_number, new_secret_number << 6)
        new_secret_number = mix_and_prune(new_secret_number, new_secret_number >> 5)
        new_secret_number = mix_and_prune(new_secret_number, new_secret_number << 11)
        secret_number = new_secret_number
    return secret_number


def part_1(puzzle_input, iterations):
    return sum(generate_secret_number(int(l), iterations) for l in puzzle_input.split("\n"))


def part_2(puzzle_input, max_iterations):
    seq_dict = {}
    for l in set(puzzle_input.split("\n")):
        secret_number = int(l)
        last_prices = [secret_number % 10]
        seq_dict[l] = {}
        for _ in range(max_iterations):
            secret_number = generate_secret_number(secret_number, 1)
            last_prices.append(secret_number % 10)
            if len(last_prices) < 5:
                continue
            seq = (last_prices[-4] - last_prices[-5],
                   last_prices[-3] - last_prices[-4],
                   last_prices[-2] - last_prices[-3],
                   last_prices[-1] - last_prices[-2])
            if seq not in seq_dict[l]:
                seq_dict[l][seq] = last_prices[-1]
            last_prices.pop(0)

    all_seqs = set()
    for _, seqs in seq_dict.items():
        all_seqs = all_seqs.union(seqs)
    best_seq = None
    best_bananas = None
    for seq in all_seqs:
        total = 0
        for l, seqs in seq_dict.items():
            if seq in seqs:
                total += seqs[seq]
        if best_bananas is None or best_bananas < total:
            best_bananas = total
            best_seq = seq
    # print(best_seq, best_bananas)
    return best_bananas


def test():
    part_1_sample_result = 37327623
    part_2_sample_result = 23
    result = True
    result &= test_sample_input(1, 1, part_1_sample_result, part_1, [2000])
    result &= test_sample_input(2, 2, part_2_sample_result, part_2, [2000])
    return result


def main():
    puzzle_input = get_puzzle_input()
    print("Part 1:", part_1(puzzle_input, 2000))
    print("Part 2:", part_2(puzzle_input, 2000))


if __name__ == "__main__":
    if test():
        main()
