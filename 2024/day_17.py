"""Day 17"""

from common import get_puzzle_input, test_sample_input


class Computer():
    def __init__(self, regs):
        self.regs = list(regs)
        self.program = []
        self.pointer  = 0
        self.expected_output = None
        self.successful = False

    def __get_literal_operand(self) -> int:
        v = self.program[self.pointer]
        self.pointer += 1
        return v

    def __get_combo_operand(self) -> int:
        v = self.program[self.pointer]
        self.pointer += 1
        if 0 <= v <= 3:
            return v
        if 4 <= v <= 6:
            return self.regs[v - 4]
        return None

    def __is_correct_output(self, output) -> bool:
        return self.expected_output is None\
            or self.expected_output.startswith(",".join(output))

    def set_registers(self, reg_a, reg_b, reg_c):
        self.regs = list([reg_a, reg_b, reg_c])

    def set_expected_output(self, expected_output):
        self.expected_output = expected_output

    def was_successful(self) -> bool:
        return self.successful

    def execute(self, program) -> str:
        self.program = program
        self.pointer  = 0
        output = []
        while self.pointer < len(program):
            match(program[self.pointer]):
                case 0: # adv : a-division
                    self.pointer += 1
                    self.regs[0] = int(self.regs[0] / (2 ** self.__get_combo_operand()))
                case 1: # bxl : b-xor-literal
                    self.pointer += 1
                    self.regs[1] = self.regs[1] ^ self.__get_literal_operand()
                case 2: # bst : b-store
                    self.pointer += 1
                    self.regs[1] = self.__get_combo_operand() % 8
                case 3: # jnz : jump-not-zero
                    self.pointer += 1
                    if self.regs[0] != 0:
                        self.pointer = self.__get_literal_operand()
                    else:
                        self.pointer += 1
                case 4: # bxc : b-xor-c
                    self.pointer += 2
                    self.regs[1] = self.regs[1] ^ self.regs[2]
                case 5: # out : output
                    self.pointer += 1
                    output.append(str(self.__get_combo_operand() % 8))
                    if not self.__is_correct_output(output):
                        self.successful = False
                        return ",".join(output)
                case 6: # bdv : b-division
                    self.pointer += 1
                    self.regs[1] = int(self.regs[0] / (2 ** self.__get_combo_operand()))
                case 7: # cdv : c-division
                    self.pointer += 1
                    self.regs[2] = int(self.regs[0] / (2 ** self.__get_combo_operand()))
        self.successful = self.expected_output is None or ",".join(output) == self.expected_output
        return ",".join(output)


def parse_input(puzzle_input):
    regs, _, program = puzzle_input.partition("\n\n")
    reg_a, reg_b, reg_c = [int(l.partition(": ")[2]) for l in regs.split("\n")]
    program = [int(c) for c in program.partition(": ")[2].split(",")]
    return [reg_a, reg_b, reg_c, program]


def part_1(puzzle_input):
    reg_a, reg_b, reg_c, program = parse_input(puzzle_input)
    comp = Computer((reg_a, reg_b, reg_c))
    return comp.execute(program)


def part_2(puzzle_input):
    _, reg_b, reg_c, program = parse_input(puzzle_input)
    reg_a = 0
    comp = Computer((reg_a, reg_b, reg_c))
    for i in range(1, len(program) + 1):
        expected_output = ",".join([str(c) for c in program[-i:]])
        comp.set_expected_output(expected_output)
        found = False
        for temp_reg_a in range(8*8): # don't know why *8 ??? *2 was not enough for sample 2 but for main input
            comp.set_registers(reg_a + temp_reg_a, reg_b, reg_c)
            comp.execute(program)
            if comp.was_successful():
                found = True
                reg_a = (reg_a + temp_reg_a) * 8
                break
        if not found:
            print("No valid reg_a found")
            return ""
    reg_a = int(reg_a / 8)
    return reg_a


def test():
    part_1_sample_result = "4,6,3,5,6,3,5,2,1,0"
    part_2_sample_result = 117440
    test_sample_input(1, 1, part_1_sample_result, part_1)
    test_sample_input(2, 2, part_2_sample_result, part_2)


def main():
    puzzle_input = get_puzzle_input()
    print("Part 1:", part_1(puzzle_input))
    print("Part 2:", part_2(puzzle_input))


if __name__ == "__main__":
    test()
    main()
