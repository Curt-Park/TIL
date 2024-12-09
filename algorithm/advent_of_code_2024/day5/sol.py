from collections import defaultdict


g = defaultdict(set)
pages = []

with open("test.txt", "r") as f:
    for line in f.readlines():
        split = line.split("|")
        if len(split) > 1:
            g[int(split[0])].add(int(split[1]))
        split = line.split(",")
        if len(split) > 1:
            p = [int(n) for n in split]
            pages.append(p[::-1])


def validate(g, page) -> bool:
    for i in range(len(page) - 1):
        for j in range(i+1, len(page)):
            if page[j] in g[page[i]]:
                return False
    return True


def print_queue_0(g, pages) -> int:
    s = 0
    for page in pages:
        if not validate(g, page):
            continue
        mid = page[len(page) // 2]
        s += mid
    return s


def print_queue_1(g, pages) -> int:
    s = 0
    for page in pages:
        if validate(g, page):
            continue
        print("invalid:", page[::-1])
        # sort... how?
        mid = page[len(page) // 2]
        s += mid
    return s


print(print_queue_0(g, pages))
print(print_queue_1(g, pages))