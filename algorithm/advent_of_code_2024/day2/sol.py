def validate(report: list[int]) -> bool:
    if len(report) <= 1:
        return True
    must_increase = report[0] < report[1]
    must_decrease = not must_increase
    for i in range(len(report) - 1):
        if must_increase and report[i] > report[i+1]:
            return False
        if must_decrease and report[i] < report[i+1]:
            return False
        if not (1 <= abs(report[i+1] - report[i]) <= 3):
            return False
    return True


def check_safety() -> int:
    n_safe = 0
    with open("input.txt", "r") as f:
        lines = f.readlines()
    for line in lines:
        report = [int(n) for n in line.split()]
        n_safe += validate(report) or any(
            validate(report[:i]+report[i+1:]) for i in range(len(report))
        )
    return n_safe


print(check_safety())