# 209. Minimum Size Subarray Sum
# https://leetcode.com/problems/minimum-size-subarray-sum/
# Accepted: 2026-10-07T06:27:10.000Z
# Language: Python3
# Runtime: 20 ms · Beats 31.37%
# Memory: 30.5 MB · Beats 42.96%
# Submission: https://leetcode.com/submissions/detail/2164992517/

class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        left = 0 
        current_sum = 0
        min_sum = float('inf')

        for right, num in enumerate(nums) : 
            current_sum += num
            while current_sum >= target : 
                min_sum = min(min_sum, right-left +1)
                current_sum -= nums[left]
                left+=1
        
        return min_sum if min_sum != float('inf') else 0
