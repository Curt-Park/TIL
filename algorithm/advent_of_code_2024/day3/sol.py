def mull_it_over() -> int:
    with open("input.txt", "r") as f:
        inp = "".join(f.readlines())
    do = True
    sum_muls = 0
    i = 0
    while i < len(inp):
        while i < len(inp) and not inp[i] in {"m", "d"}:
            i += 1
        if inp[i: i+2] == "do":
            do = not inp[i+2:i+5] == "n't"
            i += 2 if do else 5
            continue
        if not do:
            i += 1
            continue
        if inp[i+1: i+4] != "ul(":
            i += 1
            continue
        i = start = i + 4
        while i < len(inp) and inp[i].isdigit() or inp[i] == ",":
            i += 1
        if inp[i] != ")":
            continue
        digits = inp[start: i]
        num1, num2 = [int(n) for n in digits.split(",")]
        sum_muls += num1 * num2
    return sum_muls

print(mull_it_over())