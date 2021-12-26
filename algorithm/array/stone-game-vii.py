"""
https://leetcode.com/problems/stone-game-vii/

1690. Stone Game VII
Medium

Alice and Bob take turns playing a game, with Alice starting first.

There are n stones arranged in a row. On each player's turn, they can remove either the leftmost stone or the rightmost stone from the row and receive points equal to the sum of the remaining stones' values in the row. The winner is the one with the higher score when there are no stones left to remove.

Bob found that he will always lose this game (poor Bob, he always loses), so he decided to minimize the score's difference. Alice's goal is to maximize the difference in the score.

Given an array of integers stones where stones[i] represents the value of the ith stone from the left, return the difference in Alice and Bob's score if they both play optimally.



Example 1:

Input: stones = [5,3,1,4,2]
Output: 6
Explanation:
- Alice removes 2 and gets 5 + 3 + 1 + 4 = 13 points. Alice = 13, Bob = 0, stones = [5,3,1,4].
- Bob removes 5 and gets 3 + 1 + 4 = 8 points. Alice = 13, Bob = 8, stones = [3,1,4].
- Alice removes 3 and gets 1 + 4 = 5 points. Alice = 18, Bob = 8, stones = [1,4].
- Bob removes 1 and gets 4 points. Alice = 18, Bob = 12, stones = [4].
- Alice removes 4 and gets 0 points. Alice = 18, Bob = 12, stones = [].
The score difference is 18 - 12 = 6.
Example 2:

Input: stones = [7,90,5,1,100,10,10,2]
Output: 122


Constraints:

n == stones.length
2 <= n <= 1000
1 <= stones[i] <= 1000
"""


class Solution:
    def stoneGameVIIiter(self, stones: List[int]) -> int:
        """Add List DP. O(N^2): Passed."""
        dp = [[0] * len(stones) for _ in range(len(stones))]
        partial_sum = [0] + list(accumulate(stones))
        for l in range(len(stones) - 2, -1, -1):
            for r in range(l + 1, len(stones)):
                score_lr = partial_sum[r + 1] - partial_sum[l]
                dp[l][r] = max(
                    score_lr - stones[l] - dp[l + 1][r],
                    score_lr - stones[r] - dp[l][r - 1],
                )
        return dp[0][len(stones) - 1]

    def stoneGameVIIListDP(self, stones: List[int]) -> int:
        """Add List DP. O(N^2): Passed."""
        def do_stone_game(l: int, r: int) -> int:
            if l == r:
                return 0
            if dp[l][r] == 0:
                score_lr = partial_sum[r + 1] - partial_sum[l]
                dp[l][r] = max(
                    score_lr - stones[l] - do_stone_game(l + 1, r),
                    score_lr - stones[r] - do_stone_game(l, r - 1),
                )
            return dp[l][r]
        dp = [[0] * len(stones) for _ in range(len(stones))]
        partial_sum = [0] + list(accumulate(stones))
        return do_stone_game(0, len(stones) - 1)

    def stoneGameVIIDictDP(self, stones: List[int]) -> int:
        """Add DP. O(N^2): TLE."""
        def do_stone_game(l: int, r: int) -> int:
            if l == r:
                return 0
            if (l, r) not in dp:
                score_lr = partial_sum[r + 1] - partial_sum[l]
                dp[l, r] = max(
                    score_lr - stones[l] - do_stone_game(l + 1, r),
                    score_lr - stones[r] - do_stone_game(l, r - 1),
                )
            return dp[l, r]
        dp: Dict[Tuple[int, int], int] = {}
        partial_sum = [0] + list(accumulate(stones))
        return do_stone_game(0, len(stones) - 1)

    def stoneGameVIIRec2(self, stones: List[int]) -> int:
        """Make it simple. O(2^N): TLE."""
        def do_stone_game(l: int, r: int) -> int:
            if l == r:
                return 0
            score_lr = partial_sum[r + 1] - partial_sum[l]
            return max(
                score_lr - stones[l] - do_stone_game(l + 1, r),
                score_lr - stones[r] - do_stone_game(l, r - 1),
            )
        partial_sum = [0] + list(accumulate(stones))
        return do_stone_game(0, len(stones) - 1)

    def stoneGameVIIRec1(self, stones: List[int]) -> int:
        """s_a, s_b => diff. O(2^N): TLE."""
        def do_stone_game(l: int, r: int, diff: int, i: int) -> int:
            if l == r:
                return diff
            score_lr = scores[r] - scores[l - 1]
            l_s, r_s = stones[l], stones[r]
            # alice
            if (i + 1) % 2:
                return max(
                    do_stone_game(l + 1, r, diff + score_lr - l_s, i + 1),
                    do_stone_game(l, r - 1, diff + score_lr - r_s, i + 1),
                )
            # bob
            return min(
                do_stone_game(l + 1, r, diff - (score_lr - l_s), i + 1),
                do_stone_game(l, r - 1, diff - (score_lr - r_s), i + 1),
            )
        scores = defaultdict(int)
        for i, s in enumerate(stones):
            scores[i] = scores[i - 1] + s
        return do_stone_game(0, len(stones) - 1, 0, 0)

    def stoneGameVIIRec0(self, stones: List[int]) -> int:
        """Intuitive approach of O(2^N): TLE."""
        def turn_alice(l: int, r: int, s_a: int, s_b: int) -> int:
            if l == r:
                return s_a - s_b
            score_lr = scores[r] - scores[l - 1]
            l_s, r_s = stones[l], stones[r]
            return max(
                turn_bob(l + 1, r, s_a + score_lr - l_s, s_b),
                turn_bob(l, r - 1, s_a + score_lr - r_s, s_b),
            )

        def turn_bob(l: int, r: int, s_a: int, s_b: int) -> int:
            if l == r:
                return s_a - s_b
            score_lr = scores[r] - scores[l - 1]
            l_s, r_s = stones[l], stones[r]
            return min(
                turn_alice(l + 1, r, s_a, s_b + score_lr - l_s),
                turn_alice(l, r - 1, s_a, s_b + score_lr - r_s),
            )

        scores = defaultdict(int)
        for i, s in enumerate(stones):
            scores[i] = scores[i - 1] + s
        return turn_alice(0, len(stones) - 1, 0, 0)
