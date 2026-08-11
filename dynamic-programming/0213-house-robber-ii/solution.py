# 213. House Robber II
# https://leetcode.com/problems/house-robber-ii/
# Accepted: 2026-08-11T18:43:52.000Z
# Language: Python3
# Collection: dynamic-programming
# Runtime: 0 ms · Beats 100%
# Memory: 19.3 MB · Beats 68.45%
# Submission: https://leetcode.com/submissions/detail/2103333084/

class Solution:
    def rob(self, nums: List[int]) -> int:
        
        n = len(nums)
        if n == 1:
            return nums[0]

        def rob_linear(houses):
            prev2, prev1 = 0, 0
            for money in houses:
                prev2, prev1 = prev1, max(prev1, prev2 + money)
            return prev1

        return max(rob_linear(nums[:-1]), rob_linear(nums[1:]))
