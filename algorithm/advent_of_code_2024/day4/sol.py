from functools import lru_cache


with open("input.txt", "r") as f:
    puzzle = f.read().strip().splitlines()


def search_xmas_0(puzzle: list[str]) -> int:
    w, h = len(puzzle[0]), len(puzzle)
    cnt = 0
    directions = [
        [lambda r, c: r+3<h, (0,0), (1,0), (2,0), (3,0)],
        [lambda r, c: c+3<w, (0,0), (0,1), (0,2), (0,3)],
        [lambda r, c: r-3>=0, (0,0), (-1,0), (-2,0), (-3,0)],
        [lambda r, c: c-3>=0, (0,0), (0,-1), (0,-2), (0,-3)],
        [lambda r, c: r+3<h and c+3<w, (0,0), (1,1), (2,2), (3,3)],
        [lambda r, c: r-3>=0 and c-3>=0, (0,0), (-1,-1), (-2,-2), (-3,-3)],
        [lambda r, c: r-3>=0 and c+3<w, (0,0), (-1,1), (-2,2), (-3,3)],
        [lambda r, c: r+3<h and c-3>=0, (0,0), (1,-1), (2,-2), (3,-3)],
    ]
    word = "XMAS"

    for r in range(h):
        for c in range(w):
            for dir in directions:
                if not dir[0](r, c):
                    continue
                for i, (dr, dc) in enumerate(dir[1:]):
                    if word[i] != puzzle[r+dr][c+dc]:     
                        break
                else:
                    cnt += 1
    return cnt


def search_xmas_1(puzzle: list[str]) -> int:
    w, h = len(puzzle[0]), len(puzzle)
    cnt = 0
    for r in range(1, h-1):
        for c in range(1, w-1):
            if puzzle[r][c] != "A":
                continue
            if puzzle[r-1][c-1] == "M" and puzzle[r-1][c+1] == "M" and puzzle[r+1][c-1] =="S" and puzzle[r+1][c+1] =="S":
                cnt += 1
            if puzzle[r-1][c-1] == "S" and puzzle[r-1][c+1] == "S" and puzzle[r+1][c-1] =="M" and puzzle[r+1][c+1] =="M":
                cnt += 1
            if puzzle[r-1][c-1] == "M" and puzzle[r-1][c+1] == "S" and puzzle[r+1][c-1] =="M" and puzzle[r+1][c+1] =="S":
                cnt += 1
            if puzzle[r-1][c-1] == "S" and puzzle[r-1][c+1] == "M" and puzzle[r+1][c-1] =="S" and puzzle[r+1][c+1] =="M":
                cnt += 1
    return cnt

print(search_xmas_1(puzzle))