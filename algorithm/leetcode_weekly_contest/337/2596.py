class Solution:
    def checkValidGrid(self, grid: List[List[int]]) -> bool:
        n = len(grid)
        r = c = 0
        moves = [(-2, -1), (-1, -2), (2, -1), (-1, 2), (-2, 1), (1, -2), (2, 1), (1, 2)]
        for i in range(1, n * n):
            for dr, dc in moves:
                next_r, next_c = r + dr, c + dc
                if 0 <= next_r < n and 0 <= next_c < n and grid[next_r][next_c] == i:
                    r, c = next_r, next_c
                    break
            else:
                return False
        return True
