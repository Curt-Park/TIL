#
# @lc app=leetcode id=134 lang=python3
#
# [134] Gas Station
#

# @lc code=start
class Solution:
    def canCompleteCircuit_0(self, gas: List[int], cost: List[int]) -> int:
        sum_diff, max_diff, max_diff_idx = 0, -10_000, -1
        for i in range(len(gas)):
            diff = gas[i] - cost[i] 
            sum_diff += diff
            prev_max_diff = max_diff
            max_diff = max(max_diff, diff)
            if max_diff != prev_max_diff:
                max_diff_idx = i
        return sum_diff < 0 and -1 or max_diff_idx

    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        partial_sum, min_partial_sum, start, total_diff = 0, 0, 0, 0
        for i in range(len(gas)):
            diff = gas[i] - cost[i] 
            partial_sum += diff
            prev_min_partial_sum = min_partial_sum
            min_partial_sum = min(min_partial_sum, partial_sum)
            if min_partial_sum != prev_min_partial_sum:
                start = i + 1
        return partial_sum < 0 and -1 or start
# @lc code=end

