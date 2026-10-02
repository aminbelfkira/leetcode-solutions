# 300. Longest Increasing Subsequence
# https://leetcode.com/problems/longest-increasing-subsequence/
# Accepted: 2026-10-02T16:20:22.000Z
# Language: Python3
# Collection: top-interview-150
# Runtime: 1254 ms · Beats 46.06%
# Memory: 19.3 MB · Beats 97.71%
# Submission: https://leetcode.com/submissions/detail/2160330832/

class Solution:
    def lengthOfLIS(self, nums: list[int]) -> int:
        n = len(nums) 
        dp = [1] *n 
        for i in range(n) : 
            for j in range(i) : 
                if nums[j] < nums[i] : 
                    dp[i] = max(1 + dp[j], dp[i])
        return max(dp)
