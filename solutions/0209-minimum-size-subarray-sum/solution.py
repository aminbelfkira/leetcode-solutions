# 209. Minimum Size Subarray Sum
# https://leetcode.com/problems/minimum-size-subarray-sum/
# Accepted: 2026-07-21T23:20:02.000Z
# Language: Python3
# Runtime: 19 ms · Beats 29.81%
# Memory: 30.6 MB · Beats 16.16%
# Submission: https://leetcode.com/submissions/detail/2076422028/

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:

        left = 0
        min_len = float('inf') 
        n = len(nums)
        current_sum =0

        for i in range(n) : 
            current_sum+= nums[i]
            while current_sum >= target: 
                min_len = min(min_len, i - left +1)
                current_sum -= nums[left]
                left+=1
        return min_len if min_len != float('inf') else 0
                
