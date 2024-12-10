import sys

from collections import defaultdict
from functools import lru_cache


filename = sys.argv[1] if len(sys.argv) > 1 else "test.txt"

g = defaultdict(set)
pages = []

with open(filename, "r") as f:
    edges, queries = f.read().split("\n\n")
    for x, y in [edge.split("|") for edge in edges.split()]:
        g[int(x)].add(int(y))
    for query in queries.split():
        p = list(map(int, query.split(",")))
        pages.append(p)


def validate(page) -> bool:
    for i, x in enumerate(page):
        for j, y in enumerate(page):
            if i < j and x in g[y]:
                return False
    return True


def sort(page) -> list[int]:
    s_nodes = set(page)
    d_reachable = dict()
    for n in page:
        d_reachable[n] = g[n] & s_nodes

    sorted_page = []
    while d_reachable:
        placed = 0
        for n in d_reachable:
            if len(d_reachable[n]) == 0:  # must be placed at the end!
                sorted_page.append(n)
                d_reachable.pop(n)
                placed = n
                break
        for n in d_reachable:  # remove the node already placed
            d_reachable[n].remove(placed)
    return sorted_page[::-1]


def print_queue_0(pages) -> int:
    s = 0
    for page in pages:
        if validate(page):
            mid = page[len(page) // 2]
            s += mid
    return s


def print_queue_1(pages) -> int:
    s = 0
    for page in pages:
        if validate(page):
            continue
        # sort
        sorted_page = sort(page)
        mid = sorted_page[len(sorted_page) // 2]
        s += mid
    return s


print(print_queue_0(pages))
print(print_queue_1(pages))