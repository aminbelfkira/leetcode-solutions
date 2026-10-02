# 198. House Robber
# https://leetcode.com/problems/house-robber/
# Accepted: 2026-10-02T16:03:00.000Z
# Language: Python3
# Collection: top-interview-150
# Runtime: 0 ms · Beats 100%
# Memory: 19.2 MB · Beats 63.31%
# Submission: https://leetcode.com/submissions/detail/2160314173/

class Solution:
    def rob(self, nums: list[int]) -> int:
        n = len(nums) 
        if n <=2 : 
            return max(nums)
        dp = [0]* n
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        
        for i in range(2,n) :
            dp[i] = max(nums[i] + dp[i-2], dp[i-1])
        return dp[n-1]
