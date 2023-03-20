class Solution:
    def evenOddBit(self, n: int) -> List[int]:
        res = [0, 0]
        for i in range(10, -1, -1):
            d = 2 ** i
            if n < d:
                continue
            res[i % 2] += 1
            n -= d
        return res
