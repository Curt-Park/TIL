import sys


filename = sys.argv[1] if len(sys.argv) > 1 else "example.txt"


with open(filename, "r") as f:
    lines = f.read().split()


# Read the map info.
start = (0, 0)
obstacles = set()
w, h = len(lines[0]), len(lines)
for i, line in enumerate(lines):
    for j, ch in enumerate(line):
        if ch == "#":
            obstacles.add((i, j))
        if ch == "^":
            start = (i, j)


def print_map(poss) -> None:
    for r in range(h):
        for c in range(w):
            if (r, c) in poss:
                print("X", end="")
            elif (r, c) in obstacles:
                print("#", end="")
            else:
                print(".", end="")
        print()


def part1() -> int:
    d_pos = {0: (-1, 0), 1: (0, 1), 2: (1, 0), 3: (0, -1)}
    pos, poss, direction = start, set(), 0
    while 0 <= pos[0] < h and 0 <= pos[1] < w:
        next_pos = (pos[0] + d_pos[direction][0], pos[1] + d_pos[direction][1])
        if next_pos in obstacles:  # Change the direction.
            direction = (direction + 1) % 4
            continue
        poss.add(pos)
        pos = next_pos  # Move.
    return len(poss)


def part2() -> int:
    # place an obstruction on any position of poss.
    # check it makes a cycle!
    def visit() -> bool:
        d_pos = {0: (-1, 0), 1: (0, 1), 2: (1, 0), 3: (0, -1)}
        pos, poss, visited, direction = start, set(), set(), 0
        while 0 <= pos[0] < h and 0 <= pos[1] < w:
            next_pos = (pos[0] + d_pos[direction][0], pos[1] + d_pos[direction][1])
            if next_pos in obstacles:  # Change the direction.
                direction = (direction + 1) % 4
                continue
            poss.add(pos)
            pos = next_pos  # Move.
            if (pos, direction) in visited:
                return False
            visited.add((pos, direction))
        return True

    sol = 0
    for r in range(h):
        for c in range(w):
            if (r, c) not in obstacles:
                obstacles.add((r, c))
                sol += not visit()
                obstacles.remove((r, c))
    return sol

print(part1())
print(part2())