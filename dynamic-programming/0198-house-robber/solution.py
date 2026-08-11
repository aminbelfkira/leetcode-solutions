# 198. House Robber
# https://leetcode.com/problems/house-robber/
# Accepted: 2026-08-11T18:40:19.000Z
# Language: Python3
# Collection: dynamic-programming
# Runtime: 0 ms · Beats 100%
# Memory: 19.3 MB · Beats 61.4%
# Submission: https://leetcode.com/submissions/detail/2103329065/

class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [0] * n

        if n <= 2 : 
            return max(nums)
        dp[0] = nums[0]
        dp[1] = max(nums[:2])

        for i in range(2, n) : 
            dp[i] = max(nums[i] + dp[i-2], dp[i-1])
        return dp[n-1]
