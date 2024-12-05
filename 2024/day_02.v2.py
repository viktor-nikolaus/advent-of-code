"""Day 2 v2"""

from common.common import get_puzzle_input

PUZZLE_INPUT = get_puzzle_input()

def extract_diff_list(report):
    levels = [int(l) for l in report.split(" ")]
    return [levels[i] - levels[i-1] for i in range(1, len(levels))]

def is_report_ok_v1(report) -> bool:
    return len([l for l in report if l == 0 or l > 3 or l < -3]) == 0\
        and (all(l > 0 for l in report) or all(l < 0 for l in report))

# defect
def is_report_ok_v2(report) -> bool:
    inc = len([l for l in report if l > 0]) - len([l for l in report if l < 0])
    if inc == 0:
        return False
    errors = [[i, l] for i, l in enumerate(report) if l == 0 or l > 3 or l < -3 or l * inc < 0]
    if len(errors) > 2:
        return False
    if len(errors) == 0 or len(errors) == 1 and errors[0][0] == 0 or errors[0][0] == len(report) - 1:
        return True
    if len(errors) == 1:
        return (report[errors[0][0] - 1] + errors[0][1]) * inc > 0
    if errors[0][0] + 1 == errors[1][0]:
        merge = errors[0][1] + errors[1][1]
        return 3 >= merge >= -3 and merge != 0 and merge * inc > 0
    return False

reports = [extract_diff_list(l) for l in PUZZLE_INPUT.split("\n")]
print(len(list(filter(is_report_ok_v1, reports))))
print(len(list(filter(is_report_ok_v2, reports))))
