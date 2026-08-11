# 300. Longest Increasing Subsequence
# https://leetcode.com/problems/longest-increasing-subsequence/
# Accepted: 2026-08-11T20:16:30.000Z
# Language: Python3
# Collection: dynamic-programming
# Runtime: 1226 ms · Beats 61%
# Memory: 19.3 MB · Beats 97.15%
# Submission: https://leetcode.com/submissions/detail/2103411904/

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        ###dp[i] : length of the LIS in nums[:j]
        n = len(nums)
        dp = [1]* n

        for i in range(n) : 
            for j in range(i) : 
                if nums[j] < nums[i] : 
                    dp[i] = max(1 + dp[j], dp[i])
        return max(dp)
