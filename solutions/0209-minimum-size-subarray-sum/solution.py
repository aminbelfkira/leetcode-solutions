# 209. Minimum Size Subarray Sum
# https://leetcode.com/problems/minimum-size-subarray-sum/
# Accepted: 2026-09-11T20:42:34.000Z
# Language: Python3
# Runtime: 19 ms · Beats 44.66%
# Memory: 30.6 MB · Beats 16.85%
# Submission: https://leetcode.com/submissions/detail/2138961512/

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0 
        current_sum = 0
        min_len = float('inf')
        for right, num in enumerate(nums) : 
            current_sum += num
            while current_sum >= target : 
                min_len = min(min_len, right- left +1)
                current_sum -= nums[left]
                left +=1
        return min_len if min_len != float('inf') else 0
