#
# @lc app=leetcode id=134 lang=python3
#
# [134] Gas Station
#

# @lc code=start
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        sum_diff, max_diff, max_diff_idx = 0, -10_000, -1
        for i in range(len(gas)):
            diff = gas[i] - cost[i] 
            sum_diff += diff
            prev_max_diff = max_diff
            max_diff = max(max_diff, diff)
            if max_diff != prev_max_diff:
                max_diff_idx = i
        return sum_diff < 0 and -1 or max_diff_idx
# @lc code=end

