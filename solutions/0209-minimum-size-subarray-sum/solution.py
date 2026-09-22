# 209. Minimum Size Subarray Sum
# https://leetcode.com/problems/minimum-size-subarray-sum/
# Accepted: 2026-09-22T06:39:30.000Z
# Language: Python3
# Runtime: 16 ms · Beats 64.28%
# Memory: 30.5 MB · Beats 43.11%
# Submission: https://leetcode.com/submissions/detail/2149419102/

class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        
        min_len = float('inf')

        left = 0
        current_sum = 0
        for right, num in enumerate(nums) : 
            current_sum += num
            while current_sum >= target :
                min_len = min(min_len, right - left +1)
                current_sum -= nums[left]
                left +=1
        return min_len if min_len != float('inf') else 0
