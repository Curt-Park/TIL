import sys
from collections import defaultdict


filename = sys.argv[1] if len(sys.argv) > 1 else "test.txt"

g = defaultdict(set)
v = set()
pages = []

with open(filename, "r") as f:
    edges, queries = f.read().split("\n\n")
    for x, y in [edge.split("|") for edge in edges.split()]:
        g[int(x)].add(int(y))
    for query in queries.split():
        p = []
        for n in query.split(","):
            p.append(int(n))
            v.add(int(n))
        pages.append(p)


def get_reachable(graph, start) -> set[int]:
    def dfs(node, visited):
        if node in visited:
            return
        visited.add(node)
        for neighbor in graph[node]:
            dfs(neighbor, visited)

    visited = set()
    dfs(start, visited)
    visited.remove(start)
    return visited


def validate(g, page) -> bool:
    for i, x in enumerate(page):
        for j, y in enumerate(page):
            if i < j and x in g[y]:
                return False
    return True


def print_queue_0(g, pages) -> int:
    s = 0
    for page in pages:
        if validate(g, page):
            mid = page[len(page) // 2]
            s += mid
    return s


def print_queue_1(g, pages) -> int:
    reachable = defaultdict(set)
    for node in v:
        reachable[node] = get_reachable(g, node)

    s = 0
    for page in pages:
        if validate(g, page):
            continue
        # sort
        sorted_page = []
        for node in page:
            sorted_page.append(node)
            for i in range(len(sorted_page)-1, 0, -1):
                if sorted_page[i] in reachable[sorted_page[i-1]]:
                    break
                sorted_page[i], sorted_page[i-1] = sorted_page[i-1], sorted_page[i]

        # validate
        for i, x in enumerate(sorted_page):
            for j, y in enumerate(sorted_page):
                if i < j and y not in reachable[x]:
                    print(sorted_page)

        mid = sorted_page[len(sorted_page) // 2]
        s += mid
    return s


print(print_queue_0(g, pages))
print(print_queue_1(g, pages))