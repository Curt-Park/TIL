from collections import Counter


def get_list() -> tuple[list[int], list[int]]:
    left, right = [], []
    with open("input.txt", "r") as file:
        for line in file:
            l, r = line.split()
            left.append(int(l))
            right.append(int(r))
    left.sort()
    right.sort()
    return left, right


def get_dist(left: list[int], right: list[int]) -> int:
    dist = 0
    for l, r in zip(left, right):
        dist += abs(l - r)
    return dist


def get_sim(left: list[int], right: list[int]) -> int:
    sim = 0
    c = Counter(right)
    for l in left:
        sim += l * c.get(l, 0)
    return sim


left, right = get_list()
print(get_dist(left, right))
print(get_sim(left, right))